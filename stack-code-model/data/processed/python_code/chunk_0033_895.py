/**
 * Math utility class.
 *
 * Created by bslote on 3/14/15.
 */
package pw.fractal.vbm.util
{
    public class MathUtil
    {
        public static const PHI:Number = 1.61803;

        public static function digitalRoot(number:uint):uint
        {
            var m:uint = number % 9;
            return m == 0 ? 9 : m;
        }
    }
}