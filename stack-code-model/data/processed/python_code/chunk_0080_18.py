package flash.desktop
{
    import flash.utils.*;

    public class Clipboard extends Object
    {
        private static const LIFETIME_ERROR:String = "Attempt to access a dead clipboard";
        private static const READ_ACCESS_ERROR:String = "Reading from clipboard not permitted in this context";
        private static const WRITE_ACCESS_ERROR:String = "Writing to clipboard not permitted in this context";
        private static var _fromFlash:Dictionary;
        private static var _toFlash:Dictionary;
        private static var _wasFormatMapInitialized:Boolean = false;

        public function Clipboard()
        {
            initFormatMap();
            return;
        }// end function

        public function get formats() : Array;

        public function clear() : void;

        public function clearData(param1:String) : void;

        public function setData(param1:String, param2:Object, param3:Boolean = true) : Boolean
        {
            var _loc_4:* = param1 == null;
            if (!_loc_4)
            {
            }
            if (param2 == null)
            {
                if (this.swfVersion >= 10)
                {
                    Error.throwError(TypeError, 2007, _loc_4 ? ("format") : ("data"));
                }
                else if (_loc_4)
                {
                    return false;
                }
            }
            if (param1 != this.URL_FORMAT)
            {
            }
            if (param1 != this.FILE_LIST_FORMAT)
            {
            }
            if (param1 != this.BITMAP_FORMAT)
            {
            }
            if (param1 == this.FILE_PROMISE_LIST_FORMAT)
            {
                return false;
            }
            this.checkAccess(false, true);
            return this.convertFlashFormat(param1, param2, param3);
        }// end function

        public function setDataHandler(param1:String, param2:Function, param3:Boolean = true) : Boolean
        {
            var toNative:*;
            var format:* = param1;
            var handler:* = param2;
            var serializable:* = param3;
            if (this.swfVersion >= 10)
            {
                if (format == null)
                {
                    Error.throwError(TypeError, 2007, "format");
                }
                if (handler == null)
                {
                    Error.throwError(TypeError, 2007, "handler");
                }
            }
            if (format != this.URL_FORMAT)
            {
            }
            if (format != this.FILE_LIST_FORMAT)
            {
            }
            if (format != this.BITMAP_FORMAT)
            {
            }
            if (format == this.FILE_PROMISE_LIST_FORMAT)
            {
                return false;
            }
            this.checkAccess(false, true);
            var fullHandler:* = function () : void
            {
                var _loc_1:* = handler() as Object;
                setHandlerStoringData(true);
                setData(format, _loc_1, serializable);
                setHandlerStoringData(false);
                return;
            }// end function
            ;
            if (isSystemFormat(format))
            {
                toNative = _fromFlash[format];
                if (!toNative)
                {
                    return false;
                }
                this.nativeSetHandler(format, fullHandler);
            }
            else
            {
                this.nativeSetHandler(this.REFERENCE_PREFIX + format, fullHandler);
                if (serializable)
                {
                    this.nativeSetHandler(this.SERIALIZATION_PREFIX + format, fullHandler);
                }
            }
            return true;
        }// end function

        public function getData(param1:String, param2:String = "originalPreferred") : Object
        {
            var _loc_3:* = null;
            this.checkAccess(true, false);
            _loc_3 = this.convertNativeFormat(param1);
            if (_loc_3)
            {
                return _loc_3;
            }
            switch(param2)
            {
                case this.ORIGINAL_PREFERRED:
                {
                    _loc_3 = this.getOriginal(param1);
                    if (_loc_3 == undefined)
                    {
                        _loc_3 = this.getClone(param1);
                    }
                    return _loc_3;
                }
                case this.ORIGINAL_ONLY:
                {
                    return this.getOriginal(param1);
                }
                case this.CLONE_PREFERRED:
                {
                    _loc_3 = this.getClone(param1);
                    if (_loc_3 == undefined)
                    {
                        _loc_3 = this.getOriginal(param1);
                    }
                    return _loc_3;
                }
                case this.CLONE_ONLY:
                {
                    return this.getClone(param1);
                }
                default:
                {
                    throw new Error("Illegal value for transferMode: " + param2);
                    break;
                }
            }
        }// end function

        public function hasFormat(param1:String) : Boolean
        {
            this.checkAccess(false, false);
            return this.formats.indexOf(param1) != -1;
        }// end function

        private function getOriginal(param1:String) : Object
        {
            return this.convertNativeFormat(this.REFERENCE_PREFIX + param1);
        }// end function

        private function getClone(param1:String) : Object
        {
            return this.convertNativeFormat(this.SERIALIZATION_PREFIX + param1);
        }// end function

        private function get alive() : Boolean;

        private function get canReadContents() : Boolean;

        private function get canWriteContents() : Boolean;

        private function checkAccess(param1:Boolean, param2:Boolean) : void
        {
            if (!this.alive)
            {
                throw new IllegalOperationError(LIFETIME_ERROR);
            }
            if (param1)
            {
            }
            if (!this.canReadContents)
            {
                throw new SecurityError(READ_ACCESS_ERROR);
            }
            if (param2)
            {
            }
            if (!this.canWriteContents)
            {
                throw new SecurityError(WRITE_ACCESS_ERROR);
            }
            return;
        }// end function

        private function nativeSetHandler(param1:String, param2:Function) : void;

        private function getObjectReference(param1:String) : Object;

        private function putObjectReference(param1:String, param2:Object) : void;

        private function getDeserialization(param1:String) : Object
        {
            var _loc_2:* = this.getByteArray(param1);
            if (!_loc_2)
            {
                return null;
            }
            return _loc_2.readObject();
        }// end function

        private function putSerialization(param1:String, param2:Object) : void
        {
            var _loc_3:* = new ByteArray();
            _loc_3.writeObject(param2);
            this.putByteArray(param1, _loc_3);
            return;
        }// end function

        private function getString() : String;

        private function putString(param1:String) : void;

        private function getHTML() : String;

        private function putHTML(param1:String) : void;

        private function getRTF() : ByteArray;

        private function putRTF(param1:ByteArray) : void;

        private function getByteArray(param1:String) : ByteArray;

        private function putByteArray(param1:String, param2:ByteArray) : void;

        private function convertNativeFormat(param1:String) : Object
        {
            var _loc_2:* = _toFlash[param1];
            if (_loc_2)
            {
                return this._loc_2(this);
            }
            var _loc_3:* = this.REFERENCE_PREFIX == param1.substr(0, this.REFERENCE_PREFIX.length);
            var _loc_4:* = this.SERIALIZATION_PREFIX == param1.substr(0, this.SERIALIZATION_PREFIX.length);
            if (_loc_3)
            {
                return this.getObjectReference(param1);
            }
            if (_loc_4)
            {
                return this.getDeserialization(param1);
            }
            return undefined;
        }// end function

        private function convertFlashFormat(param1:String, param2:Object, param3:Boolean) : Boolean
        {
            var _loc_4:* = undefined;
            if (isSystemFormat(param1))
            {
                _loc_4 = _fromFlash[param1];
                if (_loc_4)
                {
                    this._loc_4(this, param2);
                    return true;
                }
                return false;
            }
            this.putObjectReference(this.REFERENCE_PREFIX + param1, param2);
            if (param3)
            {
                this.putSerialization(this.SERIALIZATION_PREFIX + param1, param2);
            }
            return true;
        }// end function

        private function get swfVersion() : int;

        private function setHandlerStoringData(param1:Boolean) : void;

        public static function get generalClipboard() : Clipboard;

        private static function isSystemFormat(param1:String) : Boolean
        {
            if (Clipboard.FLASH_PREFIX != param1.substr(0, Clipboard.FLASH_PREFIX.length))
            {
            }
            return Clipboard.AIR_PREFIX == param1.substr(0, Clipboard.AIR_PREFIX.length);
        }// end function

        private static function initFormatMap() : void
        {
            if (!_wasFormatMapInitialized)
            {
                _fromFlash = new Dictionary();
                _toFlash = new Dictionary();
                addFormatMapping(Clipboard.TEXT_FORMAT, function (param1:Clipboard, param2:String) : void
            {
                param1.putString(param2);
                return;
            }// end function
            , function (param1:Clipboard) : String
            {
                return param1.getString();
            }// end function
            );
                addFormatMapping(Clipboard.HTML_FORMAT, function (param1:Clipboard, param2:String) : void
            {
                param1.putHTML(param2);
                return;
            }// end function
            , function (param1:Clipboard) : String
            {
                return param1.getHTML();
            }// end function
            );
                addFormatMapping(Clipboard.RICH_TEXT_FORMAT, function (param1:Clipboard, param2:ByteArray) : void
            {
                param1.putRTF(param2);
                return;
            }// end function
            , function (param1:Clipboard) : ByteArray
            {
                return param1.getRTF();
            }// end function
            );
                _wasFormatMapInitialized = true;
            }
            return;
        }// end function

        private static function addFormatMapping(param1:String, param2:Function, param3:Function)
        {
            _fromFlash[param1] = param2;
            _toFlash[param1] = param3;
            return;
        }// end function

    }
}