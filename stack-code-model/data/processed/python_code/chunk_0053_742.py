package flash.display3D.textures
{
    import flash.display.*;
    import flash.utils.*;

    final public class CubeTexture extends TextureBase
    {

        public function CubeTexture()
        {
            return;
        }// end function

        public function uploadFromBitmapData(param1:BitmapData, param2:uint, param3:uint = 0) : void;

        public function uploadFromByteArray(param1:ByteArray, param2:uint, param3:uint, param4:uint = 0) : void;

        public function uploadCompressedTextureFromByteArray(param1:ByteArray, param2:uint, param3:Boolean = false) : void;

    }
}