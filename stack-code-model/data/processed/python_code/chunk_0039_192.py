package flash.filters
{

    final public class BlurFilter extends BitmapFilter
    {

        public function BlurFilter(param1:Number = 4, param2:Number = 4, param3:int = 1)
        {
            this.blurX = param1;
            this.blurY = param2;
            this.quality = param3;
            return;
        }// end function

        public function get blurX() : Number;

        public function set blurX(param1:Number) : void;

        public function get blurY() : Number;

        public function set blurY(param1:Number) : void;

        public function get quality() : int;

        public function set quality(param1:int) : void;

        override public function clone() : BitmapFilter
        {
            return new BlurFilter(this.blurX, this.blurY, this.quality);
        }// end function

    }
}