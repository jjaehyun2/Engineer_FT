package 
{
    import Number.*;

    final public class Number extends Object
    {
        public static const length:int = 1;
        public static const NaN:Number = NaN;
        public static const NEGATIVE_INFINITY:Number = -1.#INF;
        public static const POSITIVE_INFINITY:Number = 1.#INF;
        public static const MIN_VALUE:Number = _minValue();
        public static const MAX_VALUE:Number = 1.79769e+308;
        public static const E:Number = 2.71828;
        public static const LN10:Number = 2.30259;
        public static const LN2:Number = 0.693147;
        public static const LOG10E:Number = 0.434294;
        public static const LOG2E:Number = 1.4427;
        public static const PI:Number = 3.14159;
        public static const SQRT1_2:Number = 0.707107;
        public static const SQRT2:Number = 1.41421;
        private static const DTOSTR_FIXED:int = 1;
        private static const DTOSTR_PRECISION:int = 2;
        private static const DTOSTR_EXPONENTIAL:int = 3;

        public function Number(param1 = 0)
        {
            return;
        }// end function

        function toString(param1 = 10) : String
        {
            return _numberToString(this, param1);
        }// end function

        function valueOf() : Number
        {
            return this;
        }// end function

        function toExponential(param1 = 0) : String
        {
            return _convert(this, int(param1), DTOSTR_EXPONENTIAL);
        }// end function

        function toPrecision(param1 = 0) : String
        {
            if (param1 == undefined)
            {
                return this.toString();
            }
            return _convert(this, int(param1), DTOSTR_PRECISION);
        }// end function

        function toFixed(param1 = 0) : String
        {
            return _convert(this, int(param1), DTOSTR_FIXED);
        }// end function

        public static function abs(param1:Number) : Number;

        public static function acos(param1:Number) : Number;

        public static function asin(param1:Number) : Number;

        public static function atan(param1:Number) : Number;

        public static function ceil(param1:Number) : Number;

        public static function cos(param1:Number) : Number;

        public static function exp(param1:Number) : Number;

        public static function floor(param1:Number) : Number;

        public static function log(param1:Number) : Number;

        public static function round(param1:Number) : Number;

        public static function sin(param1:Number) : Number;

        public static function sqrt(param1:Number) : Number;

        public static function tan(param1:Number) : Number;

        public static function atan2(param1:Number, param2:Number) : Number;

        public static function pow(param1:Number, param2:Number) : Number;

        public static function max(param1:Number = -1.#INF, param2:Number = -1.#INF, ... args) : Number;

        public static function min(param1:Number = 1.#INF, param2:Number = 1.#INF, ... args) : Number;

        public static function random() : Number;

        private static function _numberToString(param1:Number, param2:int) : String;

        private static function _convert(param1:Number, param2:int, param3:int) : String;

        private static function _minValue() : Number;

        var _loc_1:* = function (param1 = 10) : String
        {
            if (prototype === this)
            {
                return "0";
            }
            if (!(this is Number))
            {
                Error.throwError(TypeError, 1004, "Number.prototype.toString");
            }
            return _numberToString(this, param1);
        }// end function
        ;
        prototype.toString = function (param1 = 10) : String
        {
            if (prototype === this)
            {
                return "0";
            }
            if (!(this is Number))
            {
                Error.throwError(TypeError, 1004, "Number.prototype.toString");
            }
            return _numberToString(this, param1);
        }// end function
        ;
        prototype.toLocaleString = _loc_1;
        prototype.valueOf = function ()
        {
            if (prototype === this)
            {
                return 0;
            }
            if (!(this is Number))
            {
                Error.throwError(TypeError, 1004, "Number.prototype.valueOf");
            }
            return this;
        }// end function
        ;
        prototype.toExponential = function (param1 = 0) : String
        {
            return _convert(Number(this), int(param1), DTOSTR_EXPONENTIAL);
        }// end function
        ;
        prototype.toPrecision = function (param1 = 0) : String
        {
            if (param1 == undefined)
            {
                return this.toString();
            }
            return _convert(Number(this), int(param1), DTOSTR_PRECISION);
        }// end function
        ;
        prototype.toFixed = function (param1 = 0) : String
        {
            return _convert(Number(this), int(param1), DTOSTR_FIXED);
        }// end function
        ;
        _dontEnumPrototype(prototype);
    }
}