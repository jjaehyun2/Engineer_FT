package preview_fla
{
    import flash.display.*;
    import flash.events.*;
    import flash.net.*;

    dynamic public class background3_14 extends MovieClip
    {
        public var bg3iconLoader:Loader;
        public var bg3iconBMP:Bitmap;
        public var url:URLRequest;
        public var bg3iconString:String;

        public function background3_14()
        {
            addFrameScript(0, frame1);
            return;
        }// end function

        public function bg3iconLoaded(param1:Event) : void
        {
            bg3iconLoader.contentLoaderInfo.removeEventListener(Event.COMPLETE, bg3iconLoaded);
            bg3iconLoader = null;
            bg3iconBMP.bitmapData = Bitmap(param1.target.content).bitmapData;
            addChild(bg3iconBMP);
            return;
        }// end function

        function frame1()
        {
            bg3iconString = "./site_images/bg3icon.jpg";
            bg3iconBMP = new Bitmap();
            url = new URLRequest(bg3iconString);
            bg3iconLoader = new Loader();
            bg3iconLoader.contentLoaderInfo.addEventListener(Event.COMPLETE, bg3iconLoaded, false, 0, true);
            bg3iconLoader.load(url);
            return;
        }// end function

    }
}