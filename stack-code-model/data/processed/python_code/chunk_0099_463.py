class mx.transitions.Fly extends mx.transitions.Transition
{
    var __get__manager, _xFinal, _yFinal, _stagePoints, _content, _innerBounds, _xInitial, _yInitial;
    function Fly(content, transParams, manager)
    {
        super();
        this.init(content, transParams, manager);
    } // End of the function
    function init(content, transParams, manager)
    {
        super.init(content, transParams, manager);
        if (transParams.startPoint)
        {
            _startPoint = transParams.startPoint;
        } // end if
        _xFinal = this.__get__manager().__get__contentAppearance()._x;
        _yFinal = this.__get__manager().__get__contentAppearance()._y;
        var _loc6 = Stage.scaleMode;
        Stage.scaleMode = "showAll";
        var _loc3 = _stagePoints = {};
        _loc3[1] = {x: 0, y: 0};
        _loc3[2] = {x: 0, y: 0};
        _loc3[3] = {x: Stage.width, y: 0};
        _loc3[4] = {x: 0, y: 0};
        _loc3[5] = {x: Stage.width / 2, y: Stage.height / 2};
        _loc3[6] = {x: Stage.width, y: 0};
        _loc3[7] = {x: 0, y: Stage.height};
        _loc3[8] = {x: 0, y: Stage.height};
        _loc3[9] = {x: Stage.width, y: Stage.height};
        for (var _loc5 in _loc3)
        {
            _content._parent.globalToLocal(_loc3[_loc5]);
        } // end of for...in
        var _loc4 = _innerBounds;
        _loc3[1].x = _loc3[1].x - _loc4.xMax;
        _loc3[1].y = _loc3[1].y - _loc4.yMax;
        _loc3[2].x = this.__get__manager().__get__contentAppearance()._x;
        _loc3[2].y = _loc3[2].y - _loc4.yMax;
        _loc3[3].x = _loc3[3].x - _loc4.xMin;
        _loc3[3].y = _loc3[3].y - _loc4.yMax;
        _loc3[4].x = _loc3[4].x - _loc4.xMax;
        _loc3[4].y = this.__get__manager().__get__contentAppearance()._y;
        _loc3[5].x = _loc3[5].x - (_loc4.xMax + _loc4.xMin) / 2;
        _loc3[5].y = _loc3[5].y - (_loc4.yMax + _loc4.yMin) / 2;
        _loc3[6].x = _loc3[6].x - _loc4.xMin;
        _loc3[6].y = this.__get__manager().__get__contentAppearance()._y;
        _loc3[7].x = _loc3[7].x - _loc4.xMax;
        _loc3[7].y = _loc3[7].y - _loc4.yMin;
        _loc3[8].x = this.__get__manager().__get__contentAppearance()._x;
        _loc3[8].y = _loc3[8].y - _loc4.yMin;
        _loc3[9].x = _loc3[9].x - _loc4.xMin;
        _loc3[9].y = _loc3[9].y - _loc4.yMin;
        _xInitial = _stagePoints[_startPoint].x;
        _yInitial = _stagePoints[_startPoint].y;
        Stage.scaleMode = _loc6;
    } // End of the function
    function _render(p)
    {
        _content._x = _xFinal + (_xInitial - _xFinal) * (1 - p);
        _content._y = _yFinal + (_yInitial - _yFinal) * (1 - p);
    } // End of the function
    static var version = "1.1.0.52";
    var type = mx.transitions.Fly;
    var className = "Fly";
    var _startPoint = 4;
} // End of Class