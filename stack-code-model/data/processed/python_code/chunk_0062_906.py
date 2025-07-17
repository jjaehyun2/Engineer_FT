package flash.events
{
    import flash.display.*;

    public class SoftKeyboardEvent extends Event
    {
        private var m_relatedObject:InteractiveObject;
        private var m_triggerType:String;
        public static const SOFT_KEYBOARD_ACTIVATE:String = "softKeyboardActivate";
        public static const SOFT_KEYBOARD_DEACTIVATE:String = "softKeyboardDeactivate";
        public static const SOFT_KEYBOARD_ACTIVATING:String = "softKeyboardActivating";

        public function SoftKeyboardEvent(param1:String, param2:Boolean, param3:Boolean, param4:InteractiveObject, param5:String)
        {
            super(param1, param2, param3);
            this.relatedObject = param4;
            this.m_triggerType = param5;
            return;
        }// end function

        override public function clone() : Event
        {
            return new SoftKeyboardEvent(type, bubbles, cancelable, this.m_relatedObject, this.m_triggerType);
        }// end function

        override public function toString() : String
        {
            return formatToString("SoftKeyboardEvent", "type", "bubbles", "cancelable", "relatedObject", "triggerType");
        }// end function

        public function get triggerType() : String
        {
            return this.m_triggerType;
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

    }
}