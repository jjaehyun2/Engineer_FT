package flash.ui
{
    import flash.events.*;

    dynamic public class GameInputControl extends EventDispatcher
    {

        public function GameInputControl()
        {
            return;
        }// end function

        public function get value() : Number;

        public function get minValue() : Number;

        public function get maxValue() : Number;

        public function get device() : GameInputDevice;

        public function get id() : String;

    }
}