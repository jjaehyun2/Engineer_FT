package preview_fla
{
    import flash.display.*;
    import flash.events.*;
    import flash.net.*;

    dynamic public class fs_15 extends MovieClip
    {
        public var url:URLRequest;
        public var fullScreenBMP:Bitmap;
        public var fullScreenString:String;
        public var fullScreenLoader:Loader;

        public function fs_15()
        {
            addFrameScript(0, frame1);
            return;
        }// end function

        function frame1()
        {
            fullScreenString = "./site_images/fullScreen.jpg";
            fullScreenBMP = new Bitmap();
            url = new URLRequest(fullScreenString);
            fullScreenLoader = new Loader();
            fullScreenLoader.contentLoaderInfo.addEventListener(Event.COMPLETE, fullScreenLoaded, false, 0, true);
            fullScreenLoader.load(url);
            return;
        }// end function

        public function fullScreenLoaded(param1:Event) : void
        {
            fullScreenLoader.contentLoaderInfo.removeEventListener(Event.COMPLETE, fullScreenLoaded);
            fullScreenLoader = null;
            fullScreenBMP.bitmapData = Bitmap(param1.target.content).bitmapData;
            addChild(fullScreenBMP);
            return;
        }// end function

    }
}