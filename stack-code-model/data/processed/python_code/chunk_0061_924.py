package flash.display
{

    public class Bitmap extends DisplayObject
    {

        public function Bitmap(param1:BitmapData = null, param2:String = "auto", param3:Boolean = false)
        {
            this.ctor(param1, param2, param3);
            return;
        }// end function

        private function ctor(param1:BitmapData, param2:String, param3:Boolean) : void;

        public function get pixelSnapping() : String;

        public function set pixelSnapping(param1:String) : void;

        public function get smoothing() : Boolean;

        public function set smoothing(param1:Boolean) : void;

        public function get bitmapData() : BitmapData;

        public function set bitmapData(param1:BitmapData) : void;

    }
}