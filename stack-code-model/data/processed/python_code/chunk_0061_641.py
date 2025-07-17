class mx.transitions.Squeeze extends mx.transitions.Transition
{
    var _scaleProp, __get__manager, _scaleFinal, _content;
    function Squeeze(content, transParams, manager)
    {
        super();
        this.init(content, transParams, manager);
    } // End of the function
    function init(content, transParams, manager)
    {
        super.init(content, transParams, manager);
        if (transParams.dimension)
        {
            _scaleProp = "_yscale";
            _scaleFinal = this.__get__manager().__get__contentAppearance()._yscale;
        }
        else
        {
            _scaleProp = "_xscale";
            _scaleFinal = this.__get__manager().__get__contentAppearance()._xscale;
        } // end else if
    } // End of the function
    function _render(p)
    {
        if (p <= 0)
        {
            p = 0;
            _content._visible = false;
        }
        else
        {
            _content._visible = true;
        } // end else if
        _content[_scaleProp] = p * _scaleFinal;
    } // End of the function
    static var version = "1.1.0.52";
    var type = mx.transitions.Squeeze;
    var className = "Squeeze";
} // End of Class