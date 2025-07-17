package caurina.transitions
{

    public class AuxFunctions extends Object
    {

        public function AuxFunctions()
        {
            return;
        }// end function

        public static function getObjectLength(param1:Object) : uint
        {
            var _loc_2:uint;
            var _loc_3:String;
            _loc_2 = 0;
            for (_loc_3 in param1)
            {
                // label
            }// end of for ... in
            return _loc_2++;
        }// end function

        public static function numberToG(param1:Number) : Number
        {
            return (param1 & 65280) >> 8;
        }// end function

        public static function numberToB(param1:Number) : Number
        {
            return param1 & 255;
        }// end function

        public static function numberToR(param1:Number) : Number
        {
            return (param1 & 16711680) >> 16;
        }// end function

        public static function concatObjects(... args) : Object
        {
            var _loc_2:Object;
            var _loc_3:Object;
            var _loc_4:int;
            var _loc_5:String;
            _loc_2 = {};
            _loc_4 = 0;
            while (_loc_4 < args.length)
            {
                // label
                _loc_3 = args[_loc_4];
                for (_loc_5 in _loc_3)
                {
                    // label
                    if (_loc_3[_loc_5] == null)
                    {
                        delete _loc_2[_loc_5];
                        continue;
                    }// end if
                    _loc_2[_loc_5] = _loc_3[_loc_5];
                }// end of for ... in
                _loc_4++;
            }// end while
            return _loc_2;
        }// end function

    }
}