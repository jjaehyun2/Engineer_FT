package flash.ui
{
    import flash.events.*;

    final public class GameInput extends EventDispatcher
    {

        public function GameInput()
        {
            return;
        }// end function

        public static function getDeviceAt(param1:int) : GameInputDevice;

        public static function get numDevices() : int;

        public static function get isSupported() : Boolean;

    }
}