package flash.text.engine
{
    import flash.events.*;

    public class ContentElement extends Object
    {
        public var userData:Object;
        public static const GRAPHIC_ELEMENT:uint = 65007;

        public function ContentElement(param1:ElementFormat = null, param2:EventDispatcher = null, param3:String = "rotate0")
        {
            if (getQualifiedClassName(this) == "flash.text.engine::ContentElement")
            {
                Error.throwError(ArgumentError, 2012, "ContentElement");
            }
            this.elementFormat = param1;
            this.eventMirror = param2;
            this.textRotation = param3;
            return;
        }// end function

        public function get textBlock() : TextBlock;

        public function get textBlockBeginIndex() : int;

        public function get elementFormat() : ElementFormat;

        public function set elementFormat(param1:ElementFormat) : void;

        public function get eventMirror() : EventDispatcher;

        public function set eventMirror(param1:EventDispatcher) : void;

        public function get groupElement() : GroupElement;

        public function get rawText() : String;

        public function get text() : String;

        public function get textRotation() : String;

        public function set textRotation(param1:String) : void;

    }
}