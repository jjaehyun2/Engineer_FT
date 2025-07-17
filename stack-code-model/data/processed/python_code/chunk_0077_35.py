/**
 * Created by Blake McBride on 9/27/15.
 */
package com.arahant.core.util {

    import flash.external.ExternalInterface;
    import flash.utils.describeType;
    import flash.utils.getQualifiedClassName;

    public class Debugger {

        /**
         * Log levels
         *
         * 0 = no logging
         * 1 = only error (default)
         * 2 = only error and warn
         * 3 = error, warn, log, and info
         */
        private static var defaultLevel:int = 1;

        private static var moduleLevels:Object = {};

        public static function getModuleLevel(module:String):int {
            if (moduleLevels[module] == undefined)
                return defaultLevel;
            return moduleLevels[module];
        }

        public static function setModuleLevel(module:String, val:int):void {
            moduleLevels[module] = val;
        }

        public static function info(module:String, location:String, msg:String=null):void {
            if (getModuleLevel(module) >= 3)
                ExternalInterface.call("console.info", format(module, location, msg));
        }

        public static function log(module:String, location:String, msg:String=null):void {
            if (getModuleLevel(module) >= 3)
                ExternalInterface.call("console.log", format(module, location, msg));
        }

        public static function warn(module:String, location:String, msg:String=null):void {
            if (getModuleLevel(module) >= 2)
                ExternalInterface.call("console.warn", format(module, location, msg));
        }

        public static function error(module:String, location:String, msg:String=null):void {
            if (getModuleLevel(module) >= 1)
                ExternalInterface.call("console.error", format(module, location, msg));
        }

        private static function out(location:String, msg:String=null):void {
            ExternalInterface.call("console.error", format("", location, msg));
        }

        private static function format(module:String, location:String, msg:String):String {
            if (location == null) {
                location = "";
            }
            if (module == "")
                if (msg == null  ||  msg == "")
                    return location;
                else
                    return location + ": " + msg;
            else if (msg == null  ||  msg == "")
                return module + ' - ' + location;
            else
                return module + ' - ' + location + ": " + msg;
        }

        private static function repeatString(string:String, numTimes:uint):String
        {
            var output:String = "";
            for(var i:uint = 0; i < numTimes; i++)
                output += string;
            return output;
        }

        private static function objectLength(obj:Object):int {
            var n:int = 0;
            var longType:String = getQualifiedClassName(obj);
            if (longType == 'Array'  ||  longType == 'Object') {
                for (var id:String in obj) {
                    n++;
                }
            } else {
                var iXML:XML = describeType(obj);
                for each (var vd:XML in iXML..variable) {
                    n++;
                }
            }
            return n;
        }

        private static function displayObject(obj:Object, level:int=1):void {
            var lead:String = repeatString(' ', level*4);
            var longType:String = getQualifiedClassName(obj);
            var out:String;
            var val:Object;
            var len:int;
            if ('object' != typeof obj) {
                Debugger.out(out + quoteString(obj));
            } else if (longType == 'Array'  ||  longType == 'Object') {
                for (var id:String in obj) {
                    val = obj[id];
                    out = lead + id + ' = ';
                    if ('object' == typeof val) {
                        len = objectLength(val);
                        Debugger.out(out + ' [' + getQualifiedClassName(val) + ' length ' + len + ']');
                        if (len > 0) {
                            displayObject(val, level + 1);
                        }
                    } else {
                        Debugger.out(out + quoteString(val));
                    }
                }
            } else {
                var iXML:XML = describeType(obj);
                for each (var vd:XML in iXML..variable) {
                    var name:String = vd.@name;
                    val = obj[name];
                    out = lead + name + ' = ';
                    if ('object' == typeof val) {
                        len = objectLength(val);
                        Debugger.out(out + ' [' + getQualifiedClassName(val) + ' length ' + len + ']');
                        if (len > 0) {
                            displayObject(val, level + 1);
                        }
                    } else {
                        Debugger.out(out + quoteString(val));
                    }
                }
            }
        }

        private static function quoteString(x:Object):String {
            if ('string' == typeof x) {
                return "'" + x + "'";
            }
            return String(x);
        }

        public static function value(module:String, label:String, name:String, val:Object):void {
            if (getModuleLevel(module) < 3)
                return;
            if (val == null) {
                Debugger.error(module, label, name + ' = null');
            } else if ('object' == typeof val) {
                var n:int = objectLength(val);
                Debugger.error(module, label, name + ' [' + getQualifiedClassName(val) + ' length ' + n + ']');
                displayObject(val, 1);
            } else {
                Debugger.error(module, label, name + ' = (' + getQualifiedClassName(val) + ') ' + quoteString(val));
            }
        }

        /**
         * This is designed to be a replacement for:
         *         throw new Error(msg)
         *
         * @param module
         * @param location
         * @param msg
         */
        public static function throwError(module:String, location:String, msg:String):void {
            Debugger.error(module, location, msg);
            throw new Error(msg);
        }

    }

}