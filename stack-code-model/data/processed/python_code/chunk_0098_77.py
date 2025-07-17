package flash.media
{

    public class AVSegmentedSource extends AVSource
    {
        public static const HLS:String = "HLS";
        public static const DASH:String = "DASH";
        public static const AUDIO:String = "audio";
        public static const AUDIO_PID:String = "audiopid";
        public static const AUDIO_DESCRIPTION:String = "audiodescription";
        public static const AUDIO_LANGUAGE:String = "audiolanguage";
        public static const VIDEO:String = "video";
        public static const VIDEO_DESCRIPTION:String = "videodescription";
        public static const DATA:String = "data";
        public static const DATA_DESCRIPTION:String = "datadescription";

        public function AVSegmentedSource()
        {
            this.ctor();
            return;
        }// end function

        private function ctor() : void;

        public function load(param1:String, param2:String = "HLS", param3:int = 0) : AVResult;

        public function loadWithBackgroundManifest(param1:String, param2:String, param3:int, param4:String) : AVResult;

        public function loadManifest(param1:String, param2:int = 0, param3:String = "HLS") : AVResult;

        public function releaseManifest(param1:int) : AVResult;

        public function setHoldAt(param1:Number) : AVResult;

        public function insertByVirtualTime(param1:Number, param2:int, param3:int = 0, param4:Number = 0) : AVInsertionResult;

        public function insertByLocalTime(param1:int, param2:Number, param3:int, param4:int = 0, param5:Number = 0) : AVInsertionResult;

        public function removeByVirtualTime(param1:Number, param2:Number) : AVResult;

        public function removeByLocalTime(param1:int, param2:Number, param3:Number, param4:Boolean) : AVResult;

        public function getTimeline() : AVTimeline;

        public function getBackgroundTimeline() : AVTimeline;

        public function selectTrack(param1:int, param2:String, param3:int) : AVResult;

        public function selectTrackString(param1:int, param2:String, param3:String) : AVResult;

        public function getPeriodInfo(param1:int) : AVPeriodInfo;

        public function getBackgroundPeriodInfo(param1:int) : AVPeriodInfo;

        public function getTrackCount(param1:int, param2:String) : int;

        public function getTrackInfo(param1:int, param2:String, param3:int) : AVTrackInfo;

        public function setABRParameters(param1:AVABRParameters) : AVResult;

        public function getABRProfileCount(param1:int) : int;

        public function getABRProfileInfoAtIndex(param1:int, param2:int) : AVABRProfileInfo;

        public function getCuePoint(param1:int, param2:int) : AVCuePoint;

        public function setCuePointTags(param1:Array) : AVResult;

        public function getSubscribedTag(param1:int, param2:int) : AVTagData;

        public function getSubscribedTagForBackgroundManifest(param1:int, param2:int) : AVTagData;

        public function setSubscribedTags(param1:Array) : AVResult;

        public function setSubscribedTagsForBackgroundManifest(param1:Array) : AVResult;

        public function setBandwidth(param1:int) : AVResult;

        public function getPerceivedBandwidth() : uint;

        public function setPauseAtPeriodEnd(param1:int, param2:int = 0) : AVResult;

        public function clearPauseAtPeriodEnd(param1:int) : AVResult;

        public function set useRedirectedUrl(param1:Boolean) : void;

        public function set networkingParams(param1:AVNetworkingParams) : void;

        public function get networkingParams() : AVNetworkingParams;

        public function set cookieHeader(param1:String) : void;

        public function set masterUpdateInterval(param1:int) : void;

    }
}