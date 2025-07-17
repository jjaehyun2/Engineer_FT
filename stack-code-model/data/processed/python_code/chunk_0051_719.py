package 
{

    final class Walker extends Object
    {
        var reviver:Function;

        function Walker(param1:Function)
        {
            this.reviver = param1;
            return;
        }// end function

        function walk(param1:Object, param2:String)
        {
            var _loc_4:* = null;
            var _loc_5:* = 0;
            var _loc_6:* = 0;
            var _loc_7:* = undefined;
            var _loc_8:* = null;
            var _loc_3:* = param1[param2];
            if (_loc_3 is Array)
            {
                _loc_4 = _loc_3 as Array;
                _loc_5 = 0;
                _loc_6 = _loc_4.length;
                while (_loc_5 < _loc_6)
                {
                    
                    _loc_7 = this.walk(_loc_4, String(_loc_5));
                    if (_loc_7 === undefined)
                    {
                        delete _loc_4[_loc_5];
                    }
                    else
                    {
                        _loc_4[_loc_5] = _loc_7;
                    }
                    _loc_5 = _loc_5 + 1;
                }
            }
            else
            {
                if (_loc_3 !== null)
                {
                }
                if (!(_loc_3 is Boolean))
                {
                }
                if (!(_loc_3 is Number))
                {
                }
                if (!(_loc_3 is String))
                {
                    for (_loc_8 in _loc_3)
                    {
                        
                        if (!_loc_3.hasOwnProperty(_loc_8))
                        {
                            break;
                        }
                        _loc_7 = this.walk(_loc_3, _loc_8);
                        if (_loc_7 === undefined)
                        {
                            delete _loc_3[_loc_8];
                            continue;
                        }
                        _loc_3[_loc_8] = _loc_7;
                    }
                }
            }
            return this.reviver.call(param1, param2, _loc_3);
        }// end function

    }
}