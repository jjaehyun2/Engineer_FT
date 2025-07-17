/**
 * @author Peter Hansen
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.straightouttaspace.Utils
{
	
	/**
	 * This class provides a list of all available spaceship sizes
	 * SMALL, MEDIUM, or LARGE.
	 */
	public class SizeEnum {
		
		public var Text:String;
		{CStringUtils.InitEnumConstants(SizeEnum);} // static ctor
		
		public static const SMALL:SizeEnum = new SizeEnum();
		public static const MEDIUM:SizeEnum = new SizeEnum();
		public static const LARGE:SizeEnum = new SizeEnum();
		
		public static function toArray():Array {
			return new Array(SMALL, MEDIUM, LARGE);
		}
		
		public static function count():uint {
			return toArray().length;
		}
	}
}