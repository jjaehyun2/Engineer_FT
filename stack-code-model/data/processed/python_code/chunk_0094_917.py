﻿
//Created by Action Script Viewer - http://www.buraks.com/asv
    class mx.transitions.easing.Strong
    {
        function Strong () {
        }
        static function easeIn(_arg1, _arg4, _arg3, _arg2) {
            _arg1 = _arg1 / _arg2;
            return((((((_arg3 * _arg1) * _arg1) * _arg1) * _arg1) * _arg1) + _arg4);
        }
        static function easeOut(_arg1, _arg4, _arg3, _arg2) {
            _arg1 = (_arg1 / _arg2) - 1;
            return((_arg3 * (((((_arg1 * _arg1) * _arg1) * _arg1) * _arg1) + 1)) + _arg4);
        }
        static function easeInOut(_arg1, _arg3, _arg2, _arg4) {
            _arg1 = _arg1 / (_arg4 / 2);
            if (_arg1 < 1) {
                return(((((((_arg2 / 2) * _arg1) * _arg1) * _arg1) * _arg1) * _arg1) + _arg3);
            }
            _arg1 = _arg1 - 2;
            return(((_arg2 / 2) * (((((_arg1 * _arg1) * _arg1) * _arg1) * _arg1) + 2)) + _arg3);
        }
        static var version = "1.1.0.52";
    }