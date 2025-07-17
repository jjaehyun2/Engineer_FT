
//Created by Action Script Viewer - http://www.buraks.com/asv
    class mx.events.EventDispatcher
    {
        function EventDispatcher () {
        }
        static function _removeEventListener(_arg3, event, _arg5) {
            if (_arg3 != undefined) {
                var _local4 = _arg3.length;
                var _local1;
                _local1 = 0;
                while (_local1 < _local4) {
                    var _local2 = _arg3[_local1];
                    if (_local2 == _arg5) {
                        _arg3.splice(_local1, 1);
                        return(undefined);
                    }
                    _local1++;
                }
            }
        }
        static function initialize(_arg1) {
            if (_fEventDispatcher == undefined) {
                _fEventDispatcher = new mx.events.EventDispatcher();
            }
            _arg1.addEventListener = _fEventDispatcher.addEventListener;
            _arg1.removeEventListener = _fEventDispatcher.removeEventListener;
            _arg1.dispatchEvent = _fEventDispatcher.dispatchEvent;
            _arg1.dispatchQueue = _fEventDispatcher.dispatchQueue;
        }
        function dispatchQueue(_arg6, _arg2) {
            var _local7 = "__q_" + _arg2.type;
            var _local4 = _arg6[_local7];
            if (_local4 != undefined) {
                var _local5;
                for (_local5 in _local4) {
                    var _local1 = _local4[_local5];
                    var _local3 = typeof(_local1);
                    if ((_local3 == "object") || (_local3 == "movieclip")) {
                        if (_local1.handleEvent != undefined) {
                            _local1.handleEvent(_arg2);
                        }
                        if (_local1[_arg2.type] != undefined) {
                            if (exceptions[_arg2.type] == undefined) {
                                _local1[_arg2.type](_arg2);
                            }
                        }
                    } else {
                        _local1.apply(_arg6, [_arg2]);
                    }
                }
            }
        }
        function dispatchEvent(_arg2) {
            if (_arg2.target == undefined) {
                _arg2.target = this;
            }
            this[_arg2.type + "Handler"](_arg2);
            dispatchQueue(this, _arg2);
        }
        function addEventListener(_arg4, _arg5) {
            var _local3 = "__q_" + _arg4;
            if (this[_local3] == undefined) {
                this[_local3] = new Array();
            }
            _global.ASSetPropFlags(this, _local3, 1);
            _removeEventListener(this[_local3], _arg4, _arg5);
            this[_local3].push(_arg5);
        }
        function removeEventListener(_arg3, _arg4) {
            var _local2 = "__q_" + _arg3;
            _removeEventListener(this[_local2], _arg3, _arg4);
        }
        static var _fEventDispatcher = undefined;
        static var exceptions = {move:1, draw:1, load:1};
    }