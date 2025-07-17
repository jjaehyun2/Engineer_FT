
//Created by Action Script Viewer - http://www.buraks.com/asv
    class mx.transitions.PixelDissolve extends mx.transitions.Transition
    {
        var _numSections, _indices, _content, _mask, getNextHighestDepthMC, __get__direction, _innerMask, drawBox, _innerBounds;
        function PixelDissolve (_arg3, _arg4, _arg5) {
            super();
            init(_arg3, _arg4, _arg5);
        }
        function init(_arg6, _arg5, _arg7) {
            super.init(_arg6, _arg5, _arg7);
            if (_arg5.xSections) {
                _xSections = _arg5.xSections;
            }
            if (_arg5.ySections) {
                _ySections = _arg5.ySections;
            }
            _numSections = _xSections * _ySections;
            _indices = new Array();
            var _local3 = _ySections;
            while (_local3--) {
                var _local4 = _xSections;
                while (_local4--) {
                    _indices[(_local3 * _xSections) + _local4] = {x:_local4, y:_local3};
                }
            }
            _shuffleArray(_indices);
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
            var _local3 = (_mask = _local5.createEmptyMovieClip("__mask_PixelDissolve_" + __get__direction(), _local6));
            _local3._visible = false;
            var _local4 = (_innerMask = _mask.createEmptyMovieClip("innerMask", 0));
            _local4.beginFill(16711680);
            drawBox(_local4, 0, 0, 100, 100);
            _local4.endFill();
            var _local2 = _innerBounds;
            _local3._x = _local2.xMin;
            _local3._y = _local2.yMin;
            _local3._width = _local2.xMax - _local2.xMin;
            _local3._height = _local2.yMax - _local2.yMin;
        }
        function _shuffleArray(_arg2) {
            var _local1 = _arg2.length - 1;
            while (_local1 > 0) {
                var _local3 = random(_local1 + 1);
                if (_local3 == _local1) {
                } else {
                    var _local4 = _arg2[_local1];
                    _arg2[_local1] = _arg2[_local3];
                    _arg2[_local3] = _local4;
                }
                _local1--;
            }
        }
        function _render(_arg7) {
            if (_arg7 < 0) {
                _arg7 = 0;
            }
            if (_arg7 > 1) {
                _arg7 = 1;
            }
            var _local5 = 100 / _xSections;
            var _local4 = 100 / _ySections;
            var _local3 = _indices;
            var _local6 = _innerMask;
            _local6.clear();
            _local6.beginFill(16711680);
            var _local2 = Math.floor(_arg7 * _numSections);
            while (_local2--) {
                drawBox(_local6, _local3[_local2].x * _local5, _local3[_local2].y * _local4, _local5, _local4);
            }
            _local6.endFill();
        }
        static var version = "1.1.0.52";
        var type = mx.transitions.PixelDissolve;
        var className = "PixelDissolve";
        var _xSections = 10;
        var _ySections = 10;
    }