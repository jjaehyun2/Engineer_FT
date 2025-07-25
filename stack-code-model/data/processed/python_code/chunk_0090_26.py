﻿package com.hurlant.crypto.hash {

    public class SHA1 extends SHABase implements IHash {

        public static const HASH_SIZE:int = 20;

        private function ft(_arg1:uint, _arg2:uint, _arg3:uint, _arg4:uint):uint{
            if (_arg1 < 20){
                return (((_arg2 & _arg3) | (~(_arg2) & _arg4)));
            };
            if (_arg1 < 40){
                return (((_arg2 ^ _arg3) ^ _arg4));
            };
            if (_arg1 < 60){
                return ((((_arg2 & _arg3) | (_arg2 & _arg4)) | (_arg3 & _arg4)));
            };
            return (((_arg2 ^ _arg3) ^ _arg4));
        }
        private function kt(_arg1:uint):uint{
            return (((_arg1)<20) ? 1518500249 : ((_arg1)<40) ? 1859775393 : ((_arg1)<60) ? 2400959708 : 3395469782);
        }
        override public function toString():String{
            return ("sha1");
        }
        override public function getHashSize():uint{
            return (HASH_SIZE);
        }
        private function rol(_arg1:uint, _arg2:uint):uint{
            return (((_arg1 << _arg2) | (_arg1 >>> (32 - _arg2))));
        }
        override protected function core(_arg1:Array, _arg2:uint):Array{
            var _local3:Array;
            var _local4:uint;
            var _local5:uint;
            var _local6:uint;
            var _local7:uint;
            var _local8:uint;
            var _local9:uint;
            var _local10:uint;
            var _local11:uint;
            var _local12:uint;
            var _local13:uint;
            var _local14:uint;
            var _local15:uint;
            var _local16:uint;
            _arg1[(_arg2 >> 5)] = (_arg1[(_arg2 >> 5)] | (128 << (24 - (_arg2 % 32))));
            _arg1[((((_arg2 + 64) >> 9) << 4) + 15)] = _arg2;
            _local3 = [];
            _local4 = 1732584193;
            _local5 = 4023233417;
            _local6 = 2562383102;
            _local7 = 271733878;
            _local8 = 3285377520;
            _local9 = 0;
            while (_local9 < _arg1.length) {
                _local10 = _local4;
                _local11 = _local5;
                _local12 = _local6;
                _local13 = _local7;
                _local14 = _local8;
                _local15 = 0;
                while (_local15 < 80) {
                    if (_local15 < 16){
                        _local3[_local15] = ((_arg1[(_local9 + _local15)]) || (0));
                    } else {
                        _local3[_local15] = rol((((_local3[(_local15 - 3)] ^ _local3[(_local15 - 8)]) ^ _local3[(_local15 - 14)]) ^ _local3[(_local15 - 16)]), 1);
                    };
                    _local16 = ((((rol(_local4, 5) + ft(_local15, _local5, _local6, _local7)) + _local8) + _local3[_local15]) + kt(_local15));
                    _local8 = _local7;
                    _local7 = _local6;
                    _local6 = rol(_local5, 30);
                    _local5 = _local4;
                    _local4 = _local16;
                    _local15++;
                };
                _local4 = (_local4 + _local10);
                _local5 = (_local5 + _local11);
                _local6 = (_local6 + _local12);
                _local7 = (_local7 + _local13);
                _local8 = (_local8 + _local14);
                _local9 = (_local9 + 16);
            };
            return ([_local4, _local5, _local6, _local7, _local8]);
        }

    }
}//package com.hurlant.crypto.hash