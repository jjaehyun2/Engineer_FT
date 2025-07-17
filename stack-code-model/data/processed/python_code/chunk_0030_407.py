package preview_fla
{
    import flash.display.*;
    import flash.events.*;
    import flash.net.*;

    dynamic public class background1_12 extends MovieClip
    {
        public var bg1iconBMP:Bitmap;
        public var bg1iconString:String;
        public var bg1iconLoader:Loader;
        public var url:URLRequest;

        public function background1_12()
        {
            addFrameScript(0, frame1);
            return;
        }// end function

        public function bg1iconLoaded(param1:Event) : void
        {
            bg1iconLoader.contentLoaderInfo.removeEventListener(Event.COMPLETE, bg1iconLoaded);
            bg1iconLoader = null;
            bg1iconBMP.bitmapData = Bitmap(param1.target.content).bitmapData;
            addChild(bg1iconBMP);
            return;
        }// end function

        function frame1()
        {
            bg1iconString = "./site_images/bg1icon.jpg";
            bg1iconBMP = new Bitmap();
            url = new URLRequest(bg1iconString);
            bg1iconLoader = new Loader();
            bg1iconLoader.contentLoaderInfo.addEventListener(Event.COMPLETE, bg1iconLoaded, false, 0, true);
            bg1iconLoader.load(url);
            return;
        }// end function

    }
}