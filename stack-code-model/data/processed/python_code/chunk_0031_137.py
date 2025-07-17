package 
{

    dynamic public class RegExp extends Object
    {
        public static const length:int = 1;

        public function RegExp(param1 = undefined, param2 = undefined)
        {
            return;
        }// end function

        public function get source() : String;

        public function get global() : Boolean;

        public function get ignoreCase() : Boolean;

        public function get multiline() : Boolean;

        public function get lastIndex() : int;

        public function set lastIndex(param1:int);

        public function get dotall() : Boolean;

        public function get extended() : Boolean;

        function exec(param1:String = "");

        function test(param1:String = "") : Boolean
        {
            return this.exec(param1) != null;
        }// end function

        prototype.toString = function () : String
        {
            var _loc_1:* = this;
            var _loc_2:* = "/" + _loc_1.source + "/";
            if (_loc_1.global)
            {
                _loc_2 = _loc_2 + "g";
            }
            if (_loc_1.ignoreCase)
            {
                _loc_2 = _loc_2 + "i";
            }
            if (_loc_1.multiline)
            {
                _loc_2 = _loc_2 + "m";
            }
            if (_loc_1.dotall)
            {
                _loc_2 = _loc_2 + "s";
            }
            if (_loc_1.extended)
            {
                _loc_2 = _loc_2 + "x";
            }
            return _loc_2;
        }// end function
        ;
        prototype.exec = function (param1 = "")
        {
            var _loc_2:* = this;
            return _loc_2.exec(String(param1));
        }// end function
        ;
        prototype.test = function (param1 = "") : Boolean
        {
            var _loc_2:* = this;
            return _loc_2.test(String(param1));
        }// end function
        ;
        _dontEnumPrototype(prototype);
    }
}