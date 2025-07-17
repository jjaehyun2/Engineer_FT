package __AS3__.vec
{

    final dynamic class Vector$object extends Object
    {

        function Vector$object(param1:uint = 0, param2:Boolean = false)
        {
            return;
        }// end function

        private function newThisType() : Vector$object;

        public function get length() : uint;

        public function set length(param1:uint);

        public function set fixed(param1:Boolean);

        public function get fixed() : Boolean;

        function toString() : String
        {
            return this.join();
        }// end function

        function toLocaleString() : String
        {
            var _loc_5:* = undefined;
            var _loc_1:* = this.length;
            var _loc_2:* = ",";
            var _loc_3:* = "";
            var _loc_4:* = 0;
            if (_loc_1 > 0)
            {
                while (true)
                {
                    
                    _loc_5 = this[_loc_4];
                    if (_loc_5 !== undefined)
                    {
                    }
                    if (_loc_5 !== null)
                    {
                        _loc_3 = _loc_3 + _loc_5.toLocaleString();
                    }
                    if (++_loc_4 == _loc_1)
                    {
                        break;
                    }
                    _loc_3 = _loc_3 + _loc_2;
                }
            }
            return _loc_3;
        }// end function

        function join(param1:String = ",") : String
        {
            var _loc_5:* = 0;
            var _loc_2:* = this.length;
            var _loc_3:* = "";
            var _loc_4:* = 0;
            if (_loc_2 > 0)
            {
                while (true)
                {
                    
                    _loc_5 = _loc_4;
                    _loc_3 = _loc_3 + this[_loc_5];
                    _loc_5 = _loc_4 + 1;
                    if (_loc_5 == _loc_2)
                    {
                        break;
                    }
                    _loc_3 = _loc_3 + param1;
                }
            }
            return _loc_3;
        }// end function

        private function _concat(param1:Array)
        {
            var _loc_6:* = undefined;
            var _loc_7:* = 0;
            var _loc_2:* = this.newThisType();
            _loc_2._spliceHelper(0, this.length, 0, this, 0);
            var _loc_3:* = bugzilla(504525);
            var _loc_4:* = 0;
            var _loc_5:* = param1.length;
            while (_loc_4 < _loc_5)
            {
                
                _loc_6 = castToThisType(param1[_loc_4]);
                _loc_7 = _loc_3 ? (_loc_2.length) : (this.length);
                _loc_2._spliceHelper(_loc_7, _loc_6.length, 0, _loc_6, 0);
                _loc_4 = _loc_4 + 1;
            }
            return _loc_2;
        }// end function

        function every(param1:Function, param2:Object = null) : Boolean
        {
            return _every(this, param1, param2 is Object ? (param2) : (null));
        }// end function

        function forEach(param1:Function, param2:Object = null) : void
        {
            _forEach(this, param1, param2 is Object ? (param2) : (null));
            return;
        }// end function

        function map(param1:Function, param2:Object = null)
        {
            var _loc_3:* = this._map(param1, param2 is Object ? (param2) : (null));
            return bugzilla(574600) ? (_loc_3) : (undefined);
        }// end function

        function push(... args) : uint;

        private function _reverse() : void;

        function some(param1, param2:Object = null) : Boolean
        {
            return _some(this, param1, param2 is Object ? (param2) : (null));
        }// end function

        private function _slice(param1:Number = 0, param2:Number = 2147483647)
        {
            var _loc_3:* = this.clamp(param1, this.length);
            var _loc_4:* = this.clamp(param2, this.length);
            if (_loc_4 < _loc_3)
            {
                _loc_4 = _loc_3;
            }
            var _loc_5:* = this.newThisType();
            _loc_5._spliceHelper(0, _loc_4 - _loc_3, 0, this, _loc_3);
            return _loc_5;
        }// end function

        private function _splice(param1, param2, param3:Array)
        {
            var _loc_4:* = this.clamp(param1, this.length);
            var _loc_5:* = this.clamp(param2, this.length - _loc_4);
            var _loc_6:* = this.newThisType();
            _loc_6._spliceHelper(0, _loc_5, 0, this, _loc_4);
            this._spliceHelper(_loc_4, param3.length, _loc_5, param3, 0);
            return _loc_6;
        }// end function

        private function _spliceHelper(param1:uint, param2:uint, param3:uint, param4:Object, param5:uint) : void;

        function unshift(... args) : uint;

        private function _filter(param1:Function, param2);

        private function _map(param1:Function, param2);

        private function clamp(param1:Number, param2:uint) : uint
        {
            var _loc_3:* = 0;
            if (param1 < 0)
            {
                if (param1 + param2 < 0)
                {
                    _loc_3 = 0;
                }
                else
                {
                    _loc_3 = uint(param1 + param2);
                }
            }
            else if (param1 > param2)
            {
                _loc_3 = param2;
            }
            else if (param1 != param1)
            {
                _loc_3 = 0;
            }
            else
            {
                _loc_3 = uint(param1);
            }
            return _loc_3;
        }// end function

        function concat(... args) : Vector$object
        {
            return this._concat(args);
        }// end function

        function filter(param1:Function, param2:Object = null) : Vector$object
        {
            return this._filter(param1, param2);
        }// end function

        function pop();

        function reverse() : Vector$object
        {
            this._reverse();
            return this;
        }// end function

        function shift();

        function slice(param1:Number = 0, param2:Number = 2147483647) : Vector$object
        {
            return this._slice(param1, param2);
        }// end function

        function sort(param1) : Vector$object
        {
            var _loc_2:* = [param1];
            _sort(this, _loc_2);
            return this;
        }// end function

        function splice(param1:Number, param2:Number, ... args) : Vector$object
        {
            return this._splice(param1, param2, args);
        }// end function

        function indexOf(param1:Object, param2:Number = 0) : Number
        {
            var _loc_3:* = this.clamp(param2, this.length);
            var _loc_4:* = _loc_3;
            var _loc_5:* = this.length;
            while (_loc_4 < _loc_5)
            {
                
                if (this[_loc_4] === param1)
                {
                    return _loc_4;
                }
                _loc_4 = _loc_4 + 1;
            }
            return -1;
        }// end function

        function lastIndexOf(param1:Object, param2:Number = 2147483647) : Number
        {
            var _loc_3:* = this.clamp(param2, this.length);
            if (_loc_3 == this.length)
            {
                _loc_3 = _loc_3 - 1;
            }
            var _loc_4:* = _loc_3;
            while (_loc_4 >= 0)
            {
                
                if (this[_loc_4] === param1)
                {
                    return _loc_4;
                }
                _loc_4 = _loc_4 - 1;
            }
            return -1;
        }// end function

        private static function castToThisType(param1) : Vector$object
        {
            return param1;
        }// end function

        private static function _every(param1, param2:Function, param3) : Boolean;

        private static function _forEach(param1, param2:Function, param3) : void;

        private static function _some(param1, param2:Function, param3) : Boolean;

        private static function _sort(param1, param2:Array);

        prototype.push = function (... args)
        {
            castToThisType(this);
            args = this;
            if (args.fixed)
            {
                Error.throwError(RangeError, 1126);
            }
            var _loc_3:* = args.length;
            var _loc_4:* = 0;
            var _loc_5:* = args.length;
            while (_loc_4 < _loc_5)
            {
                
                args[_loc_3] = args[_loc_4];
                _loc_4 = _loc_4 + 1;
                _loc_3 = _loc_3 + 1;
            }
            args.length = _loc_3;
            return _loc_3;
        }// end function
        ;
        prototype.toString = function ()
        {
            return castToThisType(this).toString();
        }// end function
        ;
        prototype.toLocaleString = function ()
        {
            return castToThisType(this).toLocaleString();
        }// end function
        ;
        prototype.join = function (param1 = undefined)
        {
            return castToThisType(this).join(param1 == undefined ? (",") : (String(param1)));
        }// end function
        ;
        prototype.concat = function (... args)
        {
            return castToThisType(this)._concat(args);
        }// end function
        ;
        prototype.every = function (param1, param2 = undefined) : Boolean
        {
            return _every(castToThisType(this), param1, param2 is Object ? (param2) : (null));
        }// end function
        ;
        prototype.filter = function (param1, param2 = undefined)
        {
            return castToThisType(this)._filter(param1, param2 is Object ? (param2) : (null));
        }// end function
        ;
        prototype.forEach = function (param1, param2 = undefined)
        {
            _forEach(castToThisType(this), param1, param2 is Object ? (param2) : (null));
            return;
        }// end function
        ;
        prototype.indexOf = function (param1, param2 = undefined)
        {
            return castToThisType(this).indexOf(param1, Number(param2));
        }// end function
        ;
        prototype.lastIndexOf = function (param1, param2 = undefined)
        {
            return castToThisType(this).lastIndexOf(param1, param2 == undefined ? (Infinity) : (Number(param2)));
        }// end function
        ;
        prototype.map = function (param1, param2 = undefined)
        {
            return castToThisType(this)._map(param1, param2 is Object ? (param2) : (null));
        }// end function
        ;
        prototype.pop = function ()
        {
            return castToThisType(this).pop();
        }// end function
        ;
        prototype.reverse = function ()
        {
            return castToThisType(this).reverse();
        }// end function
        ;
        prototype.shift = function ()
        {
            return castToThisType(this).shift();
        }// end function
        ;
        prototype.slice = function (param1 = undefined, param2 = undefined)
        {
            return castToThisType(this)._slice(param1 == undefined ? (0) : (Number(param1)), param2 == undefined ? (2147483647) : (Number(param2)));
        }// end function
        ;
        prototype.some = function (param1, param2 = undefined) : Boolean
        {
            return _some(castToThisType(this), param1, param2 is Object ? (param2) : (null));
        }// end function
        ;
        prototype.sort = function (param1)
        {
            var _loc_2:* = [param1];
            return _sort(castToThisType(this), _loc_2);
        }// end function
        ;
        prototype.splice = function (param1, param2, ... args)
        {
            return castToThisType(this)._splice(Number(param1), Number(param2), args);
        }// end function
        ;
        prototype.unshift = function (... args)
        {
            return castToThisType(this).unshift.apply(this, args);
        }// end function
        ;
        _dontEnumPrototype(prototype);
    }
}