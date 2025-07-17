package com.illuzor.circles.constants {
	
	import com.illuzor.circles.utils.intRandom;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class Colors {
		
		public static const BLUE:uint = 0x2538CB;
		public static const GREEN:uint = 0x81B30C;
		public static const RED:uint = 0xFF5126;
		public static const YELLOW:uint = 0xFFC70D;
		
		private static var colors:Vector.<uint> = new <uint>[BLUE, GREEN, RED, YELLOW];
		
		public static function get randomColor():uint {
			return colors[intRandom(0, colors.length - 1)];
		}
		
		public static function getColors(amount:uint = 1, random:Boolean = true):Vector.<uint> {
			var tempVector:Vector.<uint> = new Vector.<uint>();
			for (var i:int = 0; i < colors.length; i++) {
				tempVector.push(colors[i]);
			}
			
			var newVector:Vector.<uint> = new Vector.<uint>();
			for (var j:int = 0; j < amount; j++) {
				if (random) {
					var randomNumber:uint = intRandom(0, tempVector.length - 1);
					newVector.push(tempVector[randomNumber]);
					tempVector.splice(randomNumber, 1);
				} else {
					newVector.push(tempVector[j]);
				}
			}
			return newVector;
		}
		
		public static function randomColorExcept(eColor:uint):uint {
			var tempVector:Vector.<uint> = new Vector.<uint>();
			for (var i:int = 0; i < colors.length; i++) {
				tempVector.push(colors[i]);
			}
			
			var newVector:Vector.<uint> = new Vector.<uint>();
			for (var j:int = 0; j < tempVector.length; j++) {
				var randomNumber:uint = intRandom(0, tempVector.length - 1);
				newVector.push(tempVector[randomNumber]);
				tempVector.splice(randomNumber, 1);
			}
			for (var k:int = 0; k < newVector.length; k++) {
				if (eColor != newVector[k])
					return newVector[k];
			}
			return 0;
		}
		
		public static function get totalColor():uint {
			return colors.length;
		}
	}
}