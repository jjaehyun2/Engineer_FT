package com {
	import mx.formatters.NumberBaseRoundType;
	import mx.formatters.NumberFormatter;

	public class MathHelper {
		public static function setPrecision(val:Number, decimalPlaces:uint):Number {
			var multiplier:uint = Math.pow(10, decimalPlaces);
			var truncatedVal:Number = Math.round(val*multiplier);
			
			return truncatedVal/multiplier;
		} 
		
		public static function precision_to(value:Number,precision:int):Number {
			return MathHelper.setPrecision(value,precision);
		}
		
		public static function radius_of_rectangle(width:Number,height:Number):Number {
			return Math.sqrt(Math.pow(width,2) + Math.pow(height,2)) / 2;
		}
	}
}