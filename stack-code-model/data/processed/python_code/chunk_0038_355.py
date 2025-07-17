/**
 * @author Peter Hansen
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.zzznake.Util
{
	public class Helper {
		
		
		/**
		 * Converts an angle in radians to degrees
		 * 
		 * @param x Angle in radians 
		 * @return Angle in degrees
		 */
		public static function rad2Deg(x:Number):Number {
			return (x > 0 ? x : (2 * Math.PI + x)) * 360 / (2 * Math.PI);
		}
	}
}