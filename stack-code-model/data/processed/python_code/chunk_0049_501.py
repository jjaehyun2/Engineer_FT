class mx.transitions.Wipe extends mx.transitions.Transition
{
    var _mask, _content, getNextHighestDepthMC, __get__direction, _innerMask, drawBox, _cornerMode, _innerBounds;
    function Wipe(content, transParams, manager)
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
        var _loc4 = _mask = _loc5.createEmptyMovieClip("__mask_Wipe_" + this.__get__direction(), _loc6);
        var _loc2 = _innerMask = _mask.createEmptyMovieClip("innerMask", 0);
        _loc2._x = _loc2._y = 50;
        _loc4._visible = false;
        _loc2.beginFill(16711680);
        this.drawBox(_loc2, -50, -50, 100, 100);
        _loc2.endFill();
        switch (_startPoint)
        {
            case 3:
            case 2:
            {
                _loc2._rotation = 90;
                break;
            } 
            case 1:
            case 4:
            {
                _loc2._rotation = 0;
                break;
            } 
            case 9:
            case 6:
            {
                _loc2._rotation = 180;
                break;
            } 
            case 7:
            case 8:
            {
                _loc2._rotation = -90;
                break;
            } 
            default:
            {
                break;
            } 
        } // End of switch
        if (_startPoint % 2)
        {
            _cornerMode = true;
        } // end if
        var _loc3 = _innerBounds;
        _loc4._x = _loc3.xMin;
        _loc4._y = _loc3.yMin;
        _loc4._width = _loc3.xMax - _loc3.xMin;
        _loc4._height = _loc3.yMax - _loc3.yMin;
    } // End of the function
    function _render(p)
    {
        _innerMask.clear();
        _innerMask.beginFill(16711680);
        if (_cornerMode)
        {
            this._drawSlant(_innerMask, p);
        }
        else
        {
            this.drawBox(_innerMask, -50, -50, p * 100, 100);
        } // end else if
        _innerMask.endFill();
    } // End of the function
    function _drawSlant(mc, p)
    {
        mc.moveTo(-50, -50);
        if (p <= 5.000000E-001)
        {
            mc.lineTo(200 * (p - 2.500000E-001), -50);
            mc.lineTo(-50, 200 * (p - 2.500000E-001));
        }
        else
        {
            mc.lineTo(50, -50);
            mc.lineTo(50, 200 * (p - 7.500000E-001));
            mc.lineTo(200 * (p - 7.500000E-001), 50);
            mc.lineTo(-50, 50);
        } // end else if
        mc.lineTo(-50, -50);
    } // End of the function
    static var version = "1.1.0.52";
    var type = mx.transitions.Wipe;
    var className = "Wipe";
    var _startPoint = 4;
} // End of Class