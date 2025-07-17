
//Created by Action Script Viewer - http://www.buraks.com/asv
    class mx.transitions.Rotate extends mx.transitions.Transition
    {
        var _rotationFinal, __get__manager, __get__direction, _content;
        function Rotate (_arg3, _arg4, _arg5) {
            super();
            init(_arg3, _arg4, _arg5);
        }
        function init(_arg4, _arg3, _arg5) {
            super.init(_arg4, _arg3, _arg5);
            if (_rotationFinal == undefined) {
                _rotationFinal = __get__manager().__get__contentAppearance()._rotation;
            }
            if (_arg3.degrees) {
                _degrees = _arg3.degrees;
            }
            if (_arg3.ccw ^ __get__direction()) {
                _degrees = _degrees * -1;
            }
        }
        function _render(_arg2) {
            _content._rotation = _rotationFinal - (_degrees * (1 - _arg2));
        }
        static var version = "1.1.0.52";
        var type = mx.transitions.Rotate;
        var className = "Rotate";
        var _degrees = 360;
    }