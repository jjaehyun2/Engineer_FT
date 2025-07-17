package flash.display
{
    import flash.geom.*;

    final public class GraphicsBitmapFill extends Object implements IGraphicsFill, IGraphicsData
    {
        public var bitmapData:BitmapData;
        public var matrix:Matrix;
        public var repeat:Boolean;
        public var smooth:Boolean;

        public function GraphicsBitmapFill(param1:BitmapData = null, param2:Matrix = null, param3:Boolean = true, param4:Boolean = false)
        {
            this.bitmapData = param1;
            this.matrix = param2;
            this.repeat = param3;
            this.smooth = param4;
            return;
        }// end function

    }
}