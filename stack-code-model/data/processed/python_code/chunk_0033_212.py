package flash.events
{

    public class PressAndTapGestureEvent extends GestureEvent
    {
        public static const GESTURE_PRESS_AND_TAP:String = "gesturePressAndTap";

        public function PressAndTapGestureEvent(param1:String, param2:Boolean = true, param3:Boolean = false, param4:String = null, param5:Number = 0, param6:Number = 0, param7:Number = 0, param8:Number = 0, param9:Boolean = false, param10:Boolean = false, param11:Boolean = false)
        {
            super(param1, param2, param3, param4, param5, param6, param9, param10, param11);
            this.tapLocalX = param7;
            this.tapLocalY = param8;
            return;
        }// end function

        override public function clone() : Event
        {
            return new PressAndTapGestureEvent(type, bubbles, cancelable, phase, localX, localY, this.tapLocalX, this.tapLocalY, ctrlKey, altKey, shiftKey);
        }// end function

        override public function toString() : String
        {
            return formatToString("PressAndTapGestureEvent", "type", "bubbles", "cancelable", "phase", "args", "localX", "localY", "tapLocalX", "tapLocalY", "ctrlKey", "altKey", "shiftKey");
        }// end function

        public function get tapLocalX() : Number;

        public function set tapLocalX(param1:Number) : void;

        public function get tapLocalY() : Number;

        public function set tapLocalY(param1:Number) : void;

        public function get tapStageX() : Number
        {
            if (!isNaN(this.tapLocalX))
            {
                isNaN(this.tapLocalX);
            }
            if (isNaN(this.tapLocalY))
            {
                return Number.NaN;
            }
            return this.getTapStageX();
        }// end function

        public function get tapStageY() : Number
        {
            if (!isNaN(this.tapLocalX))
            {
                isNaN(this.tapLocalX);
            }
            if (isNaN(this.tapLocalY))
            {
                return Number.NaN;
            }
            return this.getTapStageY();
        }// end function

        private function getTapStageX() : Number;

        private function getTapStageY() : Number;

    }
}