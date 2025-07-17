package flash.globalization
{

    final public class CurrencyParseResult extends Object
    {

        public function CurrencyParseResult(param1:Number = NaN, param2:String = "")
        {
            this.ctor(param1, param2);
            return;
        }// end function

        private function ctor(param1:Number, param2:String) : void;

        public function get value() : Number;

        public function get currencyString() : String;

    }
}