package flash.geom
{

    public class ColorTransform extends Object
    {
        public var redMultiplier:Number;
        public var greenMultiplier:Number;
        public var blueMultiplier:Number;
        public var alphaMultiplier:Number;
        public var redOffset:Number;
        public var greenOffset:Number;
        public var blueOffset:Number;
        public var alphaOffset:Number;

        public function ColorTransform(param1:Number = 1, param2:Number = 1, param3:Number = 1, param4:Number = 1, param5:Number = 0, param6:Number = 0, param7:Number = 0, param8:Number = 0)
        {
            this.redMultiplier = param1;
            this.greenMultiplier = param2;
            this.blueMultiplier = param3;
            this.alphaMultiplier = param4;
            this.redOffset = param5;
            this.greenOffset = param6;
            this.blueOffset = param7;
            this.alphaOffset = param8;
            return;
        }// end function

        public function get color() : uint
        {
            return this.redOffset << 16 | this.greenOffset << 8 | this.blueOffset;
        }// end function

        public function set color(param1:uint) : void
        {
            var _loc_2:* = 0;
            this.blueMultiplier = 0;
            this.greenMultiplier = _loc_2;
            this.redMultiplier = _loc_2;
            this.redOffset = param1 >> 16 & 255;
            this.greenOffset = param1 >> 8 & 255;
            this.blueOffset = param1 & 255;
            return;
        }// end function

        public function concat(param1:ColorTransform) : void
        {
            this.alphaOffset = this.alphaOffset + this.alphaMultiplier * param1.alphaOffset;
            this.alphaMultiplier = this.alphaMultiplier * param1.alphaMultiplier;
            this.redOffset = this.redOffset + this.redMultiplier * param1.redOffset;
            this.redMultiplier = this.redMultiplier * param1.redMultiplier;
            this.greenOffset = this.greenOffset + this.greenMultiplier * param1.greenOffset;
            this.greenMultiplier = this.greenMultiplier * param1.greenMultiplier;
            this.blueOffset = this.blueOffset + this.blueMultiplier * param1.blueOffset;
            this.blueMultiplier = this.blueMultiplier * param1.blueMultiplier;
            return;
        }// end function

        public function toString() : String
        {
            return "(redMultiplier=" + this.redMultiplier + ", greenMultiplier=" + this.greenMultiplier + ", blueMultiplier=" + this.blueMultiplier + ", alphaMultiplier=" + this.alphaMultiplier + ", redOffset=" + this.redOffset + ", greenOffset=" + this.greenOffset + ", blueOffset=" + this.blueOffset + ", alphaOffset=" + this.alphaOffset + ")";
        }// end function

    }
}