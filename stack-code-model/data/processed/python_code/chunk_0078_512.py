class mx.transitions.PixelDissolve extends mx.transitions.Transition
{
    var _numSections, _indices, _mask, _content, getNextHighestDepthMC, __get__direction, _innerMask, drawBox, _innerBounds;
    function PixelDissolve(content, transParams, manager)
    {
        super();
        this.init(content, transParams, manager);
    } // End of the function
    function init(content, transParams, manager)
    {
        super.init(content, transParams, manager);
        if (transParams.xSections)
        {
            _xSections = transParams.xSections;
        } // end if
        if (transParams.ySections)
        {
            _ySections = transParams.ySections;
        } // end if
        _numSections = _xSections * _ySections;
        _indices = new Array();
        var _loc3 = _ySections;
        while (_loc3--)
        {
            var _loc4 = _xSections;
            while (_loc4--)
            {
                _indices[_loc3 * _xSections + _loc4] = {x: _loc4, y: _loc3};
            } // end while
        } // end while
        this._shuffleArray(_indices);
        this._initMask();
    } // End of the function
    function start()
    {
        _content.setMask(_mask);
        super.start();
    } // End of the function
    function cleanUp()
    {
        _mask.removeMovieClip();
        super.cleanUp();
    } // End of the function
    function _initMask()
    {
        var _loc5 = _content;
        var _loc6 = this.getNextHighestDepthMC(_loc5);
        var _loc3 = _mask = _loc5.createEmptyMovieClip("__mask_PixelDissolve_" + this.__get__direction(), _loc6);
        _loc3._visible = false;
        var _loc4 = _innerMask = _mask.createEmptyMovieClip("innerMask", 0);
        _loc4.beginFill(16711680);
        this.drawBox(_loc4, 0, 0, 100, 100);
        _loc4.endFill();
        var _loc2 = _innerBounds;
        _loc3._x = _loc2.xMin;
        _loc3._y = _loc2.yMin;
        _loc3._width = _loc2.xMax - _loc2.xMin;
        _loc3._height = _loc2.yMax - _loc2.yMin;
    } // End of the function
    function _shuffleArray(a)
    {
        for (var _loc1 = a.length - 1; _loc1 > 0; --_loc1)
        {
            var _loc3 = random(_loc1 + 1);
            if (_loc3 == _loc1)
            {
                continue;
            } // end if
            var _loc4 = a[_loc1];
            a[_loc1] = a[_loc3];
            a[_loc3] = _loc4;
        } // end of for
    } // End of the function
    function _render(p)
    {
        if (p < 0)
        {
            p = 0;
        } // end if
        if (p > 1)
        {
            p = 1;
        } // end if
        var _loc5 = 100 / _xSections;
        var _loc4 = 100 / _ySections;
        var _loc3 = _indices;
        var _loc6 = _innerMask;
        _loc6.clear();
        _loc6.beginFill(16711680);
        var _loc2 = Math.floor(p * _numSections);
        while (_loc2--)
        {
            this.drawBox(_loc6, _loc3[_loc2].x * _loc5, _loc3[_loc2].y * _loc4, _loc5, _loc4);
        } // end while
        _loc6.endFill();
    } // End of the function
    static var version = "1.1.0.52";
    var type = mx.transitions.PixelDissolve;
    var className = "PixelDissolve";
    var _xSections = 10;
    var _ySections = 10;
} // End of Class