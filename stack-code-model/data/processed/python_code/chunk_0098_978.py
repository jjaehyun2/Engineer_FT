package flash.display
{

    final public class JPEGXREncoderOptions extends Object
    {
        public var quantization:uint;
        public var colorSpace:String;
        public var trimFlexBits:uint;

        public function JPEGXREncoderOptions(param1:uint = 20, param2:String = "auto", param3:uint = 0)
        {
            this.quantization = param1;
            this.colorSpace = param2;
            this.trimFlexBits = param3;
            return;
        }// end function

    }
}