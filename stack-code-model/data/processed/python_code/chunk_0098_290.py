package flash.media
{
    import flash.events.*;

    final public class Microphone extends EventDispatcher
    {

        public function Microphone()
        {
            return;
        }// end function

        public function set gain(param1:Number) : void;

        public function set rate(param1:int) : void;

        public function get rate() : int;

        public function set codec(param1:String) : void;

        public function get codec() : String;

        public function get framesPerPacket() : int;

        public function set framesPerPacket(param1:int) : void;

        public function get encodeQuality() : int;

        public function set encodeQuality(param1:int) : void;

        public function get noiseSuppressionLevel() : int;

        public function set noiseSuppressionLevel(param1:int) : void;

        public function get enableVAD() : Boolean;

        public function set enableVAD(param1:Boolean) : void;

        public function setSilenceLevel(param1:Number, param2:int = -1) : void;

        public function setUseEchoSuppression(param1:Boolean) : void;

        public function get activityLevel() : Number;

        public function get gain() : Number;

        public function get index() : int;

        public function get muted() : Boolean;

        public function get name() : String;

        public function get silenceLevel() : Number;

        public function get silenceTimeout() : int;

        public function get useEchoSuppression() : Boolean;

        public function setLoopBack(param1:Boolean = true) : void;

        public function get soundTransform() : SoundTransform;

        public function set soundTransform(param1:SoundTransform) : void;

        public function get enhancedOptions() : MicrophoneEnhancedOptions;

        public function set enhancedOptions(param1:MicrophoneEnhancedOptions) : void;

        public static function getMicrophone(param1:int = -1) : Microphone;

        public static function get names() : Array;

        public static function get isSupported() : Boolean;

        public static function getEnhancedMicrophone(param1:int = -1) : Microphone;

    }
}