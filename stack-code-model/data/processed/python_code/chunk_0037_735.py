class gs.plugins.BezierThroughPlugin extends gs.plugins.BezierPlugin
{
    var propName, init;
    function BezierThroughPlugin()
    {
        super();
        propName = "bezierThrough";
    } // End of the function
    function onInitTween($target, $value, $tween)
    {
        if (!($value instanceof Array))
        {
            return (false);
        } // end if
        var _loc2 = $value;
        this.init($tween, _loc2, true);
        return (true);
    } // End of the function
    static var VERSION = 1;
    static var API = 1;
} // End of Class