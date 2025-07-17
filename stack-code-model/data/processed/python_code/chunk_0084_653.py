package com.hurlant.crypto.symmetric {
    import flash.utils.*;

    public class OFBMode extends IVMode implements IMode {

        public function OFBMode(_arg1:ISymmetricKey, _arg2:IPad=null){
            super(_arg1, null);
        }
        public function toString():String{
            return ((key.toString() + "-ofb"));
        }
        private function core(_arg1:ByteArray, _arg2:ByteArray):void{
            var _local3:uint;
            var _local4:ByteArray;
            var _local5:uint;
            var _local6:uint;
            var _local7:uint;
            _local3 = _arg1.length;
            _local4 = new ByteArray();
            _local5 = 0;
            while (_local5 < _arg1.length) {
                key.encrypt(_arg2);
                _local4.position = 0;
                _local4.writeBytes(_arg2);
                _local6 = (((_local5 + blockSize))<_local3) ? blockSize : (_local3 - _local5);
                _local7 = 0;
                while (_local7 < _local6) {
                    _arg1[(_local5 + _local7)] = (_arg1[(_local5 + _local7)] ^ _arg2[_local7]);
                    _local7++;
                };
                _arg2.position = 0;
                _arg2.writeBytes(_local4);
                _local5 = (_local5 + blockSize);
            };
        }
        public function decrypt(_arg1:ByteArray):void{
            var _local2:ByteArray;
            _local2 = getIV4d();
            core(_arg1, _local2);
        }
        public function encrypt(_arg1:ByteArray):void{
            var _local2:ByteArray;
            _local2 = getIV4e();
            core(_arg1, _local2);
        }

    }
}//package com.hurlant.crypto.symmetric