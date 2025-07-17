package flash.globalization
{
    import __AS3__.vec.*;

    final public class NumberFormatter extends Object
    {

        public function NumberFormatter(param1:String)
        {
            this.ctor(param1);
            return;
        }// end function

        private function ctor(param1:String) : void;

        public function get lastOperationStatus() : String;

        public function get requestedLocaleIDName() : String;

        public function get actualLocaleIDName() : String;

        public function get fractionalDigits() : int;

        public function set fractionalDigits(param1:int) : void;

        public function get useGrouping() : Boolean;

        public function set useGrouping(param1:Boolean) : void;

        public function get groupingPattern() : String;

        public function set groupingPattern(param1:String) : void;

        public function get digitsType() : uint;

        public function set digitsType(param1:uint) : void;

        public function get decimalSeparator() : String;

        public function set decimalSeparator(param1:String) : void;

        public function get groupingSeparator() : String;

        public function set groupingSeparator(param1:String) : void;

        public function get negativeSymbol() : String;

        public function set negativeSymbol(param1:String) : void;

        public function get negativeNumberFormat() : uint;

        public function set negativeNumberFormat(param1:uint) : void;

        public function get leadingZero() : Boolean;

        public function set leadingZero(param1:Boolean) : void;

        public function get trailingZeros() : Boolean;

        public function set trailingZeros(param1:Boolean) : void;

        public function parse(param1:String) : NumberParseResult;

        public function parseNumber(param1:String) : Number;

        public function formatInt(param1:int) : String;

        public function formatUint(param1:uint) : String;

        public function formatNumber(param1:Number) : String;

        public static function getAvailableLocaleIDNames() : Vector.<String>;

    }
}