package flash.events
{

    public class AsyncErrorEvent extends ErrorEvent
    {
        public var error:Error;
        public static const ASYNC_ERROR:String = "asyncError";

        public function AsyncErrorEvent(param1:String, param2:Boolean = false, param3:Boolean = false, param4:String = "", param5:Error = null)
        {
            this.error = param5;
            var _loc_6:* = 0;
            if (param5)
            {
                _loc_6 = param5.errorID;
            }
            super(param1, param2, param3, param4, _loc_6);
            return;
        }// end function

        override public function clone() : Event
        {
            return new AsyncErrorEvent(type, bubbles, cancelable, text, this.error);
        }// end function

        override public function toString() : String
        {
            return formatToString("AsyncErrorEvent", "type", "bubbles", "cancelable", "eventPhase", "text", "error");
        }// end function

    }
}