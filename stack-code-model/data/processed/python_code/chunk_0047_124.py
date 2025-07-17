package flash.text.engine
{

    final public class SpaceJustifier extends TextJustifier
    {

        public function SpaceJustifier(param1:String = "en", param2:String = "unjustified", param3:Boolean = false)
        {
            super(param1, param2);
            this.letterSpacing = param3;
            return;
        }// end function

        public function get letterSpacing() : Boolean;

        public function set letterSpacing(param1:Boolean) : void;

        public function get minimumSpacing() : Number;

        public function set minimumSpacing(param1:Number) : void;

        public function get optimumSpacing() : Number;

        public function set optimumSpacing(param1:Number) : void;

        public function get maximumSpacing() : Number;

        public function set maximumSpacing(param1:Number) : void;

        override public function clone() : TextJustifier
        {
            var _loc_1:* = new SpaceJustifier(this.locale, this.lineJustification, this.letterSpacing);
            _loc_1.cloneSpacing(this);
            return _loc_1;
        }// end function

        private function cloneSpacing(param1:SpaceJustifier) : void;

    }
}