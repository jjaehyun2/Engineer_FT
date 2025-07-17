package flash.sensors
{
    import flash.events.*;

    public class Accelerometer extends EventDispatcher
    {

        public function Accelerometer()
        {
            return;
        }// end function

        public function setRequestedUpdateInterval(param1:Number) : void;

        public function get muted() : Boolean;

        public static function get isSupported() : Boolean;

    }
}