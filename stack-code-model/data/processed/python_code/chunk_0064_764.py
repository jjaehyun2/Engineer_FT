package flash.system
{

    final public class Security extends Object
    {
        public static const REMOTE:String = "remote";
        public static const LOCAL_WITH_FILE:String = "localWithFile";
        public static const LOCAL_WITH_NETWORK:String = "localWithNetwork";
        public static const LOCAL_TRUSTED:String = "localTrusted";
        public static const APPLICATION:String = "application";

        public function Security()
        {
            return;
        }// end function

        public static function allowDomain(... args) : void;

        public static function allowInsecureDomain(... args) : void;

        public static function loadPolicyFile(param1:String) : void;

        public static function get exactSettings() : Boolean;

        public static function set exactSettings(param1:Boolean) : void;

        public static function get disableAVM1Loading() : Boolean;

        public static function set disableAVM1Loading(param1:Boolean) : void;

        static function duplicateSandboxBridgeInputArguments(param1:Object, param2:Array) : Array;

        static function duplicateSandboxBridgeOutputArgument(param1:Object, param2);

        private static function createSandboxBridgeProxyFunction(param1:Object, param2:Object, param3:Object, param4:Object) : Object
        {
            var targetFunc:* = param1;
            var targetObj:* = param2;
            var srcToplevel:* = param3;
            var destToplevel:* = param4;
            return function (... args)
            {
                args = duplicateSandboxBridgeInputArguments(srcToplevel, args);
                var _loc_3:* = targetFunc.apply(targetObj, args);
                return duplicateSandboxBridgeOutputArgument(destToplevel, _loc_3);
            }// end function
            ;
        }// end function

        public static function showSettings(param1:String = "default") : void;

        public static function get sandboxType() : String;

        public static function get pageDomain() : String;

    }
}