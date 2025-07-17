package flash.text
{

    public class TextFormat extends Object
    {

        public function TextFormat(param1:String = null, param2:Object = null, param3:Object = null, param4:Object = null, param5:Object = null, param6:Object = null, param7:String = null, param8:String = null, param9:String = null, param10:Object = null, param11:Object = null, param12:Object = null, param13:Object = null)
        {
            if (param1 != null)
            {
                this.font = param1;
            }
            if (param2 != null)
            {
                this.size = param2;
            }
            if (param3 != null)
            {
                this.color = param3;
            }
            if (param4 != null)
            {
                this.bold = param4;
            }
            if (param5 != null)
            {
                this.italic = param5;
            }
            if (param6 != null)
            {
                this.underline = param6;
            }
            if (param7 != null)
            {
                this.url = param7;
            }
            if (param8 != null)
            {
                this.target = param8;
            }
            if (param9 != null)
            {
                this.align = param9;
            }
            if (param10 != null)
            {
                this.leftMargin = param10;
            }
            if (param11 != null)
            {
                this.rightMargin = param11;
            }
            if (param12 != null)
            {
                this.indent = param12;
            }
            if (param13 != null)
            {
                this.leading = param13;
            }
            return;
        }// end function

        public function get align() : String;

        public function set align(param1:String) : void;

        public function get blockIndent() : Object;

        public function set blockIndent(param1:Object) : void;

        public function get bold() : Object;

        public function set bold(param1:Object) : void;

        public function get bullet() : Object;

        public function set bullet(param1:Object) : void;

        public function get color() : Object;

        public function set color(param1:Object) : void;

        public function get display() : String;

        public function set display(param1:String) : void;

        public function get font() : String;

        public function set font(param1:String) : void;

        public function get indent() : Object;

        public function set indent(param1:Object) : void;

        public function get italic() : Object;

        public function set italic(param1:Object) : void;

        public function get kerning() : Object;

        public function set kerning(param1:Object) : void;

        public function get leading() : Object;

        public function set leading(param1:Object) : void;

        public function get leftMargin() : Object;

        public function set leftMargin(param1:Object) : void;

        public function get letterSpacing() : Object;

        public function set letterSpacing(param1:Object) : void;

        public function get rightMargin() : Object;

        public function set rightMargin(param1:Object) : void;

        public function get size() : Object;

        public function set size(param1:Object) : void;

        public function get tabStops() : Array;

        public function set tabStops(param1:Array) : void;

        public function get target() : String;

        public function set target(param1:String) : void;

        public function get underline() : Object;

        public function set underline(param1:Object) : void;

        public function get url() : String;

        public function set url(param1:String) : void;

    }
}