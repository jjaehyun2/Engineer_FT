class gs.plugins.HexColorsPlugin extends gs.plugins.TweenPlugin
{
    var propName, overwriteProps, _colors, __get__changeFactor, __set__changeFactor;
    function HexColorsPlugin()
    {
        super();
        propName = "hexColors";
        overwriteProps = [];
        _colors = [];
    } // End of the function
    function onInitTween($target, $value, $tween)
    {
        for (var _loc4 in $value)
        {
            this.initColor($target, _loc4, Number($target[_loc4]), Number($value[_loc4]));
        } // end of for...in
        return (true);
    } // End of the function
    function initColor($target, $propName, $start, $end)
    {
        if ($start != $end)
        {
            var _loc4 = $start >> 16;
            var _loc6 = $start >> 8 & 255;
            var _loc3 = $start & 255;
            _colors[_colors.length] = [$target, $propName, _loc4, ($end >> 16) - _loc4, _loc6, ($end >> 8 & 255) - _loc6, _loc3, ($end & 255) - _loc3];
            overwriteProps[overwriteProps.length] = $propName;
        } // end if
    } // End of the function
    function killProps($lookup)
    {
        for (var _loc3 = _colors.length - 1; _loc3 > -1; --_loc3)
        {
            if ($lookup[_colors[_loc3][1]] != undefined)
            {
                _colors.splice(_loc3, 1);
            } // end if
        } // end of for
        super.killProps($lookup);
    } // End of the function
    function set changeFactor($n)
    {
        var _loc3;
        var _loc2;
        for (var _loc3 = _colors.length - 1; _loc3 > -1; --_loc3)
        {
            _loc2 = _colors[_loc3];
            _loc2[0][_loc2[1]] = _loc2[2] + $n * _loc2[3] << 16 | _loc2[4] + $n * _loc2[5] << 8 | _loc2[6] + $n * _loc2[7];
        } // end of for
        //return (this.changeFactor());
        null;
    } // End of the function
    static var VERSION = 1.010000E+000;
    static var API = 1;
} // End of Class