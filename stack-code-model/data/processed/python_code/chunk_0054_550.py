package 
{
    import Array.*;

    dynamic public class Array extends Object
    {
        public static const CASEINSENSITIVE:uint = 1;
        public static const DESCENDING:uint = 2;
        public static const UNIQUESORT:uint = 4;
        public static const RETURNINDEXEDARRAY:uint = 8;
        public static const NUMERIC:uint = 16;
        public static const length:int = 1;

        public function Array(... args)
        {
            var _loc_3:* = NaN;
            var _loc_4:* = 0;
            var _loc_5:* = 0;
            args = args.length;
            if (args == 1)
            {
            }
            if (args[0] is Number)
            {
                _loc_3 = args[0];
                _loc_4 = _loc_3;
                if (_loc_4 != _loc_3)
                {
                    Error.throwError(RangeError, 1005, _loc_3);
                }
                this.length = _loc_4;
            }
            else
            {
                this.length = args;
                _loc_5 = 0;
                while (_loc_5 < args)
                {
                    
                    this[_loc_5] = args[_loc_5];
                    _loc_5 = _loc_5 + 1;
                }
            }
            return;
        }// end function

        public function get length() : uint;

        public function set length(param1:uint);

        private function set_length(param1, param2:uint)
        {
            if (param1 is uint)
            {
                this.length = param1;
            }
            else if (bugzilla(661330))
            {
                Error.throwError(RangeError, 2108, param1);
            }
            else
            {
                this.length = param2;
            }
            return;
        }// end function

        function join(param1 = undefined) : String
        {
            return _join(this, param1);
        }// end function

        function pop();

        function push(... args) : uint;

        function reverse() : Array
        {
            return _reverse(this);
        }// end function

        function concat(... args) : Array
        {
            return _concat(this, args);
        }// end function

        function shift()
        {
            return _shift(this);
        }// end function

        function slice(param1 = 0, param2 = 4.29497e+009) : Array
        {
            return _slice(this, Number(param1), Number(param2));
        }// end function

        function unshift(... args) : uint;

        function splice(... args)
        {
            if (!args.length)
            {
                return undefined;
            }
            return _splice(this, args);
        }// end function

        function sort(... args)
        {
            return _sort(this, args);
        }// end function

        function sortOn(param1, param2 = 0, ... args)
        {
            return _sortOn(this, param1, param2);
        }// end function

        function indexOf(param1, param2 = 0) : int
        {
            return _indexOf(this, param1, int(param2));
        }// end function

        function lastIndexOf(param1, param2 = 2147483647) : int
        {
            return _lastIndexOf(this, param1, int(param2));
        }// end function

        function every(param1:Function, param2 = null) : Boolean
        {
            return _every(this, param1, param2);
        }// end function

        function filter(param1:Function, param2 = null) : Array
        {
            return _filter(this, param1, param2);
        }// end function

        function forEach(param1:Function, param2 = null) : void
        {
            _forEach(this, param1, param2);
            return;
        }// end function

        function map(param1:Function, param2 = null) : Array
        {
            return _map(this, param1, param2);
        }// end function

        function some(param1:Function, param2 = null) : Boolean
        {
            return _some(this, param1, param2);
        }// end function

        private static function _join(param1, param2) : String
        {
            var _loc_7:* = undefined;
            var _loc_3:* = param2 === undefined ? (",") : (String(param2));
            var _loc_4:* = "";
            var _loc_5:* = 0;
            var _loc_6:* = uint(param1.length);
            while (_loc_5 < _loc_6)
            {
                
                _loc_7 = param1[_loc_5];
                if (_loc_7 != null)
                {
                    _loc_4 = _loc_4 + _loc_7;
                }
                if ((_loc_5 + 1) < _loc_6)
                {
                    _loc_4 = _loc_4 + _loc_3;
                }
                _loc_5 = _loc_5 + 1;
            }
            return _loc_4;
        }// end function

        private static function _pop(param1);

        private static function _reverse(param1);

        private static function _concat(param1, param2:Array) : Array;

        private static function _shift(param1);

        private static function _slice(param1, param2:Number, param3:Number) : Array;

        private static function _unshift(param1, param2:Array) : uint;

        private static function _splice(param1, param2:Array) : Array;

        private static function _sort(param1, param2:Array);

        private static function _sortOn(param1, param2, param3);

        private static function _indexOf(param1, param2, param3:int) : int;

        private static function _lastIndexOf(param1, param2, param3:int = 0) : int;

        private static function _every(param1, param2:Function, param3) : Boolean;

        private static function _filter(param1, param2:Function, param3) : Array;

        private static function _forEach(param1, param2:Function, param3) : void;

        private static function _map(param1, param2:Function, param3) : Array;

        private static function _some(param1, param2:Function, param3) : Boolean;

        prototype.join = function (param1 = undefined) : String
        {
            return _join(this, param1);
        }// end function
        ;
        prototype.pop = function ()
        {
            return _pop(this);
        }// end function
        ;
        prototype.toString = function () : String
        {
            var _loc_1:* = this;
            return _join(_loc_1, ",");
        }// end function
        ;
        prototype.toLocaleString = function () : String
        {
            var _loc_5:* = undefined;
            var _loc_1:* = this;
            var _loc_2:* = "";
            var _loc_3:* = 0;
            var _loc_4:* = _loc_1.length;
            while (_loc_3 < _loc_4)
            {
                
                _loc_5 = _loc_1[_loc_3];
                if (_loc_5 != null)
                {
                    _loc_2 = _loc_2 + _loc_5.toLocaleString();
                }
                if ((_loc_3 + 1) < _loc_4)
                {
                    _loc_2 = _loc_2 + ",";
                }
                _loc_3 = _loc_3 + 1;
            }
            return _loc_2;
        }// end function
        ;
        prototype.push = function (... args) : uint
        {
            args = uint(this.length);
            var _loc_3:* = 0;
            var _loc_4:* = args.length;
            while (_loc_3 < _loc_4)
            {
                
                var _loc_5:* = args + 1;
                this[_loc_5] = args[_loc_3];
                _loc_3 = _loc_3 + 1;
            }
            this.length = _loc_2;
            return _loc_2;
        }// end function
        ;
        prototype.reverse = function ()
        {
            return _reverse(this);
        }// end function
        ;
        prototype.concat = function (... args) : Array
        {
            return _concat(this, args);
        }// end function
        ;
        prototype.shift = function ()
        {
            return _shift(this);
        }// end function
        ;
        prototype.slice = function (param1 = 0, param2 = 4.29497e+009) : Array
        {
            return _slice(this, Number(param1), Number(param2));
        }// end function
        ;
        prototype.unshift = function (... args) : uint
        {
            var _loc_4:* = 0;
            var _loc_6:* = 0;
            if (this is Array)
            {
                return _unshift(this, args);
            }
            args = uint(this.length);
            var _loc_3:* = args.length;
            _loc_4 = args;
            while (_loc_4 > 0)
            {
                
                _loc_4 = _loc_4 - 1;
                _loc_6 = _loc_4 + _loc_3;
                if (_loc_4 in this)
                {
                    this[_loc_6] = this[_loc_4];
                    continue;
                }
                delete this[_loc_6];
            }
            var _loc_5:* = 0;
            while (_loc_5 < _loc_3)
            {
                
                var _loc_7:* = _loc_4 + 1;
                this[_loc_7] = args[_loc_5];
                _loc_5 = _loc_5 + 1;
            }
            args = args + _loc_3;
            this.length = args;
            return args;
        }// end function
        ;
        prototype.splice = function (... args)
        {
            if (!args.length)
            {
                return undefined;
            }
            return _splice(this, args);
        }// end function
        ;
        prototype.sort = function (... args)
        {
            return _sort(this, args);
        }// end function
        ;
        prototype.sortOn = function (param1, param2 = 0, ... args)
        {
            return _sortOn(this, param1, param2);
        }// end function
        ;
        prototype.indexOf = function (param1, param2 = 0) : int
        {
            return _indexOf(this, param1, int(param2));
        }// end function
        ;
        prototype.lastIndexOf = function (param1, param2 = 2147483647) : int
        {
            return _lastIndexOf(this, param1, int(param2));
        }// end function
        ;
        prototype.every = function (param1:Function, param2 = null) : Boolean
        {
            return _every(this, param1, param2);
        }// end function
        ;
        prototype.filter = function (param1:Function, param2 = null) : Array
        {
            return _filter(this, param1, param2);
        }// end function
        ;
        prototype.forEach = function (param1:Function, param2 = null) : void
        {
            _forEach(this, param1, param2);
            return;
        }// end function
        ;
        prototype.map = function (param1:Function, param2 = null) : Array
        {
            return _map(this, param1, param2);
        }// end function
        ;
        prototype.some = function (param1:Function, param2 = null) : Boolean
        {
            return _some(this, param1, param2);
        }// end function
        ;
        _dontEnumPrototype(prototype);
    }
}