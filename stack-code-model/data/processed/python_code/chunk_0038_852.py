package flash.display
{
    import __AS3__.vec.*;

    final public class GraphicsTrianglePath extends Object implements IGraphicsPath, IGraphicsData
    {
        public var indices:Vector.<int>;
        public var vertices:Vector.<Number>;
        public var uvtData:Vector.<Number>;
        private var _culling:String;

        public function GraphicsTrianglePath(param1:Vector.<Number> = null, param2:Vector.<int> = null, param3:Vector.<Number> = null, param4:String = "none")
        {
            this.vertices = param1;
            this.indices = param2;
            this.uvtData = param3;
            this._culling = param4;
            if (param4 != TriangleCulling.NONE)
            {
            }
            if (param4 != TriangleCulling.POSITIVE)
            {
            }
            if (param4 != TriangleCulling.NEGATIVE)
            {
                Error.throwError(ArgumentError, 2008, "culling");
            }
            return;
        }// end function

        public function get culling() : String
        {
            return this._culling;
        }// end function

        public function set culling(param1:String) : void
        {
            if (param1 != TriangleCulling.NONE)
            {
            }
            if (param1 != TriangleCulling.POSITIVE)
            {
            }
            if (param1 != TriangleCulling.NEGATIVE)
            {
                Error.throwError(ArgumentError, 2008, "culling");
            }
            this._culling = param1;
            return;
        }// end function

    }
}