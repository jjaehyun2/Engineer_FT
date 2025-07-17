package flash.utils
{

    class ObjectOutput extends Object implements IDataOutput
    {

        function ObjectOutput()
        {
            return;
        }// end function

        public function writeBytes(param1:ByteArray, param2:uint = 0, param3:uint = 0) : void;

        public function writeBoolean(param1:Boolean) : void;

        public function writeByte(param1:int) : void;

        public function writeShort(param1:int) : void;

        public function writeInt(param1:int) : void;

        public function writeUnsignedInt(param1:uint) : void;

        public function writeFloat(param1:Number) : void;

        public function writeDouble(param1:Number) : void;

        public function writeMultiByte(param1:String, param2:String) : void;

        public function writeUTF(param1:String) : void;

        public function writeUTFBytes(param1:String) : void;

        public function writeObject(param1) : void;

        public function get objectEncoding() : uint;

        public function set objectEncoding(param1:uint) : void;

        public function get endian() : String;

        public function set endian(param1:String) : void;

    }
}