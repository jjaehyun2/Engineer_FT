package 
{

    final public class Namespace extends Object
    {
        public static const length:Object = 2;

        public function Namespace(param1 = undefined, param2 = undefined)
        {
            return;
        }// end function

        public function get prefix();

        public function get uri() : String;

        function valueOf() : String
        {
            return this.uri;
        }// end function

        function toString() : String
        {
            return this.uri;
        }// end function

        prototype.valueOf = function () : String
        {
            if (prototype === this)
            {
                return "";
            }
            var _loc_1:* = this;
            return _loc_1.uri;
        }// end function
        ;
        prototype.toString = function () : String
        {
            if (prototype === this)
            {
                return "";
            }
            var _loc_1:* = this;
            return _loc_1.toString();
        }// end function
        ;
        _dontEnumPrototype(prototype);
    }
}