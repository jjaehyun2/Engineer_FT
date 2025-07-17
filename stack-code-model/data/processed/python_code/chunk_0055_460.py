class mx.transitions.Transition
{
    var _manager, removeEventListener, addEventListener, __get__manager, _content, _twn, __get__content, __get__direction, __get__duration, _easing, __get__easing, _progress, dispatchEvent, __get__progress, __set__content, __set__direction, __set__duration, __set__easing, __set__manager, _innerBounds, _outerBounds, _width, _height, __set__progress;
    function Transition(content, transParams, manager)
    {
        if (!arguments.length)
        {
            return;
        } // end if
        this.init(content, transParams, manager);
    } // End of the function
    function set manager(mgr)
    {
        if (_manager != undefined)
        {
            this.removeEventListener("transitionInDone", _manager);
            this.removeEventListener("transitionOutDone", _manager);
            this.removeEventListener("transitionProgress", _manager);
        } // end if
        _manager = mgr;
        this.addEventListener("transitionInDone", _manager);
        this.addEventListener("transitionOutDone", _manager);
        this.addEventListener("transitionProgress", _manager);
        //return (this.manager());
        null;
    } // End of the function
    function get manager()
    {
        return (_manager);
    } // End of the function
    function set content(c)
    {
        if (typeof(c) == "movieclip")
        {
            _content = c;
            _twn.obj = c;
        } // end if
        //return (this.content());
        null;
    } // End of the function
    function get content()
    {
        return (_content);
    } // End of the function
    function set direction(direction)
    {
        _direction = direction ? (1) : (0);
        //return (this.direction());
        null;
    } // End of the function
    function get direction()
    {
        return (_direction);
    } // End of the function
    function set duration(d)
    {
        if (d)
        {
            _duration = d;
            _twn.duration = d;
        } // end if
        //return (this.duration());
        null;
    } // End of the function
    function get duration()
    {
        return (_duration);
    } // End of the function
    function set easing(e)
    {
        if (typeof(e) == "string")
        {
            e = eval(e);
        }
        else if (e == undefined)
        {
            e = this._noEase;
        } // end else if
        this._easing = e;
        this._twn.easing = e;
        //return (this.easing());
        null;
    } // End of the function
    function get easing()
    {
        return (_easing);
    } // End of the function
    function set progress(p)
    {
        if (_progress == p)
        {
            return;
        } // end if
        _progress = p;
        if (_direction)
        {
            this._render(1 - p);
        }
        else
        {
            this._render(p);
        } // end else if
        this.dispatchEvent({type: "transitionProgress", target: this, progress: p});
        //return (this.progress());
        null;
    } // End of the function
    function get progress()
    {
        return (_progress);
    } // End of the function
    function init(content, transParams, manager)
    {
        this.__set__content(content);
        this.__set__direction(transParams.direction);
        this.__set__duration(transParams.duration);
        this.__set__easing(transParams.easing);
        this.__set__manager(manager);
        _innerBounds = this.__get__manager()._innerBounds;
        _outerBounds = this.__get__manager()._outerBounds;
        _width = this.__get__manager()._width;
        _height = this.__get__manager()._height;
        this._resetTween();
    } // End of the function
    function toString()
    {
        return ("[Transition " + className + "]");
    } // End of the function
    function start()
    {
        this.__get__content()._visible = true;
        _twn.start();
    } // End of the function
    function stop()
    {
        _twn.fforward();
        _twn.stop();
    } // End of the function
    function cleanUp()
    {
        this.removeEventListener("transitionInDone", _manager);
        this.removeEventListener("transitionOutDone", _manager);
        this.removeEventListener("transitionProgress", _manager);
        this.stop();
    } // End of the function
    function getNextHighestDepthMC(mc)
    {
        var _loc4 = mc.getNextHighestDepth();
        if (_loc4 != undefined)
        {
            return (_loc4);
        }
        else
        {
            _loc4 = -1;
            var _loc3;
            var _loc1;
            for (var _loc5 in mc)
            {
                _loc1 = mc[_loc5];
                if (typeof(_loc1) == "movieclip" && _loc1._parent == mc)
                {
                    _loc3 = _loc1.getDepth();
                    if (_loc3 > _loc4)
                    {
                        _loc4 = _loc3;
                    } // end if
                } // end if
            } // end of for...in
            return (_loc4 + 1);
        } // end else if
    } // End of the function
    function drawBox(mc, x, y, w, h)
    {
        mc.moveTo(x, y);
        mc.lineTo(x + w, y);
        mc.lineTo(x + w, y + h);
        mc.lineTo(x, y + h);
        mc.lineTo(x, y);
    } // End of the function
    function drawCircle(mc, x, y, r)
    {
        mc.moveTo(x + r, y);
        mc.curveTo(r + x, 4.142136E-001 * r + y, 7.071068E-001 * r + x, 7.071068E-001 * r + y);
        mc.curveTo(4.142136E-001 * r + x, r + y, x, r + y);
        mc.curveTo(-4.142136E-001 * r + x, r + y, -7.071068E-001 * r + x, 7.071068E-001 * r + y);
        mc.curveTo(-r + x, 4.142136E-001 * r + y, -r + x, y);
        mc.curveTo(-r + x, -4.142136E-001 * r + y, -7.071068E-001 * r + x, -7.071068E-001 * r + y);
        mc.curveTo(-4.142136E-001 * r + x, -r + y, x, -r + y);
        mc.curveTo(4.142136E-001 * r + x, -r + y, 7.071068E-001 * r + x, -7.071068E-001 * r + y);
        mc.curveTo(r + x, -4.142136E-001 * r + y, r + x, y);
    } // End of the function
    function _render(p)
    {
    } // End of the function
    function _resetTween()
    {
        _twn.stop();
        _twn.removeListener(this);
        _twn = new mx.transitions.Tween(this, null, this.__get__easing(), 0, 1, this.__get__duration(), true);
        _twn.stop();
        _twn.prop = "progress";
        _twn.addListener(this);
    } // End of the function
    function _noEase(t, b, c, d)
    {
        return (c * t / d + b);
    } // End of the function
    function onMotionFinished(src)
    {
        if (this.__get__direction())
        {
            this.dispatchEvent({type: "transitionOutDone", target: this});
        }
        else
        {
            this.dispatchEvent({type: "transitionInDone", target: this});
        } // end else if
    } // End of the function
    static var version = "1.1.0.52";
    static var IN = 0;
    static var OUT = 1;
    var type = mx.transitions.Transition;
    var className = "Transition";
    var _direction = 0;
    var _duration = 2;
    static var __mixinFED = mx.events.EventDispatcher.initialize(mx.transitions.Transition.prototype);
} // End of Class