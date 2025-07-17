package 
{
    import flash.display.*;
    import flash.events.*;
    import flash.net.*;

    dynamic public class newsSCROLLA extends MovieClip
    {
        public var blogString:String;
        public var blogLoader:Loader;
        public var url:URLRequest;
        public var blogBMP:Bitmap;

        public function newsSCROLLA()
        {
            addFrameScript(0, frame1);
            return;
        }// end function

        public function blogLoaded(param1:Event) : void
        {
            blogLoader.contentLoaderInfo.removeEventListener(Event.COMPLETE, blogLoaded);
            blogLoader = null;
            blogBMP.bitmapData = Bitmap(param1.target.content).bitmapData;
            addChild(blogBMP);
            return;
        }// end function

        function frame1()
        {
            blogString = "./site_images/blogScrubber.jpg";
            blogBMP = new Bitmap();
            url = new URLRequest(blogString);
            blogLoader = new Loader();
            blogLoader.contentLoaderInfo.addEventListener(Event.COMPLETE, blogLoaded, false, 0, true);
            blogLoader.load(url);
            return;
        }// end function

    }
}