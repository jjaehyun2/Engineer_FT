
//Created by Action Script Viewer - http://www.buraks.com/asv
    class mx.transitions.Fade extends mx.transitions.Transition
    {
        var _alphaFinal, __get__manager, _content;
        function Fade (_arg3, _arg4, _arg5) {
            super();
            init(_arg3, _arg4, _arg5);
        }
        function init(_arg3, _arg4, _arg5) {
            super.init(_arg3, _arg4, _arg5);
            _alphaFinal = __get__manager().__get__contentAppearance()._alpha;
        }
        function _render(_arg2) {
            _content._alpha = _alphaFinal * _arg2;
        }
        static var version = "1.1.0.52";
        var type = mx.transitions.Fade;
        var className = "Fade";
    }