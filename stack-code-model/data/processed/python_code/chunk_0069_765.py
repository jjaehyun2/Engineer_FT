package flash.events
{
    import flash.display.*;

    public class FocusEvent extends Event
    {
        private var m_relatedObject:InteractiveObject;
        private var m_shiftKey:Boolean;
        private var m_keyCode:uint;
        private var m_isRelatedObjectInaccessible:Boolean;
        public static const FOCUS_IN:String = "focusIn";
        public static const FOCUS_OUT:String = "focusOut";
        public static const KEY_FOCUS_CHANGE:String = "keyFocusChange";
        public static const MOUSE_FOCUS_CHANGE:String = "mouseFocusChange";

        public function FocusEvent(param1:String, param2:Boolean = true, param3:Boolean = false, param4:InteractiveObject = null, param5:Boolean = false, param6:uint = 0)
        {
            super(param1, param2, param3);
            this.m_relatedObject = param4;
            this.m_shiftKey = param5;
            this.m_keyCode = param6;
            return;
        }// end function

        override public function clone() : Event
        {
            return new FocusEvent(type, bubbles, cancelable, this.m_relatedObject, this.m_shiftKey, this.m_keyCode);
        }// end function

        public function get relatedObject() : InteractiveObject
        {
            return this.m_relatedObject;
        }// end function

        public function set relatedObject(param1:InteractiveObject) : void
        {
            this.m_relatedObject = param1;
            return;
        }// end function

        public function get shiftKey() : Boolean
        {
            return this.m_shiftKey;
        }// end function

        public function set shiftKey(param1:Boolean) : void
        {
            this.m_shiftKey = param1;
            return;
        }// end function

        public function get keyCode() : uint
        {
            return this.m_keyCode;
        }// end function

        public function set keyCode(param1:uint) : void
        {
            this.m_keyCode = param1;
            return;
        }// end function

        public function get isRelatedObjectInaccessible() : Boolean
        {
            return this.m_isRelatedObjectInaccessible;
        }// end function

        public function set isRelatedObjectInaccessible(param1:Boolean) : void
        {
            this.m_isRelatedObjectInaccessible = param1;
            return;
        }// end function

        override public function toString() : String
        {
            return formatToString("FocusEvent", "type", "bubbles", "cancelable", "eventPhase", "relatedObject", "shiftKey", "keyCode");
        }// end function

    }
}