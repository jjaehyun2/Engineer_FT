
//Created by Action Script Viewer - http://www.buraks.com/asv
    class caurina.transitions.PropertyInfoObj
    {
        var valueStart, valueComplete, originalValueComplete, arrayIndex, extra, isSpecialProperty, hasModifier, modifierFunction, modifierParameters;
        function PropertyInfoObj (_arg3, _arg8, _arg4, _arg7, _arg6, _arg5, _arg2, _arg9) {
            valueStart = _arg3;
            valueComplete = _arg8;
            originalValueComplete = _arg4;
            arrayIndex = _arg7;
            extra = _arg6;
            isSpecialProperty = _arg5;
            hasModifier = _arg2 != undefined;
            modifierFunction = _arg2;
            modifierParameters = _arg9;
        }
        function clone() {
            var _local2 = new caurina.transitions.PropertyInfoObj(valueStart, valueComplete, originalValueComplete, arrayIndex, extra, isSpecialProperty, modifierFunction, modifierParameters);
            return(_local2);
        }
        function toString() {
            var _local2 = "\n[PropertyInfoObj ";
            _local2 = _local2 + ("valueStart:" + String(valueStart));
            _local2 = _local2 + ", ";
            _local2 = _local2 + ("valueComplete:" + String(valueComplete));
            _local2 = _local2 + ", ";
            _local2 = _local2 + ("originalValueComplete:" + String(originalValueComplete));
            _local2 = _local2 + ", ";
            _local2 = _local2 + ("arrayIndex:" + String(arrayIndex));
            _local2 = _local2 + ", ";
            _local2 = _local2 + ("extra:" + String(extra));
            _local2 = _local2 + ", ";
            _local2 = _local2 + ("isSpecialProperty:" + String(isSpecialProperty));
            _local2 = _local2 + ", ";
            _local2 = _local2 + ("hasModifier:" + String(hasModifier));
            _local2 = _local2 + ", ";
            _local2 = _local2 + ("modifierFunction:" + String(modifierFunction));
            _local2 = _local2 + ", ";
            _local2 = _local2 + ("modifierParameters:" + String(modifierParameters));
            _local2 = _local2 + "]\n";
            return(_local2);
        }
    }