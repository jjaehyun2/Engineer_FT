package flash.system
{
    import flash.events.*;

    final public class MessageChannel extends EventDispatcher
    {

        public function MessageChannel()
        {
            return;
        }// end function

        public function send(param1, param2:int = -1) : void;

        public function get messageAvailable() : Boolean;

        public function receive(param1:Boolean = false);

        override public function addEventListener(param1:String, param2:Function, param3:Boolean = false, param4:int = 0, param5:Boolean = false) : void
        {
            this.internalAddEventListener(param1, param2, param3, param4, param5);
            return;
        }// end function

        override public function removeEventListener(param1:String, param2:Function, param3:Boolean = false) : void
        {
            this.internalRemoveEventListener(param1, param2);
            return;
        }// end function

        public function close() : void;

        public function get state() : String;

        override public function toString() : String
        {
            return "[object MessageChannel]";
        }// end function

        private function internalRemoveEventListener(param1:String, param2:Function, param3:Boolean = false) : void;

        private function internalAddEventListener(param1:String, param2:Function, param3:Boolean = false, param4:int = 0, param5:Boolean = false) : void;

    }
}