class gs.plugins.TransformAroundPointPlugin extends gs.plugins.TweenPlugin
{
    var propName, overwriteProps, _target, _point, _local, _temp, _shortRotation, addTween, __set__changeFactor, round, _tweens, __get__changeFactor;
    function TransformAroundPointPlugin()
    {
        super();
        propName = "transformAroundPoint";
        overwriteProps = [];
    } // End of the function
    function onInitTween($target, $value, $tween)
    {
        if (!($value.point instanceof flash.geom.Point))
        {
            return (false);
        } // end if
        _target = (MovieClip)($target);
        _point = $value.point.clone();
        _local = _point.clone();
        _target._parent.localToGlobal(_local);
        _target.globalToLocal(_local);
        _temp = _local.clone();
        var _loc2;
        var _loc11;
        var _loc4;
        var _loc5;
        for (var _loc2 in $value)
        {
            if (_loc2 == "point")
            {
                continue;
            } // end if
            if (_loc2 == "shortRotation")
            {
                _shortRotation = new gs.plugins.ShortRotationPlugin();
                _shortRotation.onInitTween(_target, $value[_loc2], $tween);
                this.addTween(_shortRotation, "changeFactor", 0, 1, "shortRotation");
                for (var _loc4 in $value[_loc2])
                {
                    overwriteProps[overwriteProps.length] = _loc4;
                } // end of for...in
                continue;
            } // end if
            if (_loc2 == "_x" || _loc2 == "_y")
            {
                _loc5 = _loc2 == "_x" ? ("x") : ("y");
                this.addTween(_point, _loc5, _point[_loc5], $value[_loc2], _loc2);
                overwriteProps[overwriteProps.length] = _loc2;
                continue;
            } // end if
            if (_loc2 == "scale")
            {
                this.addTween(_target, "_xscale", _target._xscale, $value.scale, "_xscale");
                this.addTween(_target, "_yscale", _target._yscale, $value.scale, "_yscale");
                overwriteProps[overwriteProps.length] = "_xscale";
                overwriteProps[overwriteProps.length] = "_yscale";
                continue;
            } // end if
            this.addTween(_target, _loc2, _target[_loc2], $value[_loc2], _loc2);
            overwriteProps[overwriteProps.length] = _loc2;
        } // end of for...in
        if ($tween.vars._x != undefined || $tween.vars._y != undefined)
        {
            var _loc8;
            var _loc7;
            if ($tween.vars._x != undefined)
            {
                _loc8 = typeof($tween.vars._x) == "number" ? ($tween.vars._x) : (_target._x + Number($tween.vars._x));
            } // end if
            if ($tween.vars._y != undefined)
            {
                _loc7 = typeof($tween.vars._y) == "number" ? ($tween.vars._y) : (_target._y + Number($tween.vars._y));
            } // end if
            $tween.killVars({_x: true, _y: true});
            this.__set__changeFactor(1);
            if (!isNaN(_loc8))
            {
                this.addTween(_point, "x", _point.x, _point.x + (_loc8 - _target._x), "_x");
                overwriteProps[overwriteProps.length] = "_x";
            } // end if
            if (!isNaN(_loc7))
            {
                this.addTween(_point, "y", _point.y, _point.y + (_loc7 - _target._y), "_y");
                overwriteProps[overwriteProps.length] = "_y";
            } // end if
            this.__set__changeFactor(0);
        } // end if
        return (true);
    } // End of the function
    function killProps($lookup)
    {
        if (_shortRotation != undefined)
        {
            _shortRotation.killProps($lookup);
            if (_shortRotation.overwriteProps.length == 0)
            {
                $lookup.shortRotation = true;
            } // end if
        } // end if
        super.killProps($lookup);
    } // End of the function
    function set changeFactor($n)
    {
        _temp.x = _local.x;
        _temp.y = _local.y;
        var _loc3;
        var _loc2;
        if (round)
        {
            for (var _loc3 = _tweens.length - 1; _loc3 > -1; --_loc3)
            {
                _loc2 = _tweens[_loc3];
                _loc2.target[_loc2.property] = Math.round(_loc2.start + _loc2.change * $n);
            } // end of for
            _target.localToGlobal(_temp);
            _target._parent.globalToLocal(_temp);
            _target._x = Math.round(_target._x + _point.x - _temp.x);
            _target._y = Math.round(_target._y + _point.y - _temp.y);
        }
        else
        {
            for (var _loc3 = _tweens.length - 1; _loc3 > -1; --_loc3)
            {
                _loc2 = _tweens[_loc3];
                _loc2.target[_loc2.property] = _loc2.start + _loc2.change * $n;
            } // end of for
            _target.localToGlobal(_temp);
            _target._parent.globalToLocal(_temp);
            _target._x = _target._x + (_point.x - _temp.x);
            _target._y = _target._y + (_point.y - _temp.y);
        } // end else if
        //return (this.changeFactor());
        null;
    } // End of the function
    static var VERSION = 1.010000E+000;
    static var API = 1;
} // End of Class