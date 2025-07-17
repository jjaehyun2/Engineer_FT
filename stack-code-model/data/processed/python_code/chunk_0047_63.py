package flash.text.engine
{
    import __AS3__.vec.*;
    import flash.display.*;
    import flash.events.*;
    import flash.geom.*;
    import flash.ui.*;

    final public class TextLine extends DisplayObjectContainer
    {
        public var userData:Object;
        public static const MAX_LINE_WIDTH:int = 1000000;

        public function TextLine()
        {
            return;
        }// end function

        override public function set focusRect(param1:Object) : void
        {
            Error.throwError(IllegalOperationError, 2181);
            return;
        }// end function

        override public function set tabChildren(param1:Boolean) : void
        {
            Error.throwError(IllegalOperationError, 2181);
            return;
        }// end function

        override public function set tabEnabled(param1:Boolean) : void
        {
            Error.throwError(IllegalOperationError, 2181);
            return;
        }// end function

        override public function set tabIndex(param1:int) : void
        {
            Error.throwError(IllegalOperationError, 2181);
            return;
        }// end function

        public function get textBlock() : TextBlock;

        public function get hasGraphicElement() : Boolean;

        public function get hasTabs() : Boolean;

        public function get nextLine() : TextLine;

        public function get previousLine() : TextLine;

        public function get ascent() : Number;

        public function get descent() : Number;

        public function get textHeight() : Number;

        public function get textWidth() : Number;

        public function get totalAscent() : Number;

        public function get totalDescent() : Number;

        public function get totalHeight() : Number;

        public function get textBlockBeginIndex() : int;

        public function get rawTextLength() : int;

        public function get specifiedWidth() : Number;

        public function get unjustifiedTextWidth() : Number;

        public function get validity() : String;

        public function set validity(param1:String) : void;

        public function get atomCount() : int;

        public function get mirrorRegions() : Vector.<TextLineMirrorRegion>;

        public function getMirrorRegion(param1:EventDispatcher) : TextLineMirrorRegion
        {
            var _loc_4:* = null;
            var _loc_2:* = this.mirrorRegions;
            var _loc_3:* = 0;
            while (_loc_3 < _loc_2.length)
            {
                
                _loc_4 = _loc_2[_loc_3];
                if (_loc_4.mirror == param1)
                {
                    return _loc_4;
                }
                _loc_3 = _loc_3 + 1;
            }
            return null;
        }// end function

        public function flushAtomData() : void
        {
            return;
        }// end function

        public function getAtomIndexAtPoint(param1:Number, param2:Number) : int;

        public function getAtomIndexAtCharIndex(param1:int) : int;

        public function getAtomBounds(param1:int) : Rectangle;

        public function getAtomBidiLevel(param1:int) : int;

        public function getAtomTextRotation(param1:int) : String;

        public function getAtomTextBlockBeginIndex(param1:int) : int;

        public function getAtomTextBlockEndIndex(param1:int) : int;

        public function getAtomCenter(param1:int) : Number;

        public function getAtomWordBoundaryOnLeft(param1:int) : Boolean;

        public function getAtomGraphic(param1:int) : DisplayObject;

        public function getBaselinePosition(param1:String) : Number;

        public function dump() : String;

        override public function set contextMenu(param1:ContextMenu) : void
        {
            Error.throwError(IllegalOperationError, 2181);
            return;
        }// end function

    }
}