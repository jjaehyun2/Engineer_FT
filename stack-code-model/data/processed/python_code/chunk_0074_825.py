package flash.events
{

    public class StatusEvent extends Event
    {
        private var m_code:String;
        private var m_level:String;
        public static const STATUS:String = "status";

        public function StatusEvent(param1:String, param2:Boolean = false, param3:Boolean = false, param4:String = "", param5:String = "")
        {
            super(param1, param2, param3);
            this.m_code = param4;
            this.m_level = param5;
            return;
        }// end function

        override public function clone() : Event
        {
            return new StatusEvent(type, bubbles, cancelable, this.m_code, this.m_level);
        }// end function

        override public function toString() : String
        {
            return formatToString("StatusEvent", "type", "bubbles", "cancelable", "eventPhase", "code", "level");
        }// end function

        public function get code() : String
        {
            return this.m_code;
        }// end function

        public function set code(param1:String) : void
        {
            this.m_code = param1;
            return;
        }// end function

        public function get level() : String
        {
            return this.m_level;
        }// end function

        public function set level(param1:String) : void
        {
            this.m_level = param1;
            return;
        }// end function

    }
}