package flash.filters
{
    import flash.display.*;
    import flash.geom.*;

    public class ShaderFilter extends BitmapFilter
    {

        public function ShaderFilter(param1:Shader = null)
        {
            if (param1)
            {
                this.shader = param1;
            }
            return;
        }// end function

        public function get shader() : Shader;

        public function set shader(param1:Shader) : void;

        public function get leftExtension() : int
        {
            return int(this._extendBy.left);
        }// end function

        public function set leftExtension(param1:int) : void
        {
            var _loc_2:* = this._extendBy;
            _loc_2.left = Number(param1);
            this._extendBy = _loc_2;
            return;
        }// end function

        public function get topExtension() : int
        {
            return int(this._extendBy.top);
        }// end function

        public function set topExtension(param1:int) : void
        {
            var _loc_2:* = this._extendBy;
            _loc_2.top = Number(param1);
            this._extendBy = _loc_2;
            return;
        }// end function

        public function get rightExtension() : int
        {
            return int(this._extendBy.right);
        }// end function

        public function set rightExtension(param1:int) : void
        {
            var _loc_2:* = this._extendBy;
            _loc_2.right = Number(param1);
            this._extendBy = _loc_2;
            return;
        }// end function

        public function get bottomExtension() : int
        {
            return int(this._extendBy.bottom);
        }// end function

        public function set bottomExtension(param1:int) : void
        {
            var _loc_2:* = this._extendBy;
            _loc_2.bottom = Number(param1);
            this._extendBy = _loc_2;
            return;
        }// end function

        private function get _extendBy() : Rectangle;

        private function set _extendBy(param1:Rectangle) : void;

    }
}