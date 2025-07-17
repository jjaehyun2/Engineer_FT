
//Created by Action Script Viewer - http://www.buraks.com/asv
    class caurina.transitions.SpecialPropertySplitter
    {
        var parameters;
        function SpecialPropertySplitter (_arg3, _arg2) {
            splitValues = _arg3;
            parameters = _arg2;
        }
        function splitValues(p_value, p_parameters) {
            return([]);
        }
        function toString() {
            var _local2 = "";
            _local2 = _local2 + "[SpecialPropertySplitter ";
            _local2 = _local2 + ("splitValues:" + splitValues.toString());
            _local2 = _local2 + ", ";
            _local2 = _local2 + ("parameters:" + parameters.toString());
            _local2 = _local2 + "]";
            return(_local2);
        }
    }