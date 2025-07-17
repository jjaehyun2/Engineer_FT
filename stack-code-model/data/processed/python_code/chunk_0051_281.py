class gs.TweenLite
{
    var vars, duration, delay, combinedTimeScale, active, target, ease, tweens, initted, initTime, startTime, endTargetID, _hasPlugins, _hasUpdate, started, __set__enabled, gc, __get__enabled;
    static var timerClip, _tlInitted, currentTime, _gcInterval, overwriteManager;
    function TweenLite($target, $duration, $vars)
    {
        if (gs.TweenLite.timerClip._visible != false || !gs.TweenLite._tlInitted)
        {
            gs.plugins.TweenPlugin.activate([gs.plugins.TintPlugin, gs.plugins.RemoveTintPlugin, gs.plugins.FramePlugin, gs.plugins.AutoAlphaPlugin, gs.plugins.VisiblePlugin, gs.plugins.VolumePlugin, gs.plugins.EndArrayPlugin]);
            currentTime = getTimer();
            for (var _loc3 = 999; _root.getInstanceAtDepth(_loc3) != undefined; ++_loc3)
            {
            } // end of for
            timerClip = _root.createEmptyMovieClip("__tweenLite_mc", _loc3);
            gs.TweenLite.timerClip._visible = false;
            clearInterval(gs.TweenLite._gcInterval);
            _gcInterval = setInterval(gs.TweenLite.killGarbage, 2000);
            gs.TweenLite.timerClip.onEnterFrame = gs.TweenLite.updateAll;
            if (gs.TweenLite.overwriteManager == undefined)
            {
                overwriteManager = {mode: 1, enabled: false};
            } // end if
            _tlInitted = true;
        } // end if
        vars = $vars;
        duration = $duration || 1.000000E-003;
        delay = $vars.delay || 0;
        combinedTimeScale = $vars.timeScale || 1;
        active = Boolean($duration == 0 && delay == 0);
        target = $target;
        if (typeof(vars.ease) != "function")
        {
            vars.ease = gs.TweenLite.defaultEase;
        } // end if
        if (vars.easeParams != undefined)
        {
            vars.proxiedEase = vars.ease;
            vars.ease = easeProxy;
        } // end if
        ease = vars.ease;
        tweens = [];
        initted = false;
        initTime = gs.TweenLite.currentTime;
        startTime = initTime + delay * 1000;
        endTargetID = gs.TweenLite.getID($target, true);
        var _loc6 = $vars.overwrite == undefined || !gs.TweenLite.overwriteManager.enabled && $vars.overwrite > 1 ? (gs.TweenLite.overwriteManager.mode) : (Number($vars.overwrite));
        if (_loc6 == 1 && $target != undefined)
        {
            delete gs.TweenLite.masterList[endTargetID];
            gs.TweenLite.masterList[endTargetID] = {target: $target, tweens: [this]};
        }
        else
        {
            gs.TweenLite.masterList[endTargetID].tweens.push(this);
        } // end else if
        if (active || vars.runBackwards == true && vars.renderOnStart != true)
        {
            this.initTweenVals();
            if (active)
            {
                this.render(startTime + 1);
            }
            else
            {
                this.render(startTime);
            } // end else if
            if (vars._visible != undefined && vars.runBackwards == true)
            {
                target._visible = vars._visible;
            } // end if
        } // end if
    } // End of the function
    function initTweenVals()
    {
        var _loc2;
        var _loc5;
        var _loc4;
        if (vars.timeScale != undefined && target instanceof gs.TweenLite)
        {
            tweens[tweens.length] = new gs.utils.tween.TweenInfo(target, "timeScale", target.timeScale, vars.timeScale - target.timeScale, "timeScale", false);
        } // end if
        for (var _loc2 in vars)
        {
            if (gs.TweenLite._reservedProps[_loc2] != undefined)
            {
                continue;
            } // end if
            if (gs.TweenLite.plugins[_loc2] != undefined)
            {
                _loc4 = new gs.TweenLite.plugins[_loc2]();
                if (_loc4.onInitTween(target, vars[_loc2], this) == false)
                {
                    tweens[tweens.length] = new gs.utils.tween.TweenInfo(target, _loc2, target[_loc2], typeof(vars[_loc2]) == "number" ? (vars[_loc2] - target[_loc2]) : (Number(vars[_loc2])), _loc2, false);
                }
                else
                {
                    tweens[tweens.length] = new gs.utils.tween.TweenInfo(_loc4, "changeFactor", 0, 1, _loc4.overwriteProps.length == 1 ? (_loc4.overwriteProps[0]) : ("_MULTIPLE_"), true);
                    _hasPlugins = true;
                } // end else if
                continue;
            } // end if
            tweens[tweens.length] = new gs.utils.tween.TweenInfo(target, _loc2, target[_loc2], typeof(vars[_loc2]) == "number" ? (vars[_loc2] - target[_loc2]) : (Number(vars[_loc2])), _loc2, false);
        } // end of for...in
        if (vars.runBackwards == true)
        {
            var _loc3;
            for (var _loc5 = tweens.length - 1; _loc5 > -1; --_loc5)
            {
                _loc3 = tweens[_loc5];
                _loc3.start = _loc3.start + _loc3.change;
                _loc3.change = -_loc3.change;
            } // end of for
        } // end if
        if (vars.onUpdate != null)
        {
            _hasUpdate = true;
        } // end if
        if (gs.TweenLite.overwriteManager.enabled && gs.TweenLite.masterList[endTargetID] != undefined)
        {
            gs.TweenLite.overwriteManager.manageOverwrites(this, gs.TweenLite.masterList[endTargetID].tweens);
        } // end if
        initted = true;
    } // End of the function
    function activate()
    {
        started = active = true;
        if (!initted)
        {
            this.initTweenVals();
        } // end if
        if (vars.onStart != undefined)
        {
            vars.onStart.apply(vars.onStartScope, vars.onStartParams);
        } // end if
        if (duration == 1.000000E-003)
        {
            startTime = startTime - 1;
        } // end if
    } // End of the function
    function render($t)
    {
        var _loc5 = ($t - startTime) * 1.000000E-003;
        var _loc4;
        var _loc2;
        var _loc3;
        if (_loc5 >= duration)
        {
            _loc5 = duration;
            _loc4 = ease == vars.ease || duration == 1.000000E-003 ? (1) : (0);
        }
        else
        {
            _loc4 = this.ease(_loc5, 0, 1, duration);
        } // end else if
        for (var _loc3 = tweens.length - 1; _loc3 > -1; --_loc3)
        {
            _loc2 = tweens[_loc3];
            _loc2.target[_loc2.property] = _loc2.start + _loc4 * _loc2.change;
        } // end of for
        if (_hasUpdate)
        {
            vars.onUpdate.apply(vars.onUpdateScope, vars.onUpdateParams);
        } // end if
        if (_loc5 == duration)
        {
            this.complete(true);
        } // end if
    } // End of the function
    function complete($skipRender)
    {
        if ($skipRender != true)
        {
            if (!initted)
            {
                this.initTweenVals();
            } // end if
            startTime = gs.TweenLite.currentTime - duration * 1000 / combinedTimeScale;
            this.render(gs.TweenLite.currentTime);
            return;
        } // end if
        if (_hasPlugins)
        {
            for (var _loc2 = tweens.length - 1; _loc2 > -1; --_loc2)
            {
                if (tweens[_loc2].isPlugin == true && tweens[_loc2].target.onComplete != undefined)
                {
                    tweens[_loc2].target.onComplete();
                } // end if
            } // end of for
        } // end if
        if (vars.persist != true)
        {
            this.__set__enabled(false);
        } // end if
        if (vars.onComplete)
        {
            vars.onComplete.apply(vars.onCompleteScope, vars.onCompleteParams);
        } // end if
    } // End of the function
    function clear()
    {
        tweens = [];
        vars = {ease: vars.ease};
        _hasUpdate = false;
    } // End of the function
    function killVars($vars)
    {
        if (gs.TweenLite.overwriteManager.enabled)
        {
            gs.TweenLite.overwriteManager.killVars($vars, vars, tweens);
        } // end if
    } // End of the function
    static function to($target, $duration, $vars)
    {
        return (new gs.TweenLite($target, $duration, $vars));
    } // End of the function
    static function from($target, $duration, $vars)
    {
        $vars.runBackwards = true;
        return (new gs.TweenLite($target, $duration, $vars));
    } // End of the function
    static function delayedCall($delay, $onComplete, $onCompleteParams, $onCompleteScope)
    {
        return (new gs.TweenLite($onComplete, 0, {delay: $delay, onComplete: $onComplete, onCompleteParams: $onCompleteParams, onCompleteScope: $onCompleteScope, overwrite: 0}));
    } // End of the function
    static function updateAll()
    {
        var _loc4 = currentTime = getTimer();
        var _loc5 = gs.TweenLite.masterList;
        var _loc6;
        var _loc3;
        var _loc2;
        var _loc1;
        for (var _loc6 in _loc5)
        {
            _loc3 = _loc5[_loc6].tweens;
            for (var _loc2 = _loc3.length - 1; _loc2 > -1; --_loc2)
            {
                _loc1 = _loc3[_loc2];
                if (_loc1.active)
                {
                    _loc1.render(_loc4);
                    continue;
                } // end if
                if (_loc1.gc)
                {
                    _loc3.splice(_loc2, 1);
                    continue;
                } // end if
                if (_loc4 >= _loc1.startTime)
                {
                    _loc1.activate();
                    _loc1.render(_loc4);
                } // end if
            } // end of for
        } // end of for...in
    } // End of the function
    static function getID($target, $lookup)
    {
        var _loc3;
        if ($lookup)
        {
            var _loc1 = gs.TweenLite.masterList;
            if (typeof($target) == "movieclip")
            {
                if (_loc1[String($target)] != undefined)
                {
                    return (String($target));
                }
                else
                {
                    _loc3 = String($target);
                    gs.TweenLite.masterList[_loc3] = {target: $target, tweens: []};
                    return (_loc3);
                } // end else if
            }
            else
            {
                for (var _loc4 in _loc1)
                {
                    if (_loc1[_loc4].target == $target)
                    {
                        return (_loc4);
                    } // end if
                } // end of for...in
            } // end if
        } // end else if
        _cnt = ++gs.TweenLite._cnt;
        _loc3 = "t" + gs.TweenLite._cnt;
        gs.TweenLite.masterList[_loc3] = {target: $target, tweens: []};
        return (_loc3);
    } // End of the function
    static function removeTween($t, $clear)
    {
        if ($clear != false)
        {
            $t.clear();
        } // end if
        $t.__set__enabled(false);
    } // End of the function
    static function killTweensOf($target, $complete)
    {
        var _loc5 = gs.TweenLite.getID($target, true);
        var _loc3 = gs.TweenLite.masterList[_loc5];
        var _loc2;
        var _loc1;
        if (_loc3 != undefined)
        {
            for (var _loc2 = _loc3.length - 1; _loc2 > -1; --_loc2)
            {
                _loc1 = _loc3[_loc2];
                if ($complete && !_loc1.gc)
                {
                    _loc1.complete(false);
                } // end if
                _loc1.clear();
            } // end of for
            delete gs.TweenLite.masterList[_loc5];
        } // end if
    } // End of the function
    static function killGarbage()
    {
        var _loc1 = gs.TweenLite.masterList;
        var _loc2;
        var _loc3;
        for (var _loc2 in _loc1)
        {
            if (_loc1[_loc2].tweens.length == 0)
            {
                delete _loc1[_loc2];
            } // end if
        } // end of for...in
    } // End of the function
    static function defaultEase($t, $b, $c, $d)
    {
        $t = $t / $d;
        return (-$c * ($t) * ($t - 2) + $b);
    } // End of the function
    function easeProxy($t, $b, $c, $d)
    {
        return (vars.proxiedEase.apply(null, arguments.concat(vars.easeParams)));
    } // End of the function
    function get enabled()
    {
        return (gc ? (false) : (true));
    } // End of the function
    function set enabled($b)
    {
        if ($b)
        {
            if (gs.TweenLite.masterList[endTargetID] == undefined)
            {
                gs.TweenLite.masterList[endTargetID] = {target: target, tweens: [this]};
            }
            else
            {
                var _loc3 = gs.TweenLite.masterList[endTargetID].tweens;
                var _loc4;
                var _loc2;
                for (var _loc2 = _loc3.length - 1; _loc2 > -1; --_loc2)
                {
                    if (_loc3[_loc2] == this)
                    {
                        _loc4 = true;
                        break;
                    } // end if
                } // end of for
                if (!_loc4)
                {
                    _loc3[_loc3.length] = this;
                } // end if
            } // end if
        } // end else if
        gc = $b ? (false) : (true);
        if (gc)
        {
            active = false;
        }
        else
        {
            active = started;
        } // end else if
        //return (this.enabled());
        null;
    } // End of the function
    static var version = 1.009000E+001;
    static var killDelayedCallsTo = gs.TweenLite.killTweensOf;
    static var masterList = {};
    static var plugins = {};
    static var _cnt = -16000;
    static var _reservedProps = {ease: 1, delay: 1, overwrite: 1, onComplete: 1, onCompleteParams: 1, runBackwards: 1, startAt: 1, onUpdate: 1, onUpdateParams: 1, roundProps: 1, onStart: 1, onStartParams: 1, persist: 1, renderOnStart: 1, proxiedEase: 1, easeParams: 1, yoyo: 1, loop: 1, onCompleteListener: 1, onUpdateListener: 1, onStartListener: 1, orientToBezier: 1, timeScale: 1};
} // End of Class