package com.hurlant.crypto.symmetric {
    import flash.utils.*;

    public class CTRMode extends IVMode implements IMode {

        public function CTRMode(_arg1:ISymmetricKey, _arg2:IPad=null){
            super(_arg1, _arg2);
        }
        public function toString():String{
            return ((key.toString() + "-ctr"));
        }
        private function core(_arg1:ByteArray, _arg2:ByteArray):void{
            var _local3:ByteArray;
            var _local4:ByteArray;
            var _local5:uint;
            var _local6:uint;
            _local3 = new ByteArray();
            _local4 = new ByteArray();
            _local3.writeBytes(_arg2);
            _local5 = 0;
            while (_local5 < _arg1.length) {
                _local4.position = 0;
                _local4.writeBytes(_local3);
                key.encrypt(_local4);
                _local6 = 0;
                while (_local6 < blockSize) {
                    _arg1[(_local5 + _local6)] = (_arg1[(_local5 + _local6)] ^ _local4[_local6]);
                    _local6++;
                };
                _local6 = (blockSize - 1);
                while (_local6 >= 0) {
                    var _local7 = _local3;
                    var _local8 = _local6;
                    var _local9 = (_local7[_local8] + 1);
                    _local7[_local8] = _local9;
                    if (_local3[_local6] != 0){
                        break;
                    };
                    _local6--;
                };
                _local5 = (_local5 + blockSize);
            };
        }
        public function decrypt(_arg1:ByteArray):void{
            var _local2:ByteArray;
            _local2 = getIV4d();
            core(_arg1, _local2);
            padding.unpad(_arg1);
        }
        public function encrypt(_arg1:ByteArray):void{
            var _local2:ByteArray;
            padding.pad(_arg1);
            _local2 = getIV4e();
            core(_arg1, _local2);
        }

    }
}//package com.hurlant.crypto.symmetric