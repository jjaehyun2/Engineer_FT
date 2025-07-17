
//Created by Action Script Viewer - http://www.buraks.com/asv
    class caurina.transitions.SpecialPropertyModifier
    {
        var modifyValues, getValue;
        function SpecialPropertyModifier (_arg3, _arg2) {
            modifyValues = _arg3;
            getValue = _arg2;
        }
        function toString() {
            var _local2 = "";
            _local2 = _local2 + "[SpecialPropertyModifier ";
            _local2 = _local2 + ("modifyValues:" + modifyValues.toString());
            _local2 = _local2 + ", ";
            _local2 = _local2 + ("getValue:" + getValue.toString());
            _local2 = _local2 + "]";
            return(_local2);
        }
    }