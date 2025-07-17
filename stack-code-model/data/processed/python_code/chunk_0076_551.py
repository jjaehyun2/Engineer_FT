package flash.net
{
    import flash.events.*;
    import flash.media.*;
    import flash.utils.*;

    public class NetStream extends EventDispatcher
    {
        private static const kClose:uint = 0;
        private static const kAttachAudio:uint = 1;
        private static const kAttachVideo:uint = 2;
        private static const kSend:uint = 3;
        private static const kSetBufferTime:uint = 4;
        private static const kCall:uint = 202;
        private static const kGetTime:uint = 300;
        private static const kGetCurrentFps:uint = 301;
        private static const kGetBufferTime:uint = 302;
        private static const kGetBufferLength:uint = 303;
        private static const kGetLiveDelay:uint = 304;
        private static const kGetBytesLoaded:uint = 305;
        private static const kGetBytesTotal:uint = 306;
        private static const kGetTotalFrames:uint = 307;
        private static const kSetTotalFrames:uint = 308;
        private static const kGetVideoCodecID:uint = 311;
        private static const kSetVideoCodecID:uint = 312;
        private static const kGetAudioCodecID:uint = 313;
        private static const kSetAudioCodecID:uint = 314;
        private static const kGetFarID:uint = 340;
        private static const kGetNearNonce:uint = 341;
        private static const kGetFarNonce:uint = 342;
        private static const kGetInfo:uint = 343;
        private static const kGetMulticastInfo:uint = 344;
        private static const kAttach:uint = 345;
        private static const kGetMaxPauseBufferTime:uint = 400;
        private static const kSetMaxPauseBufferTime:uint = 401;
        private static const kGetBufferTimeMax:uint = 410;
        private static const kSetBufferTimeMax:uint = 411;
        private static const kGetBackBufferTime:uint = 450;
        private static const kSetBackBufferTime:uint = 451;
        private static const kGetBackBufferLength:uint = 452;
        private static const kStep:uint = 453;
        private static const kGetInBufferSeek:uint = 454;
        private static const kSetInBufferSeek:uint = 455;
        public static const DIRECT_CONNECTIONS:String = "directConnections";
        public static const CONNECT_TO_FMS:String = "connectToFMS";

        public function NetStream(param1:NetConnection, param2:String = "connectToFMS")
        {
            this.ctor(param1, param2);
            if (param2 == CONNECT_TO_FMS)
            {
                param1.call("createStream", new Responder(this.onResult, this.onStatus));
            }
            return;
        }// end function

        private function ctor(param1:NetConnection, param2:String) : void;

        private function onResult(param1:int) : void;

        private function onStatus(param1) : void
        {
            dispatchEvent(new NetStatusEvent("status", false, false, param1));
            return;
        }// end function

        public function dispose() : void;

        public function attach(param1:NetConnection) : void
        {
            this.invoke(kAttach, this, param1);
            param1.call("createStream", new Responder(this.onResult, this.onStatus));
            return;
        }// end function

        public function close() : void
        {
            this.invoke(kClose);
            return;
        }// end function

        public function attachAudio(param1:Microphone) : void
        {
            this.invoke(kAttachAudio, param1);
            return;
        }// end function

        public function attachCamera(param1:Camera, param2:int = -1) : void
        {
            this.invoke(kAttachVideo, param1, param2);
            return;
        }// end function

        public function send(param1:String, ... args) : void
        {
            args.unshift(param1);
            this.invokeWithArgsArray(kSend, args);
            return;
        }// end function

        public function get bufferTime() : Number
        {
            return this.invoke(kGetBufferTime);
        }// end function

        public function set bufferTime(param1:Number) : void
        {
            this.invoke(kSetBufferTime, param1);
            return;
        }// end function

        public function get maxPauseBufferTime() : Number
        {
            return this.invoke(kGetMaxPauseBufferTime);
        }// end function

        public function set maxPauseBufferTime(param1:Number) : void
        {
            this.invoke(kSetMaxPauseBufferTime, param1);
            return;
        }// end function

        public function get backBufferTime() : Number
        {
            return this.invoke(kGetBackBufferTime);
        }// end function

        public function set backBufferTime(param1:Number) : void
        {
            this.invoke(kSetBackBufferTime, param1);
            return;
        }// end function

        public function get inBufferSeek() : Boolean
        {
            return this.invoke(kGetInBufferSeek);
        }// end function

        public function set inBufferSeek(param1:Boolean) : void
        {
            this.invoke(kSetInBufferSeek, param1);
            return;
        }// end function

        public function get backBufferLength() : Number
        {
            return this.invoke(kGetBackBufferLength);
        }// end function

        public function step(param1:int) : void
        {
            this.invoke(kStep, this, "step", null, param1);
            return;
        }// end function

        private function call(param1:NetStream, param2:String, param3:Responder, ... args) : void
        {
            args.unshift(param1, param2, param3);
            this.invokeWithArgsArray(kCall, args);
            return;
        }// end function

        public function get bufferTimeMax() : Number
        {
            return this.invoke(kGetBufferTimeMax);
        }// end function

        public function set bufferTimeMax(param1:Number) : void
        {
            this.invoke(kSetBufferTimeMax, param1);
            return;
        }// end function

        public function receiveAudio(param1:Boolean) : void
        {
            this.call(this, "receiveAudio", null, param1);
            return;
        }// end function

        public function receiveVideo(param1:Boolean) : void
        {
            this.call(this, "receiveVideo", null, param1);
            return;
        }// end function

        public function receiveVideoFPS(param1:Number) : void
        {
            this.call(this, "receiveVideo", null, param1);
            return;
        }// end function

        public function pause() : void
        {
            this.call(this, "pause", null, true, this.time * 1000);
            return;
        }// end function

        public function resume() : void
        {
            this.call(this, "pause", null, false, this.time * 1000);
            return;
        }// end function

        public function togglePause() : void
        {
            this.call(this, "pause", null, undefined, this.time * 1000);
            return;
        }// end function

        public function seek(param1:Number) : void
        {
            this.call(this, "seek", null, param1 * 1000);
            return;
        }// end function

        public function play(... args) : void;

        public function play2(param1:NetStreamPlayOptions) : void;

        public function get info() : NetStreamInfo;

        public function get multicastInfo() : NetStreamMulticastInfo;

        public function publish(param1:String = null, param2:String = null) : void
        {
            if (param2)
            {
                this.call(this, "publish", null, param1, param2);
            }
            else
            {
                this.call(this, "publish", null, param1);
            }
            return;
        }// end function

        private function invoke(param1:uint, ... args);

        private function invokeWithArgsArray(param1:uint, param2:Array);

        public function get time() : Number
        {
            return this.invoke(kGetTime);
        }// end function

        public function get currentFPS() : Number
        {
            return this.invoke(kGetCurrentFps);
        }// end function

        public function get bufferLength() : Number
        {
            return this.invoke(kGetBufferLength);
        }// end function

        public function get liveDelay() : Number
        {
            return this.invoke(kGetLiveDelay);
        }// end function

        public function get bytesLoaded() : uint
        {
            return this.invoke(kGetBytesLoaded);
        }// end function

        public function get bytesTotal() : uint
        {
            return this.invoke(kGetBytesTotal);
        }// end function

        public function get decodedFrames() : uint
        {
            return this.invoke(kGetTotalFrames);
        }// end function

        public function get videoCodec() : uint
        {
            return this.invoke(kGetVideoCodecID);
        }// end function

        public function get audioCodec() : uint
        {
            return this.invoke(kGetAudioCodecID);
        }// end function

        public function get soundTransform() : SoundTransform;

        public function set soundTransform(param1:SoundTransform) : void;

        public function get checkPolicyFile() : Boolean;

        public function set checkPolicyFile(param1:Boolean) : void;

        public function get client() : Object;

        public function set client(param1:Object) : void;

        public function get objectEncoding() : uint;

        public function get multicastPushNeighborLimit() : Number;

        public function set multicastPushNeighborLimit(param1:Number) : void;

        public function get multicastWindowDuration() : Number;

        public function set multicastWindowDuration(param1:Number) : void;

        public function get multicastRelayMarginDuration() : Number;

        public function set multicastRelayMarginDuration(param1:Number) : void;

        public function get multicastAvailabilityUpdatePeriod() : Number;

        public function set multicastAvailabilityUpdatePeriod(param1:Number) : void;

        public function get multicastFetchPeriod() : Number;

        public function set multicastFetchPeriod(param1:Number) : void;

        public function get multicastAvailabilitySendToAll() : Boolean;

        public function set multicastAvailabilitySendToAll(param1:Boolean) : void;

        public function get farID() : String;

        public function get nearNonce() : String;

        public function get farNonce() : String;

        public function get peerStreams() : Array;

        public function onPeerConnect(param1:NetStream) : Boolean
        {
            return true;
        }// end function

        public function get audioReliable() : Boolean;

        public function set audioReliable(param1:Boolean) : void;

        public function get videoReliable() : Boolean;

        public function set videoReliable(param1:Boolean) : void;

        public function get dataReliable() : Boolean;

        public function set dataReliable(param1:Boolean) : void;

        public function get audioSampleAccess() : Boolean;

        public function set audioSampleAccess(param1:Boolean) : void;

        public function get videoSampleAccess() : Boolean;

        public function set videoSampleAccess(param1:Boolean) : void;

        public function appendBytes(param1:ByteArray) : void;

        public function appendBytesAction(param1:String) : void;

        public function get useHardwareDecoder() : Boolean;

        public function set useHardwareDecoder(param1:Boolean) : void;

        public function get useJitterBuffer() : Boolean;

        public function set useJitterBuffer(param1:Boolean) : void;

        public function get videoStreamSettings() : VideoStreamSettings;

        public function set videoStreamSettings(param1:VideoStreamSettings) : void;

        private static function createOnPlayStatusCompleteObject() : Object
        {
            var _loc_1:* = new Object();
            _loc_1["level"] = "status";
            _loc_1["code"] = "NetStream.Play.Complete";
            return _loc_1;
        }// end function

        public static function resetDRMVouchers() : void;

    }
}