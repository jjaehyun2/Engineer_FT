package flash.text.engine
{

    final public class TabStop extends Object
    {

        public function TabStop(param1:String = "start", param2:Number = 0, param3:String = "")
        {
            this.alignment = param1;
            this.position = param2;
            this.decimalAlignmentToken = param3;
            return;
        }// end function

        public function get alignment() : String;

        public function set alignment(param1:String) : void;

        public function get position() : Number;

        public function set position(param1:Number) : void;

        public function get decimalAlignmentToken() : String;

        public function set decimalAlignmentToken(param1:String) : void;

    }
}