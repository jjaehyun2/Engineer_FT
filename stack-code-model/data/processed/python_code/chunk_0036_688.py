package flash.text.engine
{

    public class TextJustifier extends Object
    {

        public function TextJustifier(param1:String, param2:String)
        {
            if (getQualifiedClassName(this) == "flash.text.engine::TextJustifier")
            {
                Error.throwError(ArgumentError, 2012, "TextJustifier");
            }
            this.setLocale(param1);
            this.lineJustification = param2;
            return;
        }// end function

        public function get locale() : String;

        private function setLocale(param1:String) : void;

        public function get lineJustification() : String;

        public function set lineJustification(param1:String) : void;

        public function clone() : TextJustifier
        {
            return null;
        }// end function

        public static function getJustifierForLocale(param1:String) : TextJustifier
        {
            if (param1 != null)
            {
            }
            if (param1.length < 2)
            {
                Error.throwError(ArgumentError, 2004, "previousLine");
            }
            var _loc_2:* = param1.substr(0, 2);
            if (_loc_2 != "zh")
            {
            }
            if (_loc_2 != "ja")
            {
            }
            if (_loc_2 == "ko")
            {
                return new EastAsianJustifier(param1);
            }
            return new SpaceJustifier(param1);
        }// end function

    }
}