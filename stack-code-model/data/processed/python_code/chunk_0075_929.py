package flash.events
{

    public class KeyboardEvent extends Event
    {
        private var m_keyLocation:uint;
        private var m_keyCode:uint;
        public static const KEY_DOWN:String = "keyDown";
        public static const KEY_UP:String = "keyUp";

        public function KeyboardEvent(param1:String, param2:Boolean = true, param3:Boolean = false, param4:uint = 0, param5:uint = 0, param6:uint = 0, param7:Boolean = false, param8:Boolean = false, param9:Boolean = false)
        {
            super(param1, param2, param3);
            this.charCode = param4;
            this.keyCode = param5;
            this.keyLocation = param6;
            this.ctrlKey = param7;
            this.altKey = param8;
            this.shiftKey = param9;
            return;
        }// end function

        override public function clone() : Event
        {
            return new KeyboardEvent(type, bubbles, cancelable, this.charCode, this.keyCode, this.keyLocation, this.ctrlKey, this.altKey, this.shiftKey);
        }// end function

        override public function toString() : String
        {
            return formatToString("KeyboardEvent", "type", "bubbles", "cancelable", "eventPhase", "charCode", "keyCode", "keyLocation", "ctrlKey", "altKey", "shiftKey");
        }// end function

        public function get charCode() : uint;

        public function set charCode(param1:uint) : void;

        public function get keyCode() : uint
        {
            return this.m_keyCode;
        }// end function

        public function set keyCode(param1:uint) : void
        {
            this.m_keyCode = param1;
            return;
        }// end function

        public function get keyLocation() : uint
        {
            return this.m_keyLocation;
        }// end function

        public function set keyLocation(param1:uint) : void
        {
            this.m_keyLocation = param1;
            return;
        }// end function

        public function get ctrlKey() : Boolean;

        public function set ctrlKey(param1:Boolean) : void;

        public function get altKey() : Boolean;

        public function set altKey(param1:Boolean) : void;

        public function get shiftKey() : Boolean;

        public function set shiftKey(param1:Boolean) : void;

        public function updateAfterEvent() : void;

    }
}