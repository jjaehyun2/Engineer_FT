class gs.plugins.ShortRotationPlugin extends gs.plugins.TweenPlugin
{
    var propName, overwriteProps, addTween;
    function ShortRotationPlugin()
    {
        super();
        propName = "shortRotation";
        overwriteProps = [];
    } // End of the function
    function onInitTween($target, $value, $tween)
    {
        if (typeof($value) == "number")
        {
            trace ("WARNING: You appear to be using the old shortRotation syntax. Instead of passing a number, please pass an object with properties that correspond to the rotations values For example, TweenMax.to(mc, 2, {shortRotation:{rotationX:-170, rotationY:25}})");
            return (false);
        } // end if
        for (var _loc4 in $value)
        {
            this.initRotation($target, _loc4, $target[_loc4], $value[_loc4]);
        } // end of for...in
        return (true);
    } // End of the function
    function initRotation($target, $propName, $start, $end)
    {
        var _loc2 = ($end - $start) % 360;
        if (_loc2 != _loc2 % 180)
        {
            _loc2 = _loc2 < 0 ? (_loc2 + 360) : (_loc2 - 360);
        } // end if
        this.addTween($target, $propName, $start, $start + _loc2, $propName);
        overwriteProps[overwriteProps.length] = $propName;
    } // End of the function
    static var VERSION = 1;
    static var API = 1;
} // End of Class