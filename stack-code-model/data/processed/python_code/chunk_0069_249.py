package 
{
    import flash.display.*;
    import flash.events.*;
    import flash.net.*;

    dynamic public class playaBack extends MovieClip
    {
        public var mp3backBMP:Bitmap;
        public var url:URLRequest;
        public var mp3backLoader:Loader;
        public var mp3backString:String;

        public function playaBack()
        {
            addFrameScript(0, frame1);
            return;
        }// end function

        function frame1()
        {
            mp3backString = "./site_images/mp3back.png";
            mp3backBMP = new Bitmap();
            url = new URLRequest(mp3backString);
            mp3backLoader = new Loader();
            mp3backLoader.contentLoaderInfo.addEventListener(Event.COMPLETE, mp3backLoaded, false, 0, true);
            mp3backLoader.load(url);
            return;
        }// end function

        public function mp3backLoaded(param1:Event) : void
        {
            mp3backLoader.contentLoaderInfo.removeEventListener(Event.COMPLETE, mp3backLoaded);
            mp3backLoader = null;
            mp3backBMP.bitmapData = Bitmap(param1.target.content).bitmapData;
            addChild(mp3backBMP);
            return;
        }// end function

    }
}