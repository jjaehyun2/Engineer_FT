package preview_fla
{
    import flash.display.*;
    import flash.events.*;
    import flash.net.*;

    dynamic public class vc_back_32 extends MovieClip
    {
        public var backString:String;
        public var backBMP:Bitmap;
        public var url:URLRequest;
        public var backLoader:Loader;

        public function vc_back_32()
        {
            addFrameScript(0, frame1);
            return;
        }// end function

        function frame1()
        {
            backString = "./site_images/back.png";
            backBMP = new Bitmap();
            url = new URLRequest(backString);
            backLoader = new Loader();
            backLoader.contentLoaderInfo.addEventListener(Event.COMPLETE, backLoaded, false, 0, true);
            backLoader.load(url);
            return;
        }// end function

        public function backLoaded(param1:Event) : void
        {
            backLoader.contentLoaderInfo.removeEventListener(Event.COMPLETE, backLoaded);
            backLoader = null;
            backBMP.bitmapData = Bitmap(param1.target.content).bitmapData;
            addChild(backBMP);
            return;
        }// end function

    }
}