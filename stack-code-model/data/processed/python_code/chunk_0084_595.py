package flash.display
{
    import flash.geom.*;
    import flash.text.*;

    public class DisplayObjectContainer extends InteractiveObject
    {

        public function DisplayObjectContainer()
        {
            return;
        }// end function

        public function addChild(param1:DisplayObject) : DisplayObject;

        public function addChildAt(param1:DisplayObject, param2:int) : DisplayObject;

        public function removeChild(param1:DisplayObject) : DisplayObject;

        public function removeChildAt(param1:int) : DisplayObject;

        public function getChildIndex(param1:DisplayObject) : int;

        public function setChildIndex(param1:DisplayObject, param2:int) : void;

        public function getChildAt(param1:int) : DisplayObject;

        public function getChildByName(param1:String) : DisplayObject;

        public function get numChildren() : int;

        public function get textSnapshot() : TextSnapshot;

        public function getObjectsUnderPoint(param1:Point) : Array;

        public function areInaccessibleObjectsUnderPoint(param1:Point) : Boolean;

        public function get tabChildren() : Boolean;

        public function set tabChildren(param1:Boolean) : void;

        public function get mouseChildren() : Boolean;

        public function set mouseChildren(param1:Boolean) : void;

        public function contains(param1:DisplayObject) : Boolean;

        public function swapChildrenAt(param1:int, param2:int) : void;

        public function swapChildren(param1:DisplayObject, param2:DisplayObject) : void;

        public function removeChildren(param1:int = 0, param2:int = 2147483647) : void;

        public function stopAllMovieClips() : void;

    }
}