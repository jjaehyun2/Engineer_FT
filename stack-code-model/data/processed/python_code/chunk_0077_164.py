package com.axis.rtspclient {
  import com.axis.ClientEvent;
  import com.axis.ErrorManager;
  import com.axis.Logger;
  import com.axis.rtspclient.ByteArrayUtils;
  import com.axis.rtspclient.RTP;
  import com.axis.rtspclient.FLVTag;

  import flash.events.Event;
  import flash.events.EventDispatcher;
  import flash.net.FileReference;
  import flash.net.NetStream;
  import flash.utils.ByteArray;

  import mx.utils.Base64Decoder;

  public class FLVMux extends EventDispatcher {
    private const EMPTY_BUF:ByteArray = new ByteArray();

    private var sdp:SDP;
    private var container:ByteArray = new ByteArray();
    private var loggedBytes:ByteArray = new ByteArray();
    private var lastTimestamp:Number = -1;
    private var firstTimestamp:Number = -1;

    private var sps:ByteArray = EMPTY_BUF;
    private var pps:ByteArray = EMPTY_BUF;

    public function FLVMux(sdp:SDP) {
      container.writeByte(0x46); // 'F'
      container.writeByte(0x4C); // 'L'
      container.writeByte(0x56); // 'V'
      container.writeByte(0x01); // Version 1
      container.writeByte(
        (sdp.getMediaBlock('audio') ? 0x01 : 0x00) << 2 |
        (sdp.getMediaBlock('video') ? 0x01 : 0x00) << 0
      );
      container.writeUnsignedInt(0x09) // Reserved: usually is 0x09
      container.writeUnsignedInt(0x0) // Previous tag size: shall be 0

      this.sdp = sdp;

      if (sdp.getMediaBlock('video') && sdp.getMediaBlock('video').hasOwnProperty('fmtp')) {
        /* Initial parameters must be taken from SDP file. Additional may be received as NAL */
        var sets:Array = sdp.getMediaBlock('video').fmtp['sprop-parameter-sets'].split(',');
        var sps:Base64Decoder = new Base64Decoder();
        var pps:Base64Decoder = new Base64Decoder();
        sps.decode(sets[0]);
        pps.decode(sets[1]);
        this.sps = sps.toByteArray();
        this.pps = pps.toByteArray();
        createVideoSpecificConfigTag();
      }

      if (sdp.getMediaBlock('audio')) {
        createAudioSpecificConfigTag(sdp.getMediaBlock('audio'));
      }
    }

    private function createVideoSpecificConfigTag():void {
      if (this.sps.bytesAvailable != 0 && this.pps.bytesAvailable != 0) {
        var spsbit:BitArray = new BitArray(sps);
        var params:Object = parseSPS(spsbit);
        createDecoderConfigRecordTag(sps, pps, params);
        createMetaDataTag(params);
      }
    }

    private function writeECMAArray(contents:Object):uint {
      var size:uint = 0;
      var count:uint = 0;

      for (var s:String in contents) count++;

      container.writeByte(0x08); // ECMA Array Type
      container.writeUnsignedInt(count); // (Approximate) number of elements in ECMA array
      size += 1 + 4;

      for (var key:String in contents) {
        container.writeShort(key.length); // Length of key
        container.writeUTFBytes(key); // The key itself
        size += 2 + key.length;
        switch(contents[key]) {
        case contents[key] as Number:
          size += writeDouble(contents[key]);
          break;

        case contents[key] as String:
          size += writeString(contents[key]);
          break;

        default:
          Logger.log("Unknown type in ECMA array:" + typeof contents[key]);

          break;
        }
      }

      /* ECMA Array End */
      container.writeByte(0x00);
      container.writeByte(0x00);
      container.writeByte(0x09);
      size += 3;

      return size;
    }

    private function writeDouble(contents:Number):uint {
      container.writeByte(0x00); // Number type marker
      container.writeDouble(contents);
      return 1 + 8;
    }

    private function writeString(contents:String):uint {
      container.writeByte(0x02); // String type marker
      container.writeShort(contents.length); // Length of string
      container.writeUTFBytes(contents); // String
      return 1 + 2 + contents.length;
    }

    private function writeTimestamp(ts:Number):uint {
      container.writeUnsignedInt(((ts >>> 24) & 0xFF) | ((ts << 8) & 0xFFFFFF00));
      return 4;
    }
    private function writeStreamId():uint {
      container.writeByte(0x00); // StreamID - always 0
      container.writeByte(0x00); // StreamID - always 0
      container.writeByte(0x00); // StreamID - always 0
      return 3;
    }
    private function writeSize(sizePos:uint, dataSize:uint):void {
      container[sizePos + 0] = (dataSize >> 16 & 0xFF);
      container[sizePos + 1] = (dataSize >> 8  & 0xFF);
      container[sizePos + 2] = (dataSize >> 0  & 0xFF);
    }
    private function parseSPS(sps:BitArray):Object {
      var nalhdr:uint      = sps.readBits(8);

      var profile:uint     = sps.readBits(8);
      Logger.log('FLVMux: sps profile =', profile);

      var constraints:uint = sps.readBits(8);
      Logger.log('FLVMUX: sps constraints =', constraints);

      var level:uint       = sps.readBits(8);
      Logger.log('FLVMux: sps level =', level);

      var seq_parameter_set_id:uint = sps.readUnsignedExpGolomb();
      if (-1 !== [100, 110, 122, 244, 44, 83, 86, 118, 128, 138].indexOf(profile)) {
        /* Parse chroma/luma parameters */
        var chroma_format_idc:uint = sps.readUnsignedExpGolomb();
        if (3 === chroma_format_idc) {
          var separate_colour_plane_flag:uint = sps.readBits(1);
        }

        var bit_depth_luma_minus8:uint = sps.readUnsignedExpGolomb();
        var bit_depth_chroma_minus8:uint = sps.readUnsignedExpGolomb();
        var qpprime_y_zero_transform_bypass_flag:uint = sps.readBits(1);
        var seq_scaling_matrix_present_flag:uint = sps.readBits(1);

        if (seq_scaling_matrix_present_flag) {
          var i:uint = 0;
          var loopCount: uint = (3 === chroma_format_idc) ? 12 : 8;
          for (i = 0; i < loopCount; i++) {
            var seq_scaling_list_present_flag:uint = sps.readBits(1);
            if (seq_scaling_list_present_flag) {
              var sizeOfScalingList:uint = (i < 6) ? 16 : 64;
              var lastScale:uint = 8;
              var nextScale:uint = 8;
              var j:uint = 0;
              for (j = 0; j < sizeOfScalingList; j++) {
                if (nextScale != 0) {
                  var delta_scale:uint = sps.readSignedExpGolomb();
                  nextScale = (lastScale + delta_scale + 256) % 256;
                }
                lastScale = (nextScale == 0) ? lastScale : nextScale;
              }
            }
          }
        }
      }

      var log2_max_frame_num_minus4:uint = sps.readUnsignedExpGolomb();
      var pic_order_cnt_type:uint        = sps.readUnsignedExpGolomb();
      if (0 == pic_order_cnt_type) {
        var log2_max_pic_order_cnt_lsb_minus4:uint = sps.readUnsignedExpGolomb();
      } else if (1 == pic_order_cnt_type) {
        ErrorManager.dispatchError(823, null, true);
      }

      var max_num_ref_frames:uint                   = sps.readUnsignedExpGolomb();
      var gaps_in_frame_num_value_allowed_flag:uint = sps.readBits(1);
      var pic_width_in_mbs_minus1:uint              = sps.readUnsignedExpGolomb();
      var pic_height_in_map_units_minus1:uint       = sps.readUnsignedExpGolomb();
      var pic_frame_mbs_only_flag:uint              = sps.readBits(1);
      var direct_8x8_inference_flag:uint            = sps.readBits(1);
      var frame_cropping_flag:uint                  = sps.readBits(1);
      var frame_crop_left_offset:uint   = frame_cropping_flag ? sps.readUnsignedExpGolomb() : 0;
      var frame_crop_right_offset:uint  = frame_cropping_flag ? sps.readUnsignedExpGolomb() : 0;
      var frame_crop_top_offset:uint    = frame_cropping_flag ? sps.readUnsignedExpGolomb() : 0;
      var frame_crop_bottom_offset:uint = frame_cropping_flag ? sps.readUnsignedExpGolomb() : 0;

      var w:uint = (pic_width_in_mbs_minus1 + 1) * 16 -
        (frame_crop_left_offset * 2) - (frame_crop_right_offset * 2);
      var h:uint = (2 - pic_frame_mbs_only_flag) * (pic_height_in_map_units_minus1 + 1) * 16 -
        (frame_crop_top_offset * 2) - (frame_crop_bottom_offset * 2)
      return {
        'profile' : profile,
        'level'   : level / 10.0,
        'width'   : w,
        'height'  : h
      };
    }

    public function createMetaDataTag(params:Object):void {
      var size:uint = 0;

      /* FLV Tag */
      var sizePosition:uint = container.position + 1; // 'Size' is the 24 last byte of the next uint
	  //container.writeUnsignedInt(0x00000012 << 24 | (size & 0x00FFFFFF)); // Type << 24 | size & 0x00FFFFFF
      container.writeByte(0x12); // Tag type
      container.position += 3; // Leave 3bytes for UI24 dataSize
      size += 4;
      size += writeTimestamp(0);
      size += writeStreamId();

      /* Method call */
      size += writeString("onMetaData");

      /* Arguments */
      size += writeECMAArray({
        videocodecid    : 7.0, /* Only support AVC (H.264) */
        width           : params.width,
        height          : params.height,
        avcprofile      : params.profile,
        avclevel        : params.level,
        metadatacreator : "Locomote FLV Muxer",
        creationdate    : new Date().toString()
      });

      container.writeUnsignedInt(size); // Previous tag size

      /* Rewind and set the data size in tag header to actual size */
      var dataSize:uint = size - 11;

      writeSize(sizePosition, dataSize);
    }

    public function createDecoderConfigRecordTag(sps:ByteArray, pps:ByteArray, params:Object):void {
      var start:uint = container.position;

      /* FLV Tag */
      var sizePosition:uint = container.position + 1; // 'Size' is the 24 last byte of the next uint
	  //container.writeUnsignedInt(0x00000009 << 24 | (0x000000 & 0x00FFFFFF)); // Type << 24 | size & 0x00FFFFFF
      container.writeByte(0x9); // Tag type
      container.position += 3; // Leave 3bytes for UI24 dataSize
      writeTimestamp(0);
      writeStreamId();

      /* Video Tag Header */
      container.writeByte(0x01 << 4 | 0x07); // Keyframe << 4 | CodecID
      container.writeUnsignedInt(0x00 << 24 | 0x00000000); // AVC NALU << 24 | CompositionTime

      var profilelevelid:uint = parseInt(params.profile, 16);
      writeDecoderConfigurationRecord(profilelevelid);
      writeParameterSets(sps, pps);
      this.sps.clear();
      this.pps.clear();

      var size:uint = container.position - start;

      /* Rewind and set the data size in tag header to actual size */
      var dataSize:uint = size - 11;

      writeSize(sizePosition, dataSize);
      /* End of tag */
      container.writeUnsignedInt(size);
    }

    public function writeDecoderConfigurationRecord(profilelevelid:uint):void {
      container.writeByte(0x01); // Version
      container.writeByte((profilelevelid & 0x00FF0000) >> 16); // AVC Profile, Baseline
      container.writeByte((profilelevelid & 0x0000FF00) >> 8); // Profile compatibility
      container.writeByte((profilelevelid & 0x000000FF) >> 0); // Level indication
      container.writeByte(0xFF); // 111111xx (xx=lengthSizeMinusOne)
    }

    public function writeParameterSets(sps:ByteArray, pps:ByteArray):void {
      if (sps.bytesAvailable > 0) {
        /* There is one sps available */
        container.writeByte(0xE1); // 111xxxxx (xxxxx=numSequenceParameters), only support 1
        container.writeShort(sps.bytesAvailable); // Sequence parameter set 1 length
        container.writeBytes(sps, sps.position); // Actual parameters
      } else {
        /* No sps here */
        container.writeByte(0xE0); // 111xxxxx (xxxxx=numOfSequenceParameters), 0 sps here
      }

      if (pps.bytesAvailable > 0) {
        container.writeByte(0x01); // Num picture parameters, only support 1
        container.writeShort(pps.bytesAvailable); // Picture parameter length
        container.writeBytes(pps, pps.position); // Actual parameters
      } else {
        /* No pps here */
        container.writeByte(0x00); // numOfPictureParameterSets
      }
    }

    private function getAudioParameters():Object {
      var sdpMedia:Object = this.sdp.getMediaBlock('audio');
      var name:String = sdpMedia.rtpmap[sdpMedia.fmt[0]].name;
      switch (name.toLowerCase()) {
      case 'mpeg4-generic':
        return {
          format: 0xA, /* AAC */
          sampling: 0x3, /* Should alway be 0x3. Actual rate is determined by AAC header. */
          depth: 0x1, /* 16 bits per sample */
          type: 0x1, /* Stereo */
          duration: 1024 * 1000 / sdpMedia.rtpmap[sdpMedia.fmt[0]].clock /* An AAC frame contains 1024 samples */
        };
      case 'pcma':
        return {
          format: 0x7, /* Logarithmic G.711 A-law  */
          sampling: 0x0, /* Doesn't matter. Rate is fixed at 8 kHz when format = 0x7 */
          depth: 0x1, /* 16 bits per sample, but why? */
          type: 0x0, /* Mono */
          duration: 0 /* not implemented */
        };
      case 'pcmu':
        return {
          format: 0x8, /* Logarithmic G.711 mu-law  */
          sampling: 0x0, /* Doesn't matter. Rate is fixed at 8 kHz when format = 0x8 */
          depth: 0x1, /* 16 bits per sample */
          type: 0x0, /* Mono */
          duration: 0 /* not implemented */
        }; 
      default:
        /* No audio params for this name. */
        ErrorManager.dispatchError(831, [ name  ], true);
        
        return false;
      }
    }

    public function createAudioSpecificConfigTag(config:Object):void {
      var start:uint = container.position;

      /* FLV Tag */
      var sizePosition:uint = container.position + 1; // 'Size' is the 24 last byte of the next uint
      container.writeByte(0x8); // Tag type
      container.position += 3; // Leave 3bytes for UI24 dataSize
      writeTimestamp(0);
      writeStreamId();

      var audioParams:Object = getAudioParameters();

      /* Audio Tag Header */
      container.writeByte(audioParams.format << 4 | audioParams.sampling << 2 | audioParams.depth << 1 | audioParams.type << 0);

      if (0xA === audioParams.format) {
        /* A little more setup required if this is AAC */
        container.writeByte(0x0); // AAC Sequence Header
        container.writeBytes(ByteArrayUtils.createFromHexstring(config.fmtp['config']));
      }

      var size:uint = container.position - start;

      /* Rewind and set the data size in tag header to actual size */
      var dataSize:uint = size - 11;

      writeSize(sizePosition, dataSize);      

      /* End of tag */
      container.writeUnsignedInt(size);
    }

    private function createVideoTag(nalu:NALU):void {
      var start:uint = container.position;
      var ts:uint = nalu.timestamp;
      // Video and audio packets may arrive out of order. In that case set new
      // first timestamp.
      if (this.firstTimestamp === -1 || ts < this.firstTimestamp) {
        this.firstTimestamp = ts;
      }
      ts -= firstTimestamp;

      /* FLV Tag */
      var sizePosition:uint = container.position + 1; // 'Size' is the 24 last byte of the next uint
      container.writeByte(0x9); // Tag type
      container.position += 3; // Leave 3bytes for UI24 dataSize
      writeTimestamp(ts);
      writeStreamId();      

      /* Video Tag Header */
      container.writeByte((nalu.isIDR() ? 1 : 2) << 4 | 0x07); // Keyframe << 4 | CodecID
      container.writeUnsignedInt(0x01 << 24 | (0x0 & 0x00FFFFFF)); // AVC NALU << 24 | CompositionTime & 0x00FFFFFF

      /* Video Data */
      nalu.writeStream(container);

      var size:uint = container.position - start;

      /* Rewind and set the data size in tag header to actual size */
      var dataSize:uint = size - 11;

      writeSize(sizePosition, dataSize);

      /* Previous Tag Size */
      container.writeUnsignedInt(size);
      this.lastTimestamp = ts;

      createFLVTag(nalu.timestamp, 0, false);
    }

    public function createAudioTag(frame:*):void {
      var start:uint = container.position;
      var ts:uint = frame.timestamp;
       // Video and audio packets may arrive out of order. In that case set new
      // first timestamp.
      if (this.firstTimestamp === -1 || ts < this.firstTimestamp) {
        this.firstTimestamp = ts;
      }
      ts -= firstTimestamp;

      /* FLV Tag */
      var sizePosition:uint = container.position + 1; // 'Size' is the 24 last byte of the next uint
      container.writeByte(0x8); // Tag type
      container.position += 3; // Leave 3bytes for UI24 dataSize
      writeTimestamp(ts);
      writeStreamId();
      
      var audioParams:Object = getAudioParameters();

      /* Audio Tag Header */
      container.writeByte(audioParams.format << 4 | audioParams.sampling << 2 | audioParams.depth << 1 | audioParams.type << 0);

      var duration:Number = audioParams.duration;
      switch (audioParams.format) {
        case 0xA:
          /* A little more setup required if this is AAC */
          container.writeByte(0x1); // AAC Raw
          break;
        case 0x7:
        case 0x8:
          duration = frame.getPayload().bytesAvailable / 8;
          break;
        default:
          break;
      }

      /* Audio Data */
      frame.writeStream(container);

      var size:uint = container.position - start;

      /* Rewind and set the data size in tag header to actual size */
      var dataSize:uint = size - 11;

      writeSize(sizePosition, dataSize);      

      /* End of tag */
      container.writeUnsignedInt(size);
      this.lastTimestamp = ts;
    
      createFLVTag(frame.timestamp, duration, true);
    }

    public function getLastTimestamp():Number {
      return this.lastTimestamp;
    }

    public function onNALU(nalu:NALU):void {
      switch (nalu.ntype) {
      case 1: /* Coded slice of a non-IDR picture */
      case 2: /* Coded slice data partition A */
      case 3: /* Coded slice data partition B */
      case 4: /* Coded slice data partition C */
      case 5: /* Coded slice of an IDR picture */
        /* 1 - 5 are Video Coding Layer (VCL) unit type class (Rec. ITU-T H264 04/2013), and contains video data */
        createVideoTag(nalu);
        break;

      case 7: /* Sequence parameter set */
        this.sps = nalu.getPayload();
        createVideoSpecificConfigTag();
        break;

      case 8: /* Picture parameter set */
	  //ExternalInterface.call("console.log","nalu type 8"+nalu.ntype);
        this.pps = nalu.getPayload();
        createVideoSpecificConfigTag();
        break;

      default:
        /* Unknown NAL unit, skip it */
        /* Return here as nothing was created, and thus nothing should be appended */
        return;
      }
    }

    public function onAudio(frame:*):void {
      createAudioTag(frame);
    }

    private function createFLVTag(timestamp:uint, duration:uint, audio:Boolean):void {
      dispatchEvent(new FLVTag(container, timestamp, duration, audio));
      container.clear()
    }
  }
}