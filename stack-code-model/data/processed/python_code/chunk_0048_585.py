package flash.concurrent
{

    final public class Condition extends Object
    {

        public function Condition(param1:Mutex)
        {
            this.ctor(param1);
            return;
        }// end function

        public function get mutex() : Mutex;

        public function wait(param1:Number = -1) : Boolean;

        public function notify() : void;

        public function notifyAll() : void;

        private function ctor(param1:Mutex) : void;

        public static function get isSupported() : Boolean;

    }
}