
//Created by Action Script Viewer - http://www.buraks.com/asv
    class mx.transitions.Blinds extends mx.transitions.Transition
    {
        var _dimension, _content, _mask, getNextHighestDepthMC, __get__direction, _innerMask, drawBox, _innerBounds;
        function Blinds (_arg3, _arg4, _arg5) {
            super();
            init(_arg3, _arg4, _arg5);
        }
        function init(_arg4, _arg3, _arg5) {
            super.init(_arg4, _arg3, _arg5);
            _dimension = (_arg3.dimension ? 1 : 0);
            if (_arg3.numStrips) {
                _numStrips = _arg3.numStrips;
            }
            _initMask();
        }
        function start() {
            _content.setMask(_mask);
            super.start();
        }
        function cleanUp() {
            _mask.removeMovieClip();
            super.cleanUp();
        }
        function _initMask() {
            var _local5 = _content;
            var _local6 = getNextHighestDepthMC(_local5);
            var _local4 = (_mask = _local5.createEmptyMovieClip("__mask_Blinds_" + __get__direction(), _local6));
            _local4._visible = false;
            var _local2 = (_innerMask = _mask.createEmptyMovieClip("innerMask", 0));
            _local2._x = (_local2._y = 50);
            if (_dimension) {
                _local2._rotation = -90;
            }
            _local2.beginFill(16711680);
            drawBox(_local2, 0, 0, 100, 100);
            _local2.endFill();
            var _local3 = _innerBounds;
            _local4._x = _local3.xMin;
            _local4._y = _local3.yMin;
            _local4._width = _local3.xMax - _local3.xMin;
            _local4._height = _local3.yMax - _local3.yMin;
        }
        function _render(_arg6) {
            var _local4 = 100 / _numStrips;
            var _local5 = _arg6 * _local4;
            var _local3 = _innerMask;
            _local3.clear();
            var _local2 = _numStrips;
            _local3.beginFill(16711680);
            while (_local2--) {
                drawBox(_local3, -50, (_local2 * _local4) - 50, 100, _local5);
            }
            _local3.endFill();
        }
        static var version = "1.1.0.52";
        var type = mx.transitions.Blinds;
        var className = "Blinds";
        var _numStrips = 10;
    }