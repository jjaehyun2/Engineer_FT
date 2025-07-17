package flash.media
{
    import __AS3__.vec.*;
    import flash.events.*;
    import flash.geom.*;
    import flash.net.*;

    public class StageVideo extends EventDispatcher
    {

        public function StageVideo()
        {
            return;
        }// end function

        public function attachNetStream(param1:NetStream) : void;

        public function attachCamera(param1:Camera) : void;

        public function get viewPort() : Rectangle;

        public function set viewPort(param1:Rectangle) : void;

        public function set pan(param1:Point) : void;

        public function get pan() : Point;

        public function set zoom(param1:Point) : void;

        public function get zoom() : Point;

        public function set depth(param1:int) : void;

        public function get depth() : int;

        public function get videoWidth() : int;

        public function get videoHeight() : int;

        public function get colorSpaces() : Vector.<String>;

        public function attachAVStream(param1:AVStream) : void;

    }
}