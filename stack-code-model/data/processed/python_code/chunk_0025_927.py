
//Created by Action Script Viewer - http://www.buraks.com/asv
    class mx.transitions.Photo extends mx.transitions.Transition
    {
        var _alphaFinal, __get__manager, _colorControl, _content;
        function Photo (_arg3, _arg4, _arg5) {
            super();
            init(_arg3, _arg4, _arg5);
        }
        function init(_arg3, _arg4, _arg5) {
            super.init(_arg3, _arg4, _arg5);
            _alphaFinal = __get__manager().__get__contentAppearance()._alpha;
            _colorControl = new Color(_content);
        }
        function _render(_arg6) {
            var _local4 = 0.8;
            var _local3 = 0.9;
            var _local2 = {};
            var _local5 = 0;
            if (_arg6 <= _local4) {
                _content._alpha = _alphaFinal * (_arg6 / _local4);
            } else {
                _content._alpha = _alphaFinal;
                if (_arg6 <= _local3) {
                    _local5 = ((_arg6 - _local4) / (_local3 - _local4)) * 256;
                } else {
                    _local5 = (1 - ((_arg6 - _local3) / (1 - _local3))) * 256;
                }
            }
            _local2.rb = (_local2.gb = (_local2.bb = _local5));
            _colorControl.setTransform(_local2);
        }
        static var version = "1.1.0.52";
        var type = mx.transitions.Photo;
        var className = "Photo";
    }