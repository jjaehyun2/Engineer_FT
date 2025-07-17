package flash.geom
{

    public class Vector3D extends Object
    {
        public var x:Number;
        public var y:Number;
        public var z:Number;
        public var w:Number;
        public static const X_AXIS:Vector3D = new Vector3D(1, 0, 0);
        public static const Y_AXIS:Vector3D = new Vector3D(0, 1, 0);
        public static const Z_AXIS:Vector3D = new Vector3D(0, 0, 1);

        public function Vector3D(param1:Number = 0, param2:Number = 0, param3:Number = 0, param4:Number = 0)
        {
            this.x = param1;
            this.y = param2;
            this.z = param3;
            this.w = param4;
            return;
        }// end function

        public function clone() : Vector3D
        {
            return new Vector3D(this.x, this.y, this.z, this.w);
        }// end function

        public function dotProduct(param1:Vector3D) : Number
        {
            return this.x * param1.x + this.y * param1.y + this.z * param1.z;
        }// end function

        public function crossProduct(param1:Vector3D) : Vector3D
        {
            return new Vector3D(this.y * param1.z - this.z * param1.y, this.z * param1.x - this.x * param1.z, this.x * param1.y - this.y * param1.x, 1);
        }// end function

        public function get length() : Number
        {
            var _loc_1:* = this.x * this.x + this.y * this.y + this.z * this.z;
            if (_loc_1 <= 0)
            {
                return 0;
            }
            return Math.sqrt(_loc_1);
        }// end function

        public function get lengthSquared() : Number
        {
            return this.x * this.x + this.y * this.y + this.z * this.z;
        }// end function

        public function normalize() : Number
        {
            var _loc_1:* = this.length;
            var _loc_2:* = _loc_1 != 0 ? (1 / _loc_1) : (0);
            this.x = this.x * _loc_2;
            this.y = this.y * _loc_2;
            this.z = this.z * _loc_2;
            return _loc_1;
        }// end function

        public function scaleBy(param1:Number) : void
        {
            this.x = this.x * param1;
            this.y = this.y * param1;
            this.z = this.z * param1;
            return;
        }// end function

        public function incrementBy(param1:Vector3D) : void
        {
            this.x = this.x + param1.x;
            this.y = this.y + param1.y;
            this.z = this.z + param1.z;
            return;
        }// end function

        public function decrementBy(param1:Vector3D) : void
        {
            this.x = this.x - param1.x;
            this.y = this.y - param1.y;
            this.z = this.z - param1.z;
            return;
        }// end function

        public function add(param1:Vector3D) : Vector3D
        {
            return new Vector3D(this.x + param1.x, this.y + param1.y, this.z + param1.z);
        }// end function

        public function subtract(param1:Vector3D) : Vector3D
        {
            return new Vector3D(this.x - param1.x, this.y - param1.y, this.z - param1.z);
        }// end function

        public function negate() : void
        {
            this.x = -this.x;
            this.y = -this.y;
            this.z = -this.z;
            return;
        }// end function

        public function equals(param1:Vector3D, param2:Boolean = false) : Boolean
        {
            if (this.x == param1.x)
            {
            }
            if (this.y == param1.y)
            {
            }
            if (this.z == param1.z)
            {
            }
            return param2 ? (this.w == param1.w) : (true);
        }// end function

        public function nearEquals(param1:Vector3D, param2:Number, param3:Boolean = false) : Boolean
        {
            var _loc_4:* = this.x - param1.x;
            _loc_4 = _loc_4 < 0 ? (-_loc_4) : (_loc_4);
            var _loc_5:* = _loc_4 < param2;
            if (_loc_5)
            {
                _loc_4 = this.y - param1.y;
                _loc_4 = _loc_4 < 0 ? (-_loc_4) : (_loc_4);
                _loc_5 = _loc_4 < param2;
                if (_loc_5)
                {
                    _loc_4 = this.z - param1.z;
                    _loc_4 = _loc_4 < 0 ? (-_loc_4) : (_loc_4);
                    _loc_5 = _loc_4 < param2;
                    if (_loc_5)
                    {
                    }
                    if (param3)
                    {
                        var _loc_6:* = param1.w;
                        this.w = param1.w;
                        _loc_4 = _loc_6;
                        _loc_4 = _loc_4 < 0 ? (-_loc_4) : (_loc_4);
                        _loc_5 = _loc_4 < param2;
                    }
                }
            }
            return _loc_5;
        }// end function

        public function project() : void
        {
            var _loc_1:* = 1 / this.w;
            this.x = this.x * _loc_1;
            this.y = this.y * _loc_1;
            this.z = this.z * _loc_1;
            return;
        }// end function

        public function toString() : String
        {
            var _loc_1:* = "Vector3D(" + this.x + ", " + this.y + ", " + this.z;
            _loc_1 = _loc_1 + ")";
            return _loc_1;
        }// end function

        public function copyFrom(param1:Vector3D) : void
        {
            this.x = param1.x;
            this.y = param1.y;
            this.z = param1.z;
            return;
        }// end function

        public function setTo(param1:Number, param2:Number, param3:Number) : void
        {
            this.x = param1;
            this.y = param2;
            this.z = param3;
            return;
        }// end function

        public static function angleBetween(param1:Vector3D, param2:Vector3D) : Number
        {
            var _loc_3:* = param1.x * param2.x + param1.y * param2.y + param1.z * param2.z;
            var _loc_4:* = param1.length;
            var _loc_5:* = param2.length;
            _loc_3 = _loc_3 / (_loc_4 * _loc_5);
            if (watson(3109405))
            {
                if (_loc_3 < -1)
                {
                    _loc_3 = -1;
                }
                if (_loc_3 > 1)
                {
                    _loc_3 = 1;
                }
            }
            return Math.acos(_loc_3);
        }// end function

        public static function distance(param1:Vector3D, param2:Vector3D) : Number
        {
            return param1.subtract(param2).length;
        }// end function

    }
}