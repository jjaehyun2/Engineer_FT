package flash.globalization
{

    final public class NumberParseResult extends Object
    {

        public function NumberParseResult(param1:Number = NaN, param2:int = 2147483647, param3:int = 2147483647)
        {
            this.ctor(param1, param2, param3);
            return;
        }// end function

        private function ctor(param1:Number, param2:int, param3:int) : void;

        public function get value() : Number;

        public function get startIndex() : int;

        public function get endIndex() : int;

    }
}