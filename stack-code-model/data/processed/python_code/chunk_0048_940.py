package flash.geom
{
    import flash.display.*;

    public class Transform extends Object
    {

        public function Transform(param1:DisplayObject)
        {
            this.ctor(param1);
            return;
        }// end function

        public function get matrix() : Matrix;

        public function set matrix(param1:Matrix) : void;

        public function get colorTransform() : ColorTransform;

        public function set colorTransform(param1:ColorTransform) : void;

        public function get concatenatedMatrix() : Matrix;

        public function get concatenatedColorTransform() : ColorTransform;

        public function get pixelBounds() : Rectangle;

        private function ctor(param1:DisplayObject) : void;

        public function get matrix3D() : Matrix3D;

        public function set matrix3D(param1:Matrix3D);

        public function getRelativeMatrix3D(param1:DisplayObject) : Matrix3D;

        public function get perspectiveProjection() : PerspectiveProjection;

        public function set perspectiveProjection(param1:PerspectiveProjection) : void;

    }
}