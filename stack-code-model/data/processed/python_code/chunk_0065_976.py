package flash.text
{

    public class TextExtent extends Object
    {
        public var width:Number;
        public var height:Number;
        public var textFieldWidth:Number;
        public var textFieldHeight:Number;
        public var ascent:Number;
        public var descent:Number;

        public function TextExtent(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number, param6:Number)
        {
            this.width = param1;
            this.height = param2;
            this.textFieldWidth = param3;
            this.textFieldHeight = param4;
            this.ascent = param5;
            this.descent = param6;
            return;
        }// end function

    }
}