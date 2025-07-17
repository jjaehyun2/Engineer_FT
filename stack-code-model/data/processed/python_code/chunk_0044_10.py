package flash.utils
{

    class ObjectInput extends Object implements IDataInput
    {

        function ObjectInput()
        {
            return;
        }// end function

        public function readBytes(param1:ByteArray, param2:uint = 0, param3:uint = 0) : void;

        public function readBoolean() : Boolean;

        public function readByte() : int;

        public function readUnsignedByte() : uint;

        public function readShort() : int;

        public function readUnsignedShort() : uint;

        public function readInt() : int;

        public function readUnsignedInt() : uint;

        public function readFloat() : Number;

        public function readDouble() : Number;

        public function readMultiByte(param1:uint, param2:String) : String;

        public function readUTF() : String;

        public function readUTFBytes(param1:uint) : String;

        public function get bytesAvailable() : uint;

        public function readObject();

        public function get objectEncoding() : uint;

        public function set objectEncoding(param1:uint) : void;

        public function get endian() : String;

        public function set endian(param1:String) : void;

    }
}