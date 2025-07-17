package com.heyi.player.core 
{
	import com.heyi.player.events.NetStatusEventCode;
	import com.heyi.player.events.NetStatusEventLevel;
	import com.heyi.player.interfaces.IMediaPlayer;
	import com.heyi.player.utils.ProxyNetClient;
	import com.tudou.utils.Debug;
	import com.tudou.utils.Global;
	import com.tudou.utils.Scheduler;
	import com.tudou.utils.Utils;
	import flash.display.BitmapData;
	import flash.display.Stage3D;
	import flash.display3D.Context3D;
	import flash.display3D.Context3DTextureFormat;
	import flash.events.VideoTextureEvent;
	import flash.geom.Rectangle;
	import flash.media.SoundTransform;
	import flash.utils.getTimer;
	import starling.core.Starling;
	import starling.display.Image;
	import starling.textures.ConcreteTexture;
	
	import flash.events.AsyncErrorEvent;
	import flash.events.IOErrorEvent;
	import flash.events.SecurityErrorEvent;
	import flash.events.StageVideoEvent;
	import flash.media.VideoStatus;
	import flash.display3D.textures.VideoTexture;
	import flash.net.NetConnection;
	import flash.net.NetStream;
	
	import starling.display.Sprite;
	import starling.events.Event;
	import starling.events.NetStatusEvent;
	import starling.display.DisplayObject;
	import starling.media.Video;
	
	/**
	 * 基于Starling的通用媒体播放核心
	 * 
	 * @author 8088
	 */
	public class StarlingMediaPlayer extends Sprite implements IMediaPlayer
	{
		private var nc:NetConnection;
		private var ns:NetStream;
		private var vi:Video;
		
		public function StarlingMediaPlayer() 
		{
			if (stage) onStage();
			else addEventListener(Event.ADDED_TO_STAGE, onStage);
			
			_client = new ProxyNetClient(this);
			_status = new MediaPlayStatus(this);
			
			
			vi = new Video();
			vi.addEventListener(StageVideoEvent.RENDER_STATE, onVideoEvent);
			
			
		}
		
		protected function onStage(evt:Event = null):void
		{
			removeEventListener(Event.ADDED_TO_STAGE, onStage);
			
			initialize();
		}
		
		protected function initialize():void
        {
			this.touchable = false;
			
			resize(stage.stageWidth, stage.stageHeight);
			//_stage.addEventListener(StageVideoStatusEvent.AVAILABLE, onStageVideoStatusEvent);
            //_stage.addEventListener(StageVideoStatusEvent.UNAVAILABLE, onStageVideoStatusEvent);
			
			/**
			 * 通知外部，播放核心初始化完毕
			 */
			 
			dispatchEvent( new NetStatusEvent
				( NetStatusEvent.NET_STATUS
				, false
				, false
				, { code:NetStatusEventCode.PLAYER_IS_READY, level:NetStatusEventLevel.STATUS, data:{id:this.id, version:"2015-11-06 20:54:34"} }
				)
			);
        }
		
		private function onRenderState(evt:VideoTextureEvent):void
		{
			trace("onRenderState", evt.status)
			_videoStatus = evt.status;
		}
		
		protected function creatNetStream():NetStream
        {
            return new NetStream(nc);
        }
		
		//API
		public function start():void 
		{
			setPlayerState(MediaPlayStatus.START);
			_first_buffer_full = true;
			//mark:如果有资源启动播放...
			if (source) openNetConnection(source.command);
		}
		
		public function play(...rest):void
		{
			if (rest[0]==undefined || rest[0] =="")
			{
				if (state == MediaPlayStatus.PLAYING) return;
				
				if (state == MediaPlayStatus.PAUSED)
				{
					resume();
					setPlayerState(MediaPlayStatus.PLAYING);
				}
				else if (state == MediaPlayStatus.START) {
					if (source) buffer(source.url);
				}
			}
			else if(typeof(rest[0]) == "string"&&String(rest[0]).length>10){
				buffer(rest[0]);
			}
			else if (typeof(rest[0]) == "object" && rest[0].url) {
				source = rest[0];
				
				start();
			}
		}
		
		public function replay():void
		{
			_first_buffer_full = true;
			// ignore..
		}
		
		public function pause():void 
		{
			if (ns) ns.pause();
			
			setPlayerState(MediaPlayStatus.PAUSED);
		}
		
		public function resume():void 
		{
			if (ns) ns.resume();
			
			setPlayerState(MediaPlayStatus.PLAYING);
		}
		
		public function seek(time:Number):void 
		{
			return;
		}
		
		public function stop():void 
		{
			disconnectStream();
			
            setPlayerState(MediaPlayStatus.NOT_START);
		}
		
		public function end():void 
		{
			//mark:直接跳到结尾处。
			//progressScheduler.stop();
			setPlayerState(MediaPlayStatus.PLAY_END);
		}
		
		public function destroy():void 
		{
			closeNetConnection();
			
			stop();
			
			//clear render
		}
		
		public function getLoadedFraction():Number 
		{
			return NaN;
		}
		
		public function getDefaultMediaSurface():DisplayObject 
		{
			return this;
		}
		
		public function resize(w:Number, h:Number):void 
		{
			_width = w;
			_height = h;
			
			resizeVideo(_width, _height);
		}
		
		public function resetStream(connect:Boolean = true):void 
		{
			connectStream();
		}
		
		public function unrecoverableError(err:String = null):void 
		{
			//..
		}
		
		public function isTagStreaming():Boolean 
		{
			return false;
		}
		
		public function isStageVideoAvailable():Boolean 
		{
			//return _stage.stageVideoAvailable;
			return true;
		}
		
		public function captureFrame():BitmapData
		{
			return null;
		}
		
		public function getDataLoadInfo():Object
		{
			var _info:Object = { };
			_info.tcp = {
				bytesLoaded: this.bytesLoaded,
				bytesTotal: this.bytesTotal
			};
			
			_info.udp = {
				bytesLoaded: 0,
				bytesTotal: 0,
				upstreams: 0,
				downstreams: 0
			};
			return _info;
		}
		
		public function getFPS():Number 
		{
			return ns?ns.currentFPS:0;
		}
		
		public function onMetaData(info:Object):void
		{
			info.bytesLoaded = this.bytesLoaded;
            info.bytesTotal = this.bytesTotal;
			
			if (ns)
            {
                if (info.width == undefined)
                {
                    info.width = vi.videoWidth;
                }
                if (info.height == undefined)
                {
                    info.height = vi.videoHeight;
                }
            }
			
			_metadata = info;
			
            if (info.width == 0 || info.height == 0)
            {
                if (!metaDataScheduler)
                {
                    metaDataScheduler = Scheduler.setInterval(0, onPollVideoForDimensions);
                }
            }
			else {
				
				if (isNaN(proportion) && info.width && info.height) proportion = info.width / info.height;
				
				//_global.info.applyMetaData(info);
				
				dispatchEvent( new NetStatusEvent
						( NetStatusEvent.NET_STATUS
						, false
						, false
						, { code:NetStatusEventCode.PLAYER_GET_META_DATA, level:NetStatusEventLevel.STATUS, data:{metadata:_metadata, id:this.id} }
						)
					);
			}
        }
		
        private function onCuePoint(info:Object):void
		{
            log("onCuePoint: " + Utils.serialize(info));
        }
		
		public function onPlayStatus(info:Object):void
		{
			log("onPlayStatus: " + Utils.serialize(info));
		}
		
		//
		public function get id():String
		{
			return _id;
		}
		
		public function set id(value:String):void
		{
			id = value;
		}
		
		public function get source():Object 
		{
			return _source;
		}
		
		public function set source(value:Object):void 
		{
			_source = value;
			
			if (_source == null) stop();
		}
		
		public function get volume():Number 
		{
			return _volume;
		}
		
		public function set volume(value:Number):void 
		{
			_volume = value;
			
			if (!isNaN(value) && ns)
			{
				_volume = volume;
				ns.soundTransform = new SoundTransform(_volume);
			}
			
		}
		
		public function get time():Number
		{
			var _time:Number = 0;
			
			if (ns && ns.time > 0)
			{
				_time = ns.time + timeOffset;
			}
			
			if (_time == Infinity)
            {
                _time = 0;
            }
			return _time;
		}
		
		public function get timeOffset():Number
		{
			return _timeOffset;
		}
		
		public function set timeOffset(value:Number):void
		{
			_timeOffset = value;
		}
		
		public function get duration():Number
		{
			return _duration;
		}
		
		public function get bytesLoaded():Number
		{
			var _bytes:Number = 0;
			if (ns)
			{
				_bytes = ns.bytesLoaded;
				if (_bytes == uint( -1))
				{
					_bytes = 0;
				}
			}
			return _bytes;
		}
		
		public function get bytesTotal():Number
		{
			var _bytes:Number = 0;
            if (ns)
            {
                _bytes = ns.bytesTotal;
                if (_bytes == uint(-1))
                {
                    _bytes = 0;
                }
            }
            return _bytes;
		}
		
		public function get status():MediaPlayStatus
		{
			return _status;
		}
		
		public function get state():String
		{
			return _status?_status.state:MediaPlayStatus.NOT_START;
		}
		
		public function get quality():String 
		{
			return null;
		}
		
		public function set quality(value:String):void
		{
			return;
		}
		
		public function get multiQuality():Array
		{
			return null;
		}
		
		public function get language():String 
		{
			return null;
		}
		
		public function set language(value:String):void
		{
			return;
		}
		
		public function get multiLanguage():Array
		{
			return null;
		}
		
		public function get stream():NetStream 
		{
			return ns;
		}
		
		public function get decoding():String
		{
			return _videoStatus;
		}
		
		public function get rendering():String
		{
			return _videoStatus==VideoStatus.ACCELERATED?VideoStatus.ACCELERATED:VideoStatus.SOFTWARE;
		}
		
		public function get proportion():Number
		{
			return _proportion;
		}
		
		public function set proportion(value:Number):void
		{
			_proportion = value;
			
			resizeVideo(_width, _height);
		}
		
		public function get metadata():Object
		{
			return _metadata;
		}
		
		public function get hardwareAccelerate():Boolean
		{
			return _hardwareAccelerate;
		}
		public function set hardwareAccelerate(value:Boolean):void
		{
			if (_hardwareAccelerate == value) return;
			
			_hardwareAccelerate = value;
			
		}
		
		
		
		// Internals..
		//
		
		private function openNetConnection(command:String=null):void
		{
			closeNetConnection();
			
			nc = new NetConnection();
			nc.client = this._client;
			nc.addEventListener(NetStatusEvent.NET_STATUS, onNetStatus);
			nc.addEventListener(SecurityErrorEvent.SECURITY_ERROR, onError);
			nc.addEventListener(AsyncErrorEvent.ASYNC_ERROR, onError);
			nc.addEventListener(IOErrorEvent.IO_ERROR, onError);
			try {
				nc.connect(command);
			}
			catch (err:Error) {
				log(err.message);
			}
		}
		
		private function closeNetConnection():void
        {
            if (nc)
            {
                nc.removeEventListener(NetStatusEvent.NET_STATUS, onNetStatus);
                nc.removeEventListener(SecurityErrorEvent.SECURITY_ERROR, onError);
                nc.removeEventListener(AsyncErrorEvent.ASYNC_ERROR, onError);
                nc.removeEventListener(IOErrorEvent.IO_ERROR, onError);
                nc.close();
                nc.client = {};
            }
        }
		
		//处理NC状态
		private function onNetStatus(evt:flash.events.NetStatusEvent):void
		{
			evt.info.data = { id:this.id };
			log(Utils.serialize(evt.info));
			switch(evt.info.code)
			{
				case "NetConnection.Connect.Success":
					connectStream();
					break;
				case "NetConnection.Connect.Rejected":
					dispatchError("1000");
					break;
				case "NetConnection.Connect.Closed":
					dispatchError("1001");
					break;
			}
        }
		
		private function connectStream():void
        {
            disconnectStream();
			
            ns = creatNetStream();
            ns.addEventListener(NetStatusEvent.NET_STATUS, onNetStreamStatus);
            ns.addEventListener(AsyncErrorEvent.ASYNC_ERROR, onError);
            ns.addEventListener(SecurityErrorEvent.SECURITY_ERROR, onError);
            ns.addEventListener(IOErrorEvent.IO_ERROR, onError);
            if (source) ns.bufferTime = source.bufferTime;
            ns.checkPolicyFile = true;
			ns.client = this._client;
            if (!isNaN(volume))
            {
                var v:Number = volume;
                ns.soundTransform = new SoundTransform(v);
            }
            attachNetStream(true);
        }
		
		private function disconnectStream():void
        {
            if (ns)
            {
                ns.soundTransform.volume = 0;
                ns.removeEventListener(NetStatusEvent.NET_STATUS, onNetStreamStatus);
                ns.removeEventListener(AsyncErrorEvent.ASYNC_ERROR, onError);
                ns.removeEventListener(IOErrorEvent.IO_ERROR, onError);
                ns.removeEventListener(SecurityErrorEvent.SECURITY_ERROR, onError);
                ns.close();
                if (ns.hasOwnProperty("dispose"))
                {
                    Object(ns).dispose();
                }
                ns.client = {};
                ns = null;
            }
            if (metaDataScheduler && metaDataScheduler.isRunning())
            {
                metaDataScheduler.stop();
            }
        }
		
		/**
		 * 处理NS状态
		 * 
		 * @param	evt
		 */
		private function onNetStreamStatus(evt:flash.events.NetStatusEvent):void
		{
			switch(evt.info.code)
			{
				case "NetStream.Play.Start":
					break;
				case "NetStream.Play.StreamNotFound":
                case "NetStream.Play.FileStructureInvalid":
                case "NetStream.Play.NoSupportedTrackFound":
                    dispatchError("2000");
					break;
				case "NetStream.Play.Complete":
					/*onProgress();*/
                    end();
					break;
				case "NetStream.Play.Stop":
                    
					break;
				case "NetStream.Buffer.Full":
					if (status.state == MediaPlayStatus.PAUSED || status.state == MediaPlayStatus.PAUSED_BUFFERING)
					{
						if(ns) ns.pause();
					}
					dispatchBufferFullEvent();
					break;
				case "NetStream.Buffer.Empty":
					if (isValidBufferEmpty()) dispatchBufferEmptyEvent();
					break;
				case "NetStream.Pause.Notify":
					
					break;
                case "NetStream.SeekStart.Notify":
					
					break;
				case "NetStream.Seek.Notify":
					//mark: seek成功...
					break;
				case "NetStream.Seek.InvalidTime":
					//mark:重新找合适的点seek
					break;
				//..
			}
			evt.info.data = { id:this.id };
			
			if (_status) _status.onNetStatus(evt);
		}
		
		//mark:从播放点重新缓冲
		private function buffer(url:String):void
		{
			if (ns)
			{
				var play_time:Number = this.time;
				ns.close();
                if (ns.hasOwnProperty("dispose")) Object(ns).dispose();
				
				setPlayerState(MediaPlayStatus.BUFFERING);
				ns.play(url+"?begin="+play_time);
			}
		}
		
		private function dispatchBufferFullEvent():void
		{
			if (_first_buffer_full)
			{
				dispatchEvent( new NetStatusEvent
					( NetStatusEvent.NET_STATUS
					, false
					, false
					, { code:NetStatusEventCode.PLAYER_PLAY_START, level:NetStatusEventLevel.STATUS, data:{id:this.id} }
					)
				);
				
				_first_buffer_full = false;
			}
			else {
				dispatchEvent( new NetStatusEvent
					( NetStatusEvent.NET_STATUS
					, false
					, false
					, { code:NetStatusEventCode.PLAYER_BUFFER_FULL, level:NetStatusEventLevel.STATUS, data:{id:this.id} }
					)
				);
			}
		}
		
		private function dispatchBufferEmptyEvent():void
		{
			dispatchEvent( new NetStatusEvent
				( NetStatusEvent.NET_STATUS
				, false
				, false
				, { code:NetStatusEventCode.PLAYER_BUFFER_EMPTY, level:NetStatusEventLevel.STATUS, data:{id:this.id} }
				)
			);
		}
		
		private function attachNetStream(b:Boolean = false):void
        {
			/*var sva:Boolean = isStageVideoAvailable();
            
            if (!b && (sva == Boolean(sv) || hardwareAccelerate==false)) return;
			if (sva&&hardwareAccelerate)
            {
                if (vi&&contains(vi))
                {
					vi.clear();
                    removeChild(vi);
                }
                if (sv == null)
                {
                    sv = _stage.stageVideos[0];
                    sv.addEventListener(StageVideoEvent.RENDER_STATE, onStageVideoEvent);
                }
				
				videoRenderStatus = null;
                stageVideoRenderStatus = null;
                sv.attachNetStream(ns);
                if (state == MediaPlayStatus.PLAYING)
                {
                    stageVideoTimeout.restart();
                }
				
            }
            else {
                if (sv)
                {
                    sv.removeEventListener(StageVideoEvent.RENDER_STATE, onStageVideoEvent);
                }
                sv = null;
				videoRenderStatus = null;
                stageVideoRenderStatus = null;
                stageVideoTimeout.stop();
                vi.attachNetStream(ns);
				addChild(vi);
            }
			*/
			
			vi.attachNetStream(ns);
			addChild(vi);
			
			if (source) buffer(source.url);
			//
			
            resizeVideo(_width, _height);
        }
		
		private function onPollVideoForDimensions(evt:Event):void
        {
            if (vi.videoWidth > 0)
            {
				//mark:如果原数据中没有，就从渲染器中读取补充。
                if (_metadata) {
					if (_metadata.width == undefined) _metadata.width = vi.videoWidth;
					if (_metadata.height == undefined) _metadata.height = vi.videoHeight;
				}
				
				if (isNaN(proportion)) proportion = vi.videoWidth / vi.videoHeight;
				
                metaDataScheduler.stop();
				
				dispatchEvent( new NetStatusEvent
						( NetStatusEvent.NET_STATUS
						, false
						, false
						, { code:NetStatusEventCode.PLAYER_GET_META_DATA, level:NetStatusEventLevel.STATUS, data:{metadata:{width:vi.videoWidth, height:vi.videoHeight}, id:this.id} }
						)
					);
            }
        }
		
		private function resizeVideo(w:Number, h:Number):void
		{
			var rec:Rectangle = new Rectangle(0, 0, w, h);
			var pw:Number = w;
			var ph:Number = h;
			var _p:Number = 16 / 9 ; //default aspect ratio for mobile
			if (!isNaN(_proportion)) _p = _proportion;
			
			if (_p < pw / ph)
			{
				rec.width = pw;
				rec.height = int(pw / _p);
            }
			else {
				rec.height = ph;
				rec.width = int(ph * _p);
            }
			
			rec.x = (pw - rec.width) * .5;
			rec.y = (ph - rec.height) * .5;
			
            if (vi)
            {
				vi.width = rec.width;
				vi.height = rec.height;
				vi.x = rec.x;
				vi.y = rec.y;
                //vi.smoothing = vi.width != vi.videoWidth || vi.height != vi.videoHeight;
            }
		}
		
        private function isValidBufferEmpty():Boolean
        {
            var min:Number = 1;
            if (status.state != MediaPlayStatus.PLAYING) return false;
            if ((getTimer() - this.lastTimeEnteringPlayingState) / 1000 < min) return false;
            if (this.duration > 0 && this.duration - this.time < min) return false;
            return true;
        }
		
		private function onError(evt:Event):void
        {
			disconnectStream();
			
            setPlayerState(MediaPlayStatus.ERROR);
        }
		
		private function onVideoEvent(evt:Event):void
        {
			log("onVideoEvent:" + evt);
            _videoStatus = Object(evt).status;
			attachNetStream();
        }
		
		private function onStageVideoEvent(evt:Event):void
        {
			log("onStageVideoEvent:" + evt);
            _videoStatus = Object(evt).status;
			attachNetStream();
        }
		
		/**
		 * 播放错误：
		 * 1000:服务器拒绝连接
		 * 1001:服务器连接关闭，无法链接
		 * 2000:播放流失败
		 * @param	code为错误码, desc为错误描述
		 */
		private function dispatchError(code:String, desc:String=null):void
		{
			var error_code:String = "E" + code;
			var error_desc:String = desc || "对不起，该视频暂时无法播放，\n请刷新页面重试。";
			
			dispatchEvent(new NetStatusEvent
				( NetStatusEvent.NET_STATUS
				, false
				, false
				, 	{ code:NetStatusEventCode.PLAYER_PLAY_FAILED
					, level:NetStatusEventLevel.ERROR
					, data: { code:error_code, desc:error_desc, id:this.id }
					}
				)
			);
		}
		
		private function setPlayerState(value:String):void
        {
			if (status && status.state != value)
			{
				status.state = value;
				
				if (status.state == MediaPlayStatus.PLAYING)
				{
					lastTimeEnteringPlayingState = getTimer();
				}
				//mark:在此统一修改，因状态而衍生的周边属性、方法控制
				//...
			}
        }
		
		internal function log(...args):void
		{
			Debug.log(args, 0x33B5E5, "SMP");
		}
		
		private var _global:Global = Global.getInstance();
		
		private var _id:String = "StarlingMediaPlayer";
		
		private var _stage:MediaPlayStatus;
		private var _status:MediaPlayStatus;
		private var _width:Number = 0;
		private var _height:Number = 0;
		private var _volume:Number = 1;
		private var _duration:Number;
		private var _timeOffset:Number = 0;
		
		private var _source:Object;
		private var _client:ProxyNetClient;
		private var _metadata:Object;
		private var _videoStatus:String;
		
		private var _first_buffer_full:Boolean = true;
		
		private var _rotation:Number = 0.0;
		private var _scale:Number = 1.0;
		private var _proportion:Number;
		private var _hardwareAccelerate:Boolean;
		
		private var progressScheduler:Scheduler;
		private var metaDataScheduler:Scheduler;
		private var lastTimeEnteringPlayingState:Number;
		private static const PROGRESS_INTERVAL:Number = 150;
		
	}

}