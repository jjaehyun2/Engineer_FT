package ro.ciacob.math {

/**
 * Holds rational numbers in numerator/denominator form instead of floating point form.
 * Provides basic math operations.
 * TODO: document more thoroughly.
 */
public class Fraction implements IFraction {

	/**
	 * Computes the Lowest Common Multiple (LCM).
	 */
	private static function lcm (a:int, b:int):int {
		return (a / gcf (a, b)) * b;
	}

	/**
	 * Computes the Greatest Common Factor (GCF).
	 */
	private static function gcf (a:int, b:int):int {
		if (a % b == 0) {
			return Math.abs (b);
		} else {
			return gcf (b, a % b);
		}
	}

    public static function get WHOLE():Fraction {
        return new Fraction(1, 1);
    }

    public static function get ZERO():Fraction {
        return new Fraction(0, 1);
    }

    /**
     * Convenience comparison method to be used when sorting arrays and similar
     * operations.
     *
     * @param a        The fraction to compare.
     * @param b        The fraction to compare with.
     * @return         The test result, which can be: 1, if current fraction is
     *                 greater than the other; -1, if current fraction is less
     *                 than the other; and 0 if fractions are equal.
     */
    public static function compare(a:Fraction, b:Fraction):int {
        return a.greaterThan(b) ? 1 : a.lessThan(b) ? -1 : 0;
    }

    public static function fromString(value:String):Fraction {
        var segments:Array = value.split('/');
        if (segments.length == 2) {
            var numVal:String = segments[0];
            var numLong:Number = parseInt(numVal);
            if (!isNaN(numLong)) {
                var numUint:uint = uint(numLong);
                if (numUint == numLong) {
                    var denomVal:String = segments[1];
                    var denomLong:Number = parseInt(denomVal);
                    if (!isNaN(denomLong)) {
                        var denomUint:uint = uint(denomLong);
                        if (denomUint == denomLong) {
                            var fraction:Fraction = new Fraction;
                            fraction.setValue(numUint, denomUint);
                            return fraction;
                        }
                    }
                }
            }
        }
        throw(new ArgumentError('Fraction::fromString() failed to import a fraction value from `' + value + '`. The only accepted format is (regexp): `\d+\/\d+`, e.g.: `1/4`.'));
        return null;
    }

    public static function fromDecimal(decimal : Number):Fraction {
        var gcd:Function = function (a:Number, b:Number):Number {
            if (b < 0.0000001) {
                return a;
            }
            return gcd(b, Math.floor(a % b));
        };
        var len:int = Math.max(1, (decimal.toString().length - 2));
        var denominator:Number = Math.pow(10, len);
        var numerator:Number = (decimal * denominator);
        var divisor:Number = gcd(numerator, denominator);
        numerator /= divisor;
        denominator /= divisor;
        return fromString(Math.floor(numerator) + '/' + Math.floor(denominator));
    }

    /**
     * You may construct a Fraction instance as follows:
     * - new Fraction;
     * - new Fraction (other : Fraction); // copies numerator and denominator values from the other fraction
     * - new Fraction (numerator : int); // assumes 1 as the denominator
     * - new Fraction (numerator : int, denominator : int);
     * - new Fraction (whole : int, numerator : int, denominator : int);
     */
    public function Fraction(...params) {
        var tmpFract:IFraction;
        var tmpNum:int;
        var haveArgError:Boolean;
        if (params.length == 0) {
            setValue(0, 1);
        } else if (params.length == 1) {
            if (params[0] is IFraction) {
                tmpFract = (params[0] as IFraction);
                setValue(tmpFract.numerator, tmpFract.denominator);
            } else if (params[0] is int) {
                setValue(params[0], 1);
            } else {
                haveArgError = true;
            }
        } else if (params.length == 2) {
            if (params[0] is int && params[1] is int) {
                setValue(params[0], params[1])
            } else {
                haveArgError = true;
            }
        } else if (params.length == 3) {
            if (params[0] is int && params[1] is int && params[2] is int) {
                tmpNum = params[0] * params[2] + params[1];
                setValue(tmpNum, params[2]);
            } else {
                haveArgError = true;
            }
        } else {
            haveArgError = true;
        }
        if (haveArgError) {
            var err:ArgumentError = new ArgumentError('Cannot create a new Fraction with provided argument(s). Please refer to documentation.');
            throw(err);
        }
    }

    private var _denominator:int;
    private var _numerator:int;

    /**
     * Adds another fraction to this one.
     * @param other        The fraction to add.
     * @return            The addition result, as a new fraction.
     */
    public function add(other:IFraction):IFraction {
        var lcd:int = lcm(_denominator, other.denominator);
        var quot1:int = lcd / _denominator;
        var quot2:int = lcd / other.denominator;
        var fract:IFraction = new Fraction;
        fract.setValue(_numerator * quot1 + other.numerator * quot2, lcd);
        return fract;
    }

    /**
     * Convenience method to determine what percentage "is" this fraction from another one.
     * Shorthand for "getFractionOf (other).floatValue";
     *
     * @param    other
     *            Another fraction to find out what percentage the current fraction represents of.
     *
     * @return    A decimal value, such 0.5.
     */
    public function getPercentageOf(other:IFraction):Number {
        return getFractionOf(other).floatValue;
    }

    /**
     * Alias of "divide (otherFraction)".
     *
     * @param    other
     *            Another fraction to find out what fraction the current fraction represents of.
     *
     * @return    A Fraction object, such 1/2.
     */
    public function getFractionOf(other:IFraction):IFraction {
        return this.divide(other);
    }

    /**
     * @return The current denominator.
     */
    public function get denominator():int {
        return _denominator;
    }

    /**
     * Divides this fraction by another. This is a convenience method.
     * @param other        The fraction to divide by.
     * @return
     */
    public function divide(other:IFraction):IFraction {
        return multiply(other.reciprocal);
    }

    /**
     * Checks if this fraction is equal to another.
     * @param other        The fraction to test.
     * @return            The equality test result.
     */
    public function equals(other:IFraction):Boolean {
        return (_numerator == other.numerator && _denominator == other.denominator);
    }

    /**
     * @return        The (aproximated) floating point value.
     */
    public function get floatValue():Number {
        return _numerator / _denominator;
    }

    /**
     * Checks if this fraction is greater than another.
     * @param other        The fraction to test.
     * @return            The test result.
     */
    public function greaterThan(other:IFraction):Boolean {
        return (other.denominator * _numerator > _denominator * other.numerator);
    }

    /**
     * Checks if this fraction is smaller than another.
     * @param other        The fraction to test.
     * @return            The test result.
     */
    public function lessThan(other:IFraction):Boolean {
        return (other.denominator * _numerator < _denominator * other.numerator);
    }

    /**
     * Multiplies this fraction by another.
     * @param other        The fraction to multiply by.
     * @return            The multiplication result.
     */
    public function multiply(other:IFraction):IFraction {
        var fract:IFraction = new Fraction;
        fract.setValue(_numerator * other.numerator, _denominator * other.denominator);
        return fract;
    }

    /**
     * @return        The current numerator of the function
     */
    public function get numerator():int {
        return _numerator;
    }

    /**
     * @return        The numerator with the whole-number portion removed.
     */
    public function get properNumerator():int {
        return (_numerator % _denominator);
    }

    /**
     * @return        The reciprocal (inverse) of the fraction, where the numerator and denominator switch place.
     */
    public function get reciprocal():IFraction {
        return new Fraction(denominator, numerator);
    }

    /**
     * Changes the fraction's compound value. You may specify a whole-number portion alogn with proper numerator and
     * denominator. A proper numerator is a numerator that does not contain the whole-number portion. For example,
     * to set the value 1 1/4 (read one whole and one fourth) you will use: setProperValue (1, 1, 4).
     *
     * This is equivalent to calling setValue (5, 4);
     *
     * @param Whole                The new whole-number portion
     * @param ProperNumerator    The new proper numerator, that is, a numerator that does not contain the whole-number portion.
     * @param Denominator        The new denominator.
     */
    public function setProperValue(Whole:int, ProperNumerator:int, Denominator:int):void {
        var tmpNum:int = Whole * Denominator + ProperNumerator;
        setValue(tmpNum, Denominator);
    }

    /**
     * Changes the fraction's compound value.
     * @param Numerator        The new numerator.
     * @param Denominator      The new denominator.
     */
    public function setValue(Numerator:int, Denominator:int):void {
        _numerator = Numerator;
        _denominator = Denominator;
        _normalize();
    }

    /**
     * Subtracts another fraction from this one.
     *
     * @param other        The fraction to subtract.
     * @return            The subtraction result, as a new fraction.
     */
    public function subtract(other:IFraction):IFraction {
        var fract:IFraction = new Fraction;
        var lcd:int = lcm(_denominator, other.denominator);
        var quot1:int = lcd / _denominator;
        var quot2:int = lcd / other.denominator;
        fract.setValue(_numerator * quot1 - other.numerator * quot2, lcd);
        return fract;
    }

    /**
     * Similar to `subtract` but switches fractions when `other` is greater than this
     * one.
     *
     * @param other        The fraction to subtract.
     * @return            The subtraction result, as a new fraction.
     */
    public function subtractAbs(other:IFraction):IFraction {
        if (other.greaterThan(this)) {
            return other.subtract(this);
        }
        return subtract(other);
    }

    /**
     * @override
     * @see Object.toString()
     */
    public function toString():String {
        return [_numerator, _denominator].join('/');
    }

    /**
     * @return        The whole part of the fraction, i.e. 5/4 is 1 whole and 1/4.
     */
    public function get whole():int {
        return (_numerator - properNumerator) / _denominator;
    }

    /**
     * @private
     * Puts fraction into a standard form, unique for each mathematically different value.
     */
    private function _normalize():void {
        // Handle cases involving 0
        if (_denominator == 0 || _numerator == 0) {
            _numerator = 0;
            _denominator = 1;
        }
        // Put negative sign in numerator only.
        if (denominator < 0) {
            _numerator *= -1;
            _denominator *= -1;
        }
        // Factor out GCF from numerator and denominator.
        var n:int = gcf(_numerator, _denominator);
        _numerator = _numerator / n;
        _denominator = _denominator / n;
    }
}
}