package org.yellcorp.lib.number
{
import org.yellcorp.lib.core.StringBuilder;

import flash.utils.ByteArray;
import flash.utils.Endian;


public class NumberInfo
{
    public static const BIAS:int = 1023;
    public static const MIN_EXPONENT:int = -BIAS;
    public static const MAX_EXPONENT:int = BIAS + 1;

    private var _value:Number;
    private var _negative:Boolean;
    private var _exponent:int;

    private var _zero:Boolean;
    private var _subnormal:Boolean;
    private var _infinity:Boolean;
    private var _nan:Boolean;

    private var mantissa:Array;
    private var zeroMantissa:Boolean;

    public function NumberInfo(number:Number)
    {
        this.value = number;
    }

    // IEEE 754 Double
    //
    // SEEEEEEE EEEEMMMM MMMMMMMM MMMMMMMM MMMMMMMM MMMMMMMM MMMMMMMM MMMMMMMM
    // 00000000 11111111 22222222 33333333 44444444 55555555 66666666 77777777

    private function split():void
    {
        var bytes:ByteArray;

        var byte0:uint;
        var byte1:uint;

        bytes = new ByteArray();
        bytes.endian = Endian.BIG_ENDIAN;
        bytes.writeDouble(_value);
        bytes.position = 0;

        byte0 = bytes.readUnsignedByte();
        byte1 = bytes.readUnsignedByte();

        _negative = (byte0 & 0x80) > 0;

        _exponent = ((byte0 & 0x7F) << 4) | (byte1 >> 4);
        _exponent -= BIAS;

        mantissa = readMantissa(bytes, byte1);

        zeroMantissa = allZeros(mantissa);

        _zero = _exponent == MIN_EXPONENT && zeroMantissa;
        _subnormal = _exponent == MIN_EXPONENT && !zeroMantissa;
        _infinity = _exponent == MAX_EXPONENT && zeroMantissa;
        _nan = _exponent == MAX_EXPONENT && !zeroMantissa;
    }

    public function get value():Number
    {
        return _value;
    }

    public function set value(new_value:Number):void
    {
        _value = new_value;
        split();
    }

    public function get negative():Boolean
    {
        return _negative;
    }

    public function get exponent():int
    {
        return _exponent;
    }

    public function get zero():Boolean
    {
        return _zero;
    }

    public function get subnormal():Boolean
    {
        return _subnormal;
    }

    public function get infinity():Boolean
    {
        return _infinity;
    }

    public function get nan():Boolean
    {
        return _nan;
    }

    public function get mantissaLength():uint
    {
        return mantissa.length;
    }

    public function getMantissaHalfByte(index:uint):uint
    {
        return mantissa[index];
    }

    public function toString():String
    {
        return _value.toString();
    }

    public function getIntegerString():String
    {
        if (_zero || _subnormal)
        {
            return "0";
        }
        else
        {
            return "1";
        }
    }

    public function getFractionalString():String
    {
        var hexString:StringBuilder;
        var zeroBuffer:StringBuilder;

        if (_zero || zeroMantissa)
        {
            return "0";
        }
        else
        {
            hexString = new StringBuilder();
            zeroBuffer = new StringBuilder();

            for each (var n:uint in mantissa)
            {
                if (n == 0)
                {
                    zeroBuffer.append("0");
                }
                else
                {
                    if (zeroBuffer.length > 0)
                    {
                        hexString.append(zeroBuffer.toString());
                        zeroBuffer.clear();
                    }
                    hexString.append(n.toString(16));
                }
            }
            return hexString.toString();
        }
    }

    public function getExponentSign():String
    {
        if (_zero || _exponent >= 0)
        {
            return "";
        }
        else
        {
            return "-";
        }
    }

    public function getExponentString():String
    {
        if (_zero)
        {
            return "0";
        }
        else if (_subnormal)
        {
            return "1022";
        }
        else
        {
            return Math.abs(_exponent).toString(10);
        }
    }

    public function toRoundTripString():String
    {
        var string:StringBuilder;

        if (_nan)
        {
            return "NaN";
        }
        else if (_infinity)
        {
            return _negative ? "-Infinity" : "Infinity";
        }
        else
        {
            string = new StringBuilder();

            if (_negative)
            {
                string.append("-");
            }
            string.append("0x");
            string.append(getIntegerString());
            string.append(".");
            string.append(getFractionalString());
            string.append("p");
            string.append(getExponentSign());
            string.append(getExponentString());
        }
        return string.toString();
    }

    private static function readMantissa(bytes:ByteArray, firstByte:uint):Array
    {
        var mantissa:Array = [ (firstByte & 0x0F) ];
        var nextByte:uint;

        while (bytes.bytesAvailable)
        {
            nextByte = bytes.readUnsignedByte();
            mantissa.push(nextByte >> 4);
            mantissa.push(nextByte & 0x0F);
        }
        return mantissa;
    }

    private static function allZeros(array:Array):Boolean
    {
        for each (var u:uint in array)
        {
            if (u !== 0)
            {
                return false;
            }
        }
        return true;
    }
}
}