
//Created by Action Script Viewer - http://www.buraks.com/asv
    class mx.transitions.Transition
    {
        var _manager, removeEventListener, addEventListener, _content, _twn, _easing, _progress, dispatchEvent, _innerBounds, _outerBounds, _width, _height;
        function Transition (_arg3, _arg4, _arg5) {
            if (!arguments.length) {
                return;
            }
            init(_arg3, _arg4, _arg5);
        }
        function set manager(_arg2) {
            if (_manager != undefined) {
                removeEventListener("transitionInDone", _manager);
                removeEventListener("transitionOutDone", _manager);
                removeEventListener("transitionProgress", _manager);
            }
            _manager = _arg2;
            addEventListener("transitionInDone", _manager);
            addEventListener("transitionOutDone", _manager);
            addEventListener("transitionProgress", _manager);
            //return(manager);
        }
        function get manager() {
            return(_manager);
        }
        function set content(_arg2) {
            if (typeof(_arg2) == "movieclip") {
                _content = _arg2;
                _twn.obj = _arg2;
            }
            //return(content);
        }
        function get content() {
            return(_content);
        }
        function set direction(_arg2) {
            _direction = (_arg2 ? 1 : 0);
            //return(direction);
        }
        function get direction() {
            return(_direction);
        }
        function set duration(_arg2) {
            if (_arg2) {
                _duration = _arg2;
                _twn.duration = _arg2;
            }
            //return(duration);
        }
        function get duration() {
            return(_duration);
        }
        function set easing(e) {
            if (typeof(e) == "string") {
                e = eval (e);
            } else if (e == undefined) {
                e = _noEase;
            }
            _easing = e;
            _twn.easing = e;
            //return(easing);
        }
        function get easing() {
            return(_easing);
        }
        function set progress(_arg2) {
            if (_progress == _arg2) {
                return;
            }
            _progress = _arg2;
            if (_direction) {
                _render(1 - _arg2);
            } else {
                _render(_arg2);
            }
            dispatchEvent({type:"transitionProgress", target:this, progress:_arg2});
            //return(progress);
        }
        function get progress() {
            return(_progress);
        }
        function init(_arg3, _arg2, _arg4) {
            content = (_arg3);
            direction = (_arg2.direction);
            duration = (_arg2.duration);
            easing = (_arg2.easing);
            manager = (_arg4);
            _innerBounds = manager._innerBounds;
            _outerBounds = manager._outerBounds;
            _width = manager._width;
            _height = manager._height;
            _resetTween();
        }
        function toString() {
            return(("[Transition " + className) + "]");
        }
        function start() {
            content._visible = true;
            _twn.start();
        }
        function stop() {
            _twn.fforward();
            _twn.stop();
        }
        function cleanUp() {
            removeEventListener("transitionInDone", _manager);
            removeEventListener("transitionOutDone", _manager);
            removeEventListener("transitionProgress", _manager);
            this.stop();
        }
        function getNextHighestDepthMC(_arg2) {
            var _local4 = _arg2.getNextHighestDepth();
            if (_local4 != undefined) {
                return(_local4);
            } else {
                _local4 = -1;
                var _local3;
                var _local1;
                for (var _local5 in _arg2) {
                    _local1 = _arg2[_local5];
                    if ((typeof(_local1) == "movieclip") && (_local1._parent == _arg2)) {
                        _local3 = _local1.getDepth();
                        if (_local3 > _local4) {
                            _local4 = _local3;
                        }
                    }
                }
                return(_local4 + 1);
            }
        }
        function drawBox(_arg1, _arg3, _arg2, _arg5, _arg4) {
            _arg1.moveTo(_arg3, _arg2);
            _arg1.lineTo(_arg3 + _arg5, _arg2);
            _arg1.lineTo(_arg3 + _arg5, _arg2 + _arg4);
            _arg1.lineTo(_arg3, _arg2 + _arg4);
            _arg1.lineTo(_arg3, _arg2);
        }
        function drawCircle(_arg4, _arg3, _arg2, _arg1) {
            _arg4.moveTo(_arg3 + _arg1, _arg2);
            _arg4.curveTo(_arg1 + _arg3, (0.414213562373095 * _arg1) + _arg2, (0.707106781186547 * _arg1) + _arg3, (0.707106781186547 * _arg1) + _arg2);
            _arg4.curveTo((0.414213562373095 * _arg1) + _arg3, _arg1 + _arg2, _arg3, _arg1 + _arg2);
            _arg4.curveTo((-0.414213562373095 * _arg1) + _arg3, _arg1 + _arg2, (-0.707106781186547 * _arg1) + _arg3, (0.707106781186547 * _arg1) + _arg2);
            _arg4.curveTo((-_arg1) + _arg3, (0.414213562373095 * _arg1) + _arg2, (-_arg1) + _arg3, _arg2);
            _arg4.curveTo((-_arg1) + _arg3, (-0.414213562373095 * _arg1) + _arg2, (-0.707106781186547 * _arg1) + _arg3, (-0.707106781186547 * _arg1) + _arg2);
            _arg4.curveTo((-0.414213562373095 * _arg1) + _arg3, (-_arg1) + _arg2, _arg3, (-_arg1) + _arg2);
            _arg4.curveTo((0.414213562373095 * _arg1) + _arg3, (-_arg1) + _arg2, (0.707106781186547 * _arg1) + _arg3, (-0.707106781186547 * _arg1) + _arg2);
            _arg4.curveTo(_arg1 + _arg3, (-0.414213562373095 * _arg1) + _arg2, _arg1 + _arg3, _arg2);
        }
        function _render(p) {
        }
        function _resetTween() {
            _twn.stop();
            _twn.removeListener(this);
            _twn = new mx.transitions.Tween(this, null, easing, 0, 1, duration, true);
            _twn.stop();
            _twn.prop = "progress";
            _twn.addListener(this);
        }
        function _noEase(_arg2, _arg4, _arg3, _arg1) {
            return(((_arg3 * _arg2) / _arg1) + _arg4);
        }
        function onMotionFinished(src) {
            if (direction) {
                dispatchEvent({type:"transitionOutDone", target:this});
            } else {
                dispatchEvent({type:"transitionInDone", target:this});
            }
        }
        static var version = "1.1.0.52";
        static var IN = 0;
        static var OUT = 1;
        var type = mx.transitions.Transition;
        var className = "Transition";
        var _direction = 0;
        var _duration = 2;
        static var __mixinFED = mx.events.EventDispatcher.initialize(mx.transitions.Transition.prototype);
    }