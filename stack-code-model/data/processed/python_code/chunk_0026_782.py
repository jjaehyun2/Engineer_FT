class mx.transitions.Photo extends mx.transitions.Transition
{
    var __get__manager, _alphaFinal, _content, _colorControl;
    function Photo(content, transParams, manager)
    {
        super();
        this.init(content, transParams, manager);
    } // End of the function
    function init(content, transParams, manager)
    {
        super.init(content, transParams, manager);
        _alphaFinal = this.__get__manager().__get__contentAppearance()._alpha;
        _colorControl = new Color(_content);
    } // End of the function
    function _render(p)
    {
        var _loc4 = 8.000000E-001;
        var _loc3 = 9.000000E-001;
        var _loc2 = {};
        var _loc5 = 0;
        if (p <= _loc4)
        {
            _content._alpha = _alphaFinal * (p / _loc4);
        }
        else
        {
            _content._alpha = _alphaFinal;
            if (p <= _loc3)
            {
                _loc5 = (p - _loc4) / (_loc3 - _loc4) * 256;
            }
            else
            {
                _loc5 = (1 - (p - _loc3) / (1 - _loc3)) * 256;
            } // end else if
        } // end else if
        _loc2.rb = _loc2.gb = _loc2.bb = _loc5;
        _colorControl.setTransform(_loc2);
    } // End of the function
    static var version = "1.1.0.52";
    var type = mx.transitions.Photo;
    var className = "Photo";
} // End of Class