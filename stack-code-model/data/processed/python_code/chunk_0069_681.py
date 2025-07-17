    class SWFAddress
    {
        static var _interval, onInit, onChange;
        function SWFAddress () {
        }
        static function _initialize() {
            if (_availability) {
                flash.external.ExternalInterface.addCallback("getSWFAddressValue", SWFAddress, function () {
                    return(this._value);
                });
                flash.external.ExternalInterface.addCallback("setSWFAddressValue", SWFAddress, _setValue);
            }
            if (typeof(_level0.$swfaddress) != "undefined") {
                _value = _level0.$swfaddress;
            }
            _interval = setInterval(_check, 10);
            return(true);
        }
        static function _check() {
            if (((typeof(onInit) == "function") || (typeof(_dispatcher.__q_init) != "undefined")) && (!_init)) {
                _setValueInit(_getValue());
                _init = true;
            }
            if ((typeof(onChange) == "function") || (typeof(_dispatcher.__q_change) != "undefined")) {
                clearInterval(_interval);
                _init = true;
                _setValueInit(_getValue());
            }
        }
        static function _strictCheck(_arg1, _arg2) {
            if (getStrict()) {
                if (_arg2) {
                    if (_arg1.substr(0, 1) != "/") {
                        _arg1 = "/" + _arg1;
                    }
                } else if (_arg1 == "") {
                    _arg1 = "/";
                }
            }
            return(_arg1);
        }
        static function _getValue() {
            var _local1;
            var _local2 = "null";
            if (_availability) {
                _local1 = String(flash.external.ExternalInterface.call("SWFAddress.getValue"));
                _local2 = String(flash.external.ExternalInterface.call("SWFAddress.getIds"));
            }
            if (((_local2 == "undefined") || (_local2 == "null")) || (!_availability)) {
                _local1 = _value;
            } else if ((_local1 == "undefined") || (_local1 == "null")) {
                _local1 = "";
            }
            return(_strictCheck(_local1 || "", false));
        }
        static function _setValueInit(_arg1) {
            _value = _arg1;
            if (!_init) {
                _dispatchEvent("init");
            } else {
                _dispatchEvent("change");
            }
            _initChange = true;
        }
        static function _setValue(_arg1) {
            if ((_arg1 == "undefined") || (_arg1 == "null")) {
                _arg1 = "";
            }
            if ((_value == _arg1) && (_init)) {
                return(undefined);
            }
            if (!_initChange) {
                return(undefined);
            }
            _value = _arg1;
            if (!_init) {
                _init = true;
                if ((typeof(onInit) == "function") || (typeof(_dispatcher.__q_init) != "undefined")) {
                    _dispatchEvent("init");
                }
            }
            _dispatchEvent("change");
        }
        static function _dispatchEvent(_arg1) {
            if (typeof(_dispatcher["__q_" + _arg1]) != "undefined") {
                _dispatcher.dispatchEvent(new SWFAddressEvent(_arg1));
            }
            _arg1 = _arg1.substr(0, 1).toUpperCase() + _arg1.substring(1);
            if (typeof(SWFAddress["on" + _arg1]) == "function") {
                SWFAddress["on" + _arg1]();
            }
        }
        static function toString() {
            return("[class SWFAddress]");
        }
        static function back() {
            if (_availability) {
                flash.external.ExternalInterface.call("SWFAddress.back");
            }
        }
        static function forward() {
            if (_availability) {
                flash.external.ExternalInterface.call("SWFAddress.forward");
            }
        }
        static function up() {
            var _local1 = getPath();
            setValue(_local1.substr(0, _local1.lastIndexOf("/", _local1.length - 2) + ((_local1.substr(_local1.length - 1) == "/") ? 1 : 0)));
        }
        static function go(_arg1) {
            if (_availability) {
                flash.external.ExternalInterface.call("SWFAddress.go", _arg1);
            }
        }
        static function href(_arg2, _arg1) {
            _arg1 = ((typeof(_arg1) != "undefined") ? (_arg1) : "_self");
            if (_availability && (System.capabilities.playerType == "ActiveX")) {
                flash.external.ExternalInterface.call("SWFAddress.href", _arg2, _arg1);
                return(undefined);
            }
            getURL (_arg2, _arg1);
        }
        static function popup(_arg4, _arg1, _arg2, _arg3) {
            _arg1 = ((typeof(_arg1) != "undefined") ? (_arg1) : "popup");
            _arg2 = ((typeof(_arg2) != "undefined") ? (_arg2) : "\"\"");
            _arg3 = ((typeof(_arg3) != "undefined") ? (_arg3) : "");
            if (_availability && (System.capabilities.playerType == "ActiveX")) {
                flash.external.ExternalInterface.call("SWFAddress.popup", _arg4, _arg1, _arg2, _arg3);
                return(undefined);
            }
            getURL (((((((("javascript:popup=window.open(\"" + _arg4) + "\",\"") + _arg1) + "\",") + _arg2) + ");") + _arg3) + ";void(0);");
        }
        static function addEventListener(_arg2, _arg1) {
            _dispatcher.addEventListener(_arg2, _arg1);
        }
        static function removeEventListener(_arg2, _arg1) {
            _dispatcher.removeEventListener(_arg2, _arg1);
        }
        static function dispatchEvent(_arg1) {
            _dispatcher.dispatchEvent(_arg1);
        }
        static function hasEventListener(_arg1) {
            return(typeof(_dispatcher["__q_" + _arg1]) != "undefined");
        }
        static function getBaseURL() {
            var _local1 = "null";
            if (_availability) {
                _local1 = String(flash.external.ExternalInterface.call("SWFAddress.getBaseURL"));
            }
            return(((((_local1 == "undefined") || (_local1 == "null")) || (!_availability)) ? "" : (_local1)));
        }
        static function getStrict() {
            var _local1 = "null";
            if (_availability) {
                _local1 = String(flash.external.ExternalInterface.call("SWFAddress.getStrict"));
            }
            return((((_local1 == "null") || (_local1 == "undefined")) ? (_strict) : (_local1 == "true")));
        }
        static function setStrict(_arg1) {
            if (_availability) {
                flash.external.ExternalInterface.call("SWFAddress.setStrict", _arg1);
            }
            _strict = _arg1;
        }
        static function getHistory() {
            return(Boolean((_availability ? (flash.external.ExternalInterface.call("SWFAddress.getHistory")) : false)));
        }
        static function setHistory(_arg1) {
            if (_availability) {
                flash.external.ExternalInterface.call("SWFAddress.setHistory", _arg1);
            }
        }
        static function getTracker() {
            return((_availability ? (String(flash.external.ExternalInterface.call("SWFAddress.getTracker"))) : ""));
        }
        static function setTracker(_arg1) {
            if (_availability) {
                flash.external.ExternalInterface.call("SWFAddress.setTracker", _arg1);
            }
        }
        static function getTitle() {
            var _local1 = (_availability ? (String(flash.external.ExternalInterface.call("SWFAddress.getTitle"))) : "");
            if ((_local1 == "undefined") || (_local1 == "null")) {
                _local1 = "";
            }
            return(_local1);
        }
        static function setTitle(_arg1) {
            if (_availability) {
                flash.external.ExternalInterface.call("SWFAddress.setTitle", _arg1);
            }
        }
        static function getStatus() {
            var _local1 = (_availability ? (String(flash.external.ExternalInterface.call("SWFAddress.getStatus"))) : "");
            if ((_local1 == "undefined") || (_local1 == "null")) {
                _local1 = "";
            }
            return(_local1);
        }
        static function setStatus(_arg1) {
            if (_availability) {
                flash.external.ExternalInterface.call("SWFAddress.setStatus", _arg1);
            }
        }
        static function resetStatus() {
            if (_availability) {
                flash.external.ExternalInterface.call("SWFAddress.resetStatus");
            }
        }
        static function getValue() {
            return(_strictCheck(_value || "", false));
        }
        static function setValue(_arg1) {
            if ((_arg1 == "undefined") || (_arg1 == "null")) {
                _arg1 = "";
            }
            _arg1 = _strictCheck(_arg1, true);
            if (_value == _arg1) {
                return(undefined);
            }
            _value = _arg1;
            if (_availability) {
                flash.external.ExternalInterface.call("SWFAddress.setValue", _arg1);
            }
            _dispatchEvent("change");
        }
        static function getPath() {
            var _local1 = getValue();
            if (_local1.indexOf("?") != -1) {
                return(_local1.split("?")[0]);
            } else {
                return(_local1);
            }
        }
        static function getPathNames() {
            var _local1 = getPath();
            var _local2 = _local1.split("/");
            if ((_local1.substr(0, 1) == "/") || (_local1.length == 0)) {
                _local2.splice(0, 1);
            }
            if (_local1.substr(_local1.length - 1, 1) == "/") {
                _local2.splice(_local2.length - 1, 1);
            }
            return(_local2);
        }
        static function getQueryString() {
            var _local1 = getValue();
            var _local2 = _local1.indexOf("?");
            if ((_local2 != -1) && (_local2 < _local1.length)) {
                return(_local1.substr(_local2 + 1));
            }
            return("");
        }
        static function getParameter(_arg5) {
            var _local4 = getValue();
            var _local6 = _local4.indexOf("?");
            if (_local6 != -1) {
                _local4 = _local4.substr(_local6 + 1);
                var _local3 = _local4.split("&");
                var _local1;
                var _local2 = _local3.length;
                while (_local2--) {
                    _local1 = _local3[_local2].split("=");
                    if (_local1[0] == _arg5) {
                        return(_local1[1]);
                    }
                }
            }
            return("");
        }
        static function getParameterNames() {
            var _local4 = getValue();
            var _local5 = _local4.indexOf("?");
            var _local3 = new Array();
            if (_local5 != -1) {
                _local4 = _local4.substr(_local5 + 1);
                if ((_local4 != "") && (_local4.indexOf("=") != -1)) {
                    var _local2 = _local4.split("&");
                    var _local1 = 0;
                    while (_local1 < _local2.length) {
                        _local3.push(_local2[_local1].split("=")[0]);
                        _local1++;
                    }
                }
            }
            return(_local3);
        }
        static var _init = false;
        static var _initChange = false;
        static var _strict = true;
        static var _value = "";
        static var _availability = flash.external.ExternalInterface.available;
        static var _dispatcher = new mx.events.EventDispatcher();
        static var _initializer = _initialize();
    }