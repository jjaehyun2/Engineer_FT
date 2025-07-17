package com.hurlant.crypto.symmetric {
    import flash.utils.*;
    import com.hurlant.util.*;

    public class TripleDESKey extends DESKey {

        protected var decKey2:Array;
        protected var decKey3:Array;
        protected var encKey2:Array;
        protected var encKey3:Array;

        public function TripleDESKey(_arg1:ByteArray){
            super(_arg1);
            encKey2 = generateWorkingKey(false, _arg1, 8);
            decKey2 = generateWorkingKey(true, _arg1, 8);
            if (_arg1.length > 16){
                encKey3 = generateWorkingKey(true, _arg1, 16);
                decKey3 = generateWorkingKey(false, _arg1, 16);
            } else {
                encKey3 = encKey;
                decKey3 = decKey;
            };
        }
        override public function decrypt(_arg1:ByteArray, _arg2:uint=0):void{
            desFunc(decKey3, _arg1, _arg2, _arg1, _arg2);
            desFunc(decKey2, _arg1, _arg2, _arg1, _arg2);
            desFunc(decKey, _arg1, _arg2, _arg1, _arg2);
        }
        override public function encrypt(_arg1:ByteArray, _arg2:uint=0):void{
            desFunc(encKey, _arg1, _arg2, _arg1, _arg2);
            desFunc(encKey2, _arg1, _arg2, _arg1, _arg2);
            desFunc(encKey3, _arg1, _arg2, _arg1, _arg2);
        }
        override public function dispose():void{
            var _local1:uint;
            super.dispose();
            _local1 = 0;
            if (encKey2 != null){
                _local1 = 0;
                while (_local1 < encKey2.length) {
                    encKey2[_local1] = 0;
                    _local1++;
                };
                encKey2 = null;
            };
            if (encKey3 != null){
                _local1 = 0;
                while (_local1 < encKey3.length) {
                    encKey3[_local1] = 0;
                    _local1++;
                };
                encKey3 = null;
            };
            if (decKey2 != null){
                _local1 = 0;
                while (_local1 < decKey2.length) {
                    decKey2[_local1] = 0;
                    _local1++;
                };
                decKey2 = null;
            };
            if (decKey3 != null){
                _local1 = 0;
                while (_local1 < decKey3.length) {
                    decKey3[_local1] = 0;
                    _local1++;
                };
                decKey3 = null;
            };
            Memory.gc();
        }
        override public function toString():String{
            return ("3des");
        }

    }
}//package com.hurlant.crypto.symmetric