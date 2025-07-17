package flash.globalization
{
    import __AS3__.vec.*;

    final public class Collator extends Object
    {

        public function Collator(param1:String, param2:String = "sorting")
        {
            this.ctor(param1, param2);
            return;
        }// end function

        private function ctor(param1:String, param2:String) : void;

        public function get ignoreCase() : Boolean;

        public function set ignoreCase(param1:Boolean) : void;

        public function get ignoreDiacritics() : Boolean;

        public function set ignoreDiacritics(param1:Boolean) : void;

        public function get ignoreKanaType() : Boolean;

        public function set ignoreKanaType(param1:Boolean) : void;

        public function get ignoreSymbols() : Boolean;

        public function set ignoreSymbols(param1:Boolean) : void;

        public function get ignoreCharacterWidth() : Boolean;

        public function set ignoreCharacterWidth(param1:Boolean) : void;

        public function get numericComparison() : Boolean;

        public function set numericComparison(param1:Boolean) : void;

        public function compare(param1:String, param2:String) : int;

        public function equals(param1:String, param2:String) : Boolean;

        public function get lastOperationStatus() : String;

        public function get actualLocaleIDName() : String;

        public function get requestedLocaleIDName() : String;

        public static function getAvailableLocaleIDNames() : Vector.<String>;

    }
}