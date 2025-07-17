package flash.filters
{

    final public class GlowFilter extends BitmapFilter
    {

        public function GlowFilter(param1:uint = 16711680, param2:Number = 1, param3:Number = 6, param4:Number = 6, param5:Number = 2, param6:int = 1, param7:Boolean = false, param8:Boolean = false)
        {
            this.color = param1;
            this.alpha = param2;
            this.blurX = param3;
            this.blurY = param4;
            this.quality = param6;
            this.strength = param5;
            this.inner = param7;
            this.knockout = param8;
            return;
        }// end function

        public function get color() : uint;

        public function set color(param1:uint) : void;

        public function get alpha() : Number;

        public function set alpha(param1:Number) : void;

        public function get blurX() : Number;

        public function set blurX(param1:Number) : void;

        public function get blurY() : Number;

        public function set blurY(param1:Number) : void;

        public function get inner() : Boolean;

        public function set inner(param1:Boolean) : void;

        public function get knockout() : Boolean;

        public function set knockout(param1:Boolean) : void;

        public function get quality() : int;

        public function set quality(param1:int) : void;

        public function get strength() : Number;

        public function set strength(param1:Number) : void;

        override public function clone() : BitmapFilter
        {
            return new GlowFilter(this.color, this.alpha, this.blurX, this.blurY, this.strength, this.quality, this.inner, this.knockout);
        }// end function

    }
}