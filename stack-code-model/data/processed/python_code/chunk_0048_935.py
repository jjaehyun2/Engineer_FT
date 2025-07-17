package flash.filters
{

    final public class GradientBevelFilter extends BitmapFilter
    {

        public function GradientBevelFilter(param1:Number = 4, param2:Number = 45, param3:Array = null, param4:Array = null, param5:Array = null, param6:Number = 4, param7:Number = 4, param8:Number = 1, param9:int = 1, param10:String = "inner", param11:Boolean = false)
        {
            this.distance = param1;
            this.angle = param2;
            if (param3 != null)
            {
                this.colors = param3;
            }
            if (param4 != null)
            {
                this.alphas = param4;
            }
            if (param5 != null)
            {
                this.ratios = param5;
            }
            this.blurX = param6;
            this.blurY = param7;
            this.quality = param9;
            this.strength = param8;
            this.type = param10;
            this.knockout = param11;
            return;
        }// end function

        public function get distance() : Number;

        public function set distance(param1:Number) : void;

        public function get angle() : Number;

        public function set angle(param1:Number) : void;

        public function get colors() : Array;

        public function set colors(param1:Array) : void;

        public function get alphas() : Array;

        public function set alphas(param1:Array) : void;

        public function get ratios() : Array;

        public function set ratios(param1:Array) : void;

        public function get blurX() : Number;

        public function set blurX(param1:Number) : void;

        public function get blurY() : Number;

        public function set blurY(param1:Number) : void;

        public function get knockout() : Boolean;

        public function set knockout(param1:Boolean) : void;

        public function get quality() : int;

        public function set quality(param1:int) : void;

        public function get strength() : Number;

        public function set strength(param1:Number) : void;

        public function get type() : String;

        public function set type(param1:String) : void;

        override public function clone() : BitmapFilter
        {
            return new GradientBevelFilter(this.distance, this.angle, this.colors, this.alphas, this.ratios, this.blurX, this.blurY, this.strength, this.quality, this.type, this.knockout);
        }// end function

    }
}