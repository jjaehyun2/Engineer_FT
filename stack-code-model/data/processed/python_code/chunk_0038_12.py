package 
{

    dynamic public class Function extends Object
    {
        public static const length:int = 1;

        public function Function()
        {
            return;
        }// end function

        public function get prototype();

        public function set prototype(param1);

        public function get length() : int;

        function call(param1 = undefined, ... args);

        function apply(param1 = undefined, param2 = undefined);

        public static function createEmptyFunction() : Function
        {
            return function ()
            {
                return;
            }// end function
            ;
        }// end function

        var _loc_1:* = function () : String
        {
            var _loc_1:* = this;
            return "function Function() {}";
        }// end function
        ;
        prototype.toString = function () : String
        {
            var _loc_1:* = this;
            return "function Function() {}";
        }// end function
        ;
        prototype.toLocaleString = _loc_1;
        prototype.call = function (param1 = undefined, ... args)
        {
            args = this;
            return args.apply(param1, args);
        }// end function
        ;
        prototype.apply = function (param1 = undefined, param2 = undefined)
        {
            var _loc_3:* = this;
            return _loc_3.apply(param1, param2);
        }// end function
        ;
        _dontEnumPrototype(prototype);
    }
}