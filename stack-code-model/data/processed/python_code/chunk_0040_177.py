class gs.plugins.VisiblePlugin extends gs.plugins.TweenPlugin
{
    var propName, overwriteProps, onComplete, _target, _tween, _visible, __get__changeFactor, __set__changeFactor;
    function VisiblePlugin()
    {
        super();
        propName = "_visible";
        overwriteProps = ["_visible"];
        onComplete = onCompleteTween;
    } // End of the function
    function onInitTween($target, $value, $tween)
    {
        _target = $target;
        _tween = $tween;
        _visible = Boolean($value);
        return (true);
    } // End of the function
    function onCompleteTween()
    {
        if (_tween.vars.runBackwards != true && _tween.ease == _tween.vars.ease)
        {
            _target._visible = _visible;
        } // end if
    } // End of the function
    function set changeFactor($n)
    {
        if (_target._visible != true)
        {
            _target._visible = true;
        } // end if
        //return (this.changeFactor());
        null;
    } // End of the function
    static var VERSION = 1;
    static var API = 1;
} // End of Class