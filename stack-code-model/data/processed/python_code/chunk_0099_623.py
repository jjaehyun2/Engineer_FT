package flash.geom
{
    import __AS3__.vec.*;

    public class Utils3D extends Object
    {

        public function Utils3D()
        {
            return;
        }// end function

        public static function projectVector(param1:Matrix3D, param2:Vector3D) : Vector3D;

        public static function projectVectors(param1:Matrix3D, param2:Vector.<Number>, param3:Vector.<Number>, param4:Vector.<Number>) : void;

        public static function pointTowards(param1:Number, param2:Matrix3D, param3:Vector3D, param4:Vector3D = null, param5:Vector3D = null) : Matrix3D;

    }
}