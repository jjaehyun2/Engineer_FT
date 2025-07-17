package com.hurlant.crypto.symmetric {
    import flash.utils.*;

    public class CBCMode extends IVMode implements IMode {

        public function CBCMode(_arg1:ISymmetricKey, _arg2:IPad=null){
            super(_arg1, _arg2);
        }
        public function toString():String{
            return ((key.toString() + "-cbc"));
        }
        public function decrypt(_arg1:ByteArray):void{
            var _local2:ByteArray;
            var _local3:ByteArray;
            var _local4:uint;
            var _local5:uint;
            _local2 = getIV4d();
            _local3 = new ByteArray();
            _local4 = 0;
            while (_local4 < _arg1.length) {
                _local3.position = 0;
                _local3.writeBytes(_arg1, _local4, blockSize);
                key.decrypt(_arg1, _local4);
                _local5 = 0;
                while (_local5 < blockSize) {
                    _arg1[(_local4 + _local5)] = (_arg1[(_local4 + _local5)] ^ _local2[_local5]);
                    _local5++;
                };
                _local2.position = 0;
                _local2.writeBytes(_local3, 0, blockSize);
                _local4 = (_local4 + blockSize);
            };
            padding.unpad(_arg1);
        }
        public function encrypt(_arg1:ByteArray):void{
            var _local2:ByteArray;
            var _local3:uint;
            var _local4:uint;
            padding.pad(_arg1);
            _local2 = getIV4e();
            _local3 = 0;
            while (_local3 < _arg1.length) {
                _local4 = 0;
                while (_local4 < blockSize) {
                    _arg1[(_local3 + _local4)] = (_arg1[(_local3 + _local4)] ^ _local2[_local4]);
                    _local4++;
                };
                key.encrypt(_arg1, _local3);
                _local2.position = 0;
                _local2.writeBytes(_arg1, _local3, blockSize);
                _local3 = (_local3 + blockSize);
            };
        }

    }
}//package com.hurlant.crypto.symmetric