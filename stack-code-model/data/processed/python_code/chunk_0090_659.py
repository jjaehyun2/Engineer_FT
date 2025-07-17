package flash.net
{
    import flash.events.*;

    public class NetConnection extends EventDispatcher
    {
        private static const kConnect:uint = 0;
        private static const kClose:uint = 1;
        private static const kCall:uint = 2;
        private static const kAddHeader:uint = 3;
        private static const kGetConnectedProxyType:uint = 4;
        private static const kGetUsingTLS:uint = 5;
        private static const kGetProtocol:uint = 6;
        private static const kGetNearID:uint = 7;
        private static const kGetFarID:uint = 8;
        private static const kGetNearNonce:uint = 9;
        private static const kGetFarNonce:uint = 10;

        public function NetConnection()
        {
            return;
        }// end function

        public function get connected() : Boolean;

        public function get uri() : String;

        public function close() : void
        {
            this.invoke(kClose);
            return;
        }// end function

        public function addHeader(param1:String, param2:Boolean = false, param3:Object = null) : void
        {
            var _loc_4:* = new Array(param1, param2, param3);
            this.invokeWithArgsArray(kAddHeader, _loc_4);
            return;
        }// end function

        public function call(param1:String, param2:Responder, ... args) : void
        {
            args.unshift(param1, param2);
            this.invokeWithArgsArray(kCall, args);
            return;
        }// end function

        public function connect(param1:String, ... args) : void;

        public function get client() : Object;

        public function set client(param1:Object) : void;

        public function get objectEncoding() : uint;

        public function set objectEncoding(param1:uint) : void;

        public function get proxyType() : String;

        public function set proxyType(param1:String) : void;

        public function get connectedProxyType() : String;

        public function get usingTLS() : Boolean;

        public function get protocol() : String;

        public function get maxPeerConnections() : uint;

        public function set maxPeerConnections(param1:uint) : void;

        public function get nearID() : String;

        public function get farID() : String;

        public function get nearNonce() : String;

        public function get farNonce() : String;

        public function get unconnectedPeerStreams() : Array;

        private function invoke(param1:uint, ... args);

        private function invokeWithArgsArray(param1:uint, param2:Array);

        public static function get defaultObjectEncoding() : uint;

        public static function set defaultObjectEncoding(param1:uint) : void;

    }
}