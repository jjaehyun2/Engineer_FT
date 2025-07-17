package flash.printing
{
    import flash.display.*;
    import flash.events.*;
    import flash.geom.*;

    public class PrintJob extends EventDispatcher
    {
        private static const kGetPaperHeight:uint = 1;
        private static const kGetPaperWidth:uint = 3;
        private static const kGetPageHeight:uint = 5;
        private static const kGetPageWidth:uint = 7;
        private static const kGetOrientation:uint = 9;
        private static const kStart:uint = 100;
        private static const kAddPage:uint = 101;
        private static const kSend:uint = 102;

        public function PrintJob()
        {
            return;
        }// end function

        public function get paperHeight() : int
        {
            return this.invoke(kGetPaperHeight);
        }// end function

        public function get paperWidth() : int
        {
            return this.invoke(kGetPaperWidth);
        }// end function

        public function get pageHeight() : int
        {
            return this.invoke(kGetPageHeight);
        }// end function

        public function get pageWidth() : int
        {
            return this.invoke(kGetPageWidth);
        }// end function

        public function get orientation() : String
        {
            return this.invoke(kGetOrientation);
        }// end function

        public function start() : Boolean
        {
            return this.invoke(kStart) == true;
        }// end function

        private function invoke(param1:uint, ... args);

        private function _invoke(param1, ... args);

        public function send() : void
        {
            this.invoke(kSend);
            return;
        }// end function

        private function toClassicRectangle(param1:Rectangle)
        {
            if (param1 != null)
            {
                return {xMin:param1.left, yMin:param1.top, xMax:param1.right, yMax:param1.bottom};
            }
            return null;
        }// end function

        public function addPage(param1:Sprite, param2:Rectangle = null, param3:PrintJobOptions = null, param4:int = 0) : void
        {
            var _loc_5:* = null;
            if (param3 != null)
            {
                _loc_5 = {printAsBitmap:param3.printAsBitmap};
            }
            if (this._invoke(kAddPage, param1, this.toClassicRectangle(param2), _loc_5, param4 > 0 ? (param4) : (-1)) == false)
            {
                Error.throwError(Error, 2057);
            }
            return;
        }// end function

        public static function get isSupported() : Boolean
        {
            return _checkSupported();
        }// end function

        private static function _checkSupported() : Boolean;

    }
}