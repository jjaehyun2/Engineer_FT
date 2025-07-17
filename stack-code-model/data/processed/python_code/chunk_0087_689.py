package com.hurlant.crypto.symmetric {
    import flash.utils.*;

    public interface ICipher {

        function encrypt(_arg1:ByteArray):void;
        function dispose():void;
        function getBlockSize():uint;
        function toString():String;
        function decrypt(_arg1:ByteArray):void;

    }
}//package com.hurlant.crypto.symmetric