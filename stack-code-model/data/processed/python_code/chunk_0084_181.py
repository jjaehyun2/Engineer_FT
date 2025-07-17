package flash.external
{

    final public class ExternalInterface extends Object
    {
        public static var marshallExceptions:Boolean = false;

        public function ExternalInterface()
        {
            return;
        }// end function

        public static function get available() : Boolean;

        public static function addCallback(param1:String, param2:Function) : void
        {
            var hasNullCallback:Boolean;
            var wrapperClosure:Function;
            var functionName:* = param1;
            var closure:* = param2;
            if (available)
            {
                _initJS();
                hasNullCallback = closure == null;
                wrapperClosure = function (param1:String, param2:Array) : String
            {
                return _callIn(closure, param1, param2);
            }// end function
            ;
                _addCallback(functionName, wrapperClosure, hasNullCallback);
            }
            else
            {
                Error.throwError(Error, 2067);
            }
            return;
        }// end function

        public static function call(param1:String, ... args)
        {
            args = null;
            var _loc_4:* = null;
            var _loc_5:* = 0;
            var _loc_6:* = null;
            var _loc_7:* = null;
            var _loc_8:* = false;
            var _loc_9:* = null;
            if (available)
            {
                args = "";
                _initJS();
                args = args + "try { ";
                _loc_4 = null;
                if (activeX)
                {
                    _loc_4 = objectID;
                }
                if (_loc_4)
                {
                    args = args + ("document.getElementById(\"" + _loc_4 + "\").SetReturnValue(");
                }
                args = args + ("__flash__toXML(" + param1 + "(");
                _loc_5 = 0;
                while (_loc_5 < args.length)
                {
                    
                    if (_loc_5 != 0)
                    {
                        args = args + ",";
                    }
                    args = args + _toJS(args[_loc_5]);
                    _loc_5 = _loc_5 + 1;
                }
                args = args + ")) ";
                if (_loc_4)
                {
                    args = args + ")";
                }
                args = args + "; } catch (e) { ";
                if (_loc_4)
                {
                    if (marshallExceptions)
                    {
                        args = args + ("document.getElementById(\"" + _loc_4 + "\").SetReturnValue(\"<exception>\" + e + \"</exception>\");");
                    }
                    else
                    {
                        args = args + ("document.getElementById(\"" + _loc_4 + "\").SetReturnValue(\"<undefined/>\");");
                    }
                }
                else if (marshallExceptions)
                {
                    args = args + "\"<exception>\" + e + \"</exception>\";";
                }
                else
                {
                    args = args + "\"<undefined/>\";";
                }
                args = args + " }";
                _loc_6 = _evalJS(args);
                if (_loc_6 == null)
                {
                    _loc_7 = "<invoke name=\"" + param1 + "\" returntype=\"xml\">" + _argumentsToXML(args) + "</invoke>";
                    _loc_6 = _callOut(_loc_7);
                }
                if (_loc_6 == null)
                {
                    return null;
                }
                _loc_8 = XML.ignoreWhitespace;
                if (Capabilities.version.split(/[\ ,]/)[1] > 9)
                {
                    XML.ignoreWhitespace = false;
                }
                _loc_9 = XML(_loc_6);
                XML.ignoreWhitespace = _loc_8;
                return _toAS(_loc_9);
            }
            else
            {
                Error.throwError(Error, 2067);
            }
            return;
        }// end function

        private static function _initJS() : void;

        private static function _getPropNames(param1:Object) : Array;

        public static function get objectID() : String;

        private static function get activeX() : Boolean;

        private static function _addCallback(param1:String, param2:Function, param3:Boolean) : void;

        private static function _evalJS(param1:String) : String;

        private static function _callOut(param1:String) : String;

        private static function _callIn(param1:Function, param2:String, param3:Array) : String
        {
            arguments = new activation;
            var result:*;
            var closure:* = param1;
            var request:* = param2;
            var args:* = param3;
            var arguments:* = arguments;
            if ( != null)
            {
                try
                {
                    result = ExternalInterface.apply(null, );
                }
                catch (e:Error)
                {
                    if (marshallExceptions)
                    {
                        result = e;
                    }
                    else
                    {
                        throw e;
                    }
                }
                return _toJS();
            }
            var oldIgnoreWhitespace:* = XML.ignoreWhitespace;
            XML.ignoreWhitespace = false;
            var xml:* = XML();
            XML.ignoreWhitespace = ;
            try
            {
                result = ExternalInterface.apply(null, _argumentsToAS(ExternalInterface.arguments));
            }
            catch (e:Error)
            {
                if (marshallExceptions)
                {
                    result = e;
                }
                else
                {
                    throw e;
                }
            }
            return ExternalInterface.@returntype == "javascript" ? (_toJS()) : (_toXML());
        }// end function

        private static function _arrayToXML(param1:Array) : String
        {
            var _loc_2:* = "<array>";
            var _loc_3:* = 0;
            while (_loc_3 < param1.length)
            {
                
                _loc_2 = _loc_2 + ("<property id=\"" + _loc_3 + "\">" + _toXML(param1[_loc_3]) + "</property>");
                _loc_3 = _loc_3 + 1;
            }
            return _loc_2 + "</array>";
        }// end function

        private static function _argumentsToXML(param1:Array) : String
        {
            var _loc_2:* = "<arguments>";
            var _loc_3:* = 0;
            while (_loc_3 < param1.length)
            {
                
                _loc_2 = _loc_2 + _toXML(param1[_loc_3]);
                _loc_3 = _loc_3 + 1;
            }
            return _loc_2 + "</arguments>";
        }// end function

        private static function _objectToXML(param1) : String
        {
            var _loc_3:* = null;
            var _loc_2:* = "<object>";
            for (_loc_3 in param1)
            {
                
                _loc_2 = _loc_2 + ("<property id=\"" + _loc_3 + "\">" + _toXML(_loc_5[_loc_3]) + "</property>");
            }
            return _loc_2 + "</object>";
        }// end function

        private static function _escapeXML(param1:String) : String
        {
            return param1.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&apos;");
        }// end function

        private static function _toXML(param1) : String
        {
            var _loc_2:* = typeof(param1);
            if (_loc_2 == "string")
            {
                return "<string>" + _escapeXML(param1) + "</string>";
            }
            if (_loc_2 == "undefined")
            {
                return "<undefined/>";
            }
            if (_loc_2 == "number")
            {
                return "<number>" + param1 + "</number>";
            }
            if (param1 == null)
            {
                return "<null/>";
            }
            if (_loc_2 == "boolean")
            {
                return param1 ? ("<true/>") : ("<false/>");
            }
            else
            {
                if (param1.hasOwnProperty("length"))
                {
                    return _arrayToXML(param1);
                }
                if (param1 is Date)
                {
                    return "<date>" + param1.time + "</date>";
                }
                if (param1 is Error)
                {
                }
                if (marshallExceptions)
                {
                    return "<exception>" + param1 + "</exception>";
                }
                if (_loc_2 == "object")
                {
                    return _objectToXML(param1);
                }
                return "<null/>";
            }
        }// end function

        private static function _objectToAS(param1:Object)
        {
            var _loc_3:* = null;
            var _loc_2:* = {};
            for each (_loc_3 in param1.property)
            {
                
                _loc_2[_loc_3.@id] = _toAS(_loc_3.children());
            }
            return _loc_2;
        }// end function

        private static function _arrayToAS(param1:Object)
        {
            var _loc_3:* = null;
            var _loc_2:* = [];
            for each (_loc_3 in param1.children())
            {
                
                _loc_2[_loc_3.@id] = _toAS(_loc_3.children());
            }
            return _loc_2;
        }// end function

        private static function _toAS(param1:Object)
        {
            var _loc_2:* = param1.name();
            if (_loc_2 == "number")
            {
                return Number(param1.children());
            }
            if (_loc_2 == "string")
            {
                return String(param1.children());
            }
            if (_loc_2 == "false")
            {
                return false;
            }
            if (_loc_2 == "true")
            {
                return true;
            }
            if (_loc_2 == "null")
            {
                return null;
            }
            if (_loc_2 == "undefined")
            {
                return undefined;
            }
            if (_loc_2 == "date")
            {
                return new Date(Number(param1.children()));
            }
            if (_loc_2 == "object")
            {
                return _objectToAS(param1);
            }
            if (_loc_2 == "array")
            {
                return _arrayToAS(param1);
            }
            if (_loc_2 == "class")
            {
                return getDefinitionByName(String(param1.children()));
            }
            if (_loc_2 == "exception")
            {
            }
            if (marshallExceptions)
            {
                throw new Error(param1.children());
            }
            return undefined;
        }// end function

        private static function _argumentsToAS(param1) : Array
        {
            var _loc_3:* = null;
            var _loc_2:* = [];
            for each (_loc_3 in param1.children())
            {
                
                _loc_2.push(_toAS(_loc_3));
            }
            return _loc_2;
        }// end function

        private static function _arrayToJS(param1:Array) : String
        {
            var _loc_2:* = "[";
            var _loc_3:* = 0;
            while (_loc_3 < param1.length)
            {
                
                if (_loc_3 != 0)
                {
                    _loc_2 = _loc_2 + ",";
                }
                _loc_2 = _loc_2 + _toJS(param1[_loc_3]);
                _loc_3 = _loc_3 + 1;
            }
            return _loc_2 + "]";
        }// end function

        private static function _objectToJS(param1) : String
        {
            var _loc_2:* = _getPropNames(param1);
            var _loc_3:* = "({";
            var _loc_4:* = 0;
            while (_loc_4 < _loc_2.length)
            {
                
                if (_loc_4 > 0)
                {
                    _loc_3 = _loc_3 + ",";
                }
                _loc_3 = _loc_3 + (_loc_2[_loc_4] + ":" + _toJS(param1[_loc_2[_loc_4]]));
                _loc_4 = _loc_4 + 1;
            }
            return _loc_3 + "})";
        }// end function

        private static function _quotedStringFromError(param1:Error) : String;

        private static function _quotedStringFromString(param1:String) : String;

        private static function _toJS(param1) : String
        {
            if (param1 is Error)
            {
            }
            if (marshallExceptions)
            {
                return "throw " + _quotedStringFromError(param1);
            }
            if (typeof(param1) == "string")
            {
                return _quotedStringFromString(param1);
            }
            if (param1 === null)
            {
                return "null";
            }
            if (param1 is Date)
            {
                return "new Date (" + param1.time + ")";
            }
            if (typeof(param1) == "object")
            {
                if (param1 is Array)
                {
                    return _arrayToJS(param1);
                }
                return _objectToJS(param1);
            }
            else
            {
                return String(param1);
            }
        }// end function

    }
}