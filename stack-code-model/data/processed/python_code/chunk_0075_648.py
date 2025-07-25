﻿package  {
	/*Many functions were taken from Josh Whizzle's ColorMathUtil.as*/
	
	public class MyFunctions {

		public function MyFunctions() {
			//This is just a collection of static functions
		}

		//Calculate the angle between vectorA and vectorB
		public static function getAngle(_sentVecAX:Number, _sentVecAY:Number, _sentVecBX:Number = 1, _sentVecBY:Number = 0, _maxAngle:Number = 360):Number {
			var formu1:Number;
			var formu2:Number;
			var formu3:Number;
			var sentVecALen:Number;
			var sentVecBLen:Number;
			var calAngle:Number;
		
			if (isNaN(_sentVecBX) || isNaN(_sentVecBY)) {
				_sentVecBX = 1;
				_sentVecBY = 0;
			}
		
			if (_sentVecBX != 1 || _sentVecBY != 0) {
				calAngle = getAngle(_sentVecAX,_sentVecAY) - getAngle(_sentVecBX,_sentVecBY);
				if (calAngle > 180) calAngle = -360 + (calAngle%360);
				if (calAngle <= -180) calAngle = 360 + (calAngle%360);
				return calAngle;
			}
			
			formu1 = _sentVecBX * _sentVecAY - _sentVecAX * _sentVecBY;
			formu2 = _sentVecAX * _sentVecAY + _sentVecBX * _sentVecBY;
			sentVecALen = Math.sqrt( _sentVecAX * _sentVecAX + _sentVecAY * _sentVecAY);
			sentVecBLen = Math.sqrt( _sentVecBX * _sentVecBX + _sentVecBY * _sentVecBY);
			formu3 = formu1 / (sentVecALen * sentVecBLen);
			
			if (formu2 >= 0 && formu1 >= 0) {
				calAngle = Math.asin(formu3) * (180 / Math.PI);
			}
			else if (formu2 >= 0 && formu1 < 0) {
				calAngle = -180 - Math.asin(formu3) * (180 / Math.PI);
			}
			else if (formu2 < 0 && formu1 >= 0) {
				calAngle = 180 - Math.asin(formu3) * (180 / Math.PI);
			}
			else if (formu2 < 0 && formu1 < 0) {
				calAngle = Math.asin(formu3) * (180 / Math.PI);
			}
			else trace("error");
			
			if (calAngle > 180) calAngle = -360 + (calAngle%360);
			if (calAngle <= -180) calAngle = 360 + (calAngle%360);
			return calAngle;
		}
		
		//Generate a color according to the index and starting color
		public static function genColor(_index:int, _startColor:uint = 0x0077F9):uint {
			var shift:Number = 0;
			var nextH:Number = 37;
			return changeColorByHSV(_startColor, (nextH * _index) + (_index/(360/nextH +1))*shift, 0, 0);
		}
		
		//Change in input color by the specific amount of hue, saturation and value
		public static function changeColorByHSV(_originalColor:uint, _deltaH:Number, _deltaS:Number, _deltaV:Number):uint {
			var colorInHSV:Array = MyFunctions.hexToHsv(_originalColor);
			var H:Number, S:Number, V:Number;
			H = (colorInHSV[0] + _deltaH) % 360;
			if (H < 0) H = H + 360;
			if (colorInHSV[1] + _deltaS > 100) S = 100; else if (colorInHSV[1] + _deltaS < 0) S = 0; else S = colorInHSV[1] + _deltaS;
			if (colorInHSV[2] + _deltaV > 100) V = 100; else if (colorInHSV[2] + _deltaV < 0) V = 0; else V = colorInHSV[2] + _deltaV;
			return MyFunctions.hsvToHex( H, S, V);
		}
		
		//Below were taken from Josh Whizzle's ColorMathUtil.as
		
		public static function RGBToHex(r:uint, g:uint, b:uint):uint
		{
			var hex:uint = (r << 16 | g << 8 | b);
			return hex;
		}
		 
		public static function HexToRGB(hex:uint):Array
		{
			var rgb:Array = [];
			 
			var r:uint = hex >> 16 & 0xFF;
			var g:uint = hex >> 8 & 0xFF;
			var b:uint = hex & 0xFF;
			 
			rgb.push(r, g, b);
			return rgb;
		}
		
		public static function hexToHsv(color:uint):Array
		{
			var colors:Array = HexToRGB(color);
			return RGBtoHSV(colors[0], colors[1], colors[2]);
		}
		
		public static function hsvToHex(h:Number, s:Number, v:Number):uint
		{
			var colors:Array = HSVtoRGB(h, s, v);
			return RGBToHex(colors[0], colors[1], colors[2]);
		}


		/**
		 * Converts Red, Green, Blue to Hue, Saturation, Value
		 * @r channel between 0-255
		 * @s channel between 0-255
		 * @v channel between 0-255
		 */
		public static function RGBtoHSV(r:uint, g:uint, b:uint):Array
		{
			var max:uint = Math.max(r, g, b);
			var min:uint = Math.min(r, g, b);
			 
			var hue:Number = 0;
			var saturation:Number = 0;
			var value:Number = 0;
			 
			var hsv:Array = [];
			 
			//get Hue
			if(max == min){
				hue = 0;
				}else if(max == r){
				hue = (60 * (g-b) / (max-min) + 360) % 360;
				}else if(max == g){
				hue = (60 * (b-r) / (max-min) + 120);
				}else if(max == b){
				hue = (60 * (r-g) / (max-min) + 240);
			}
			 
			//get Value
			value = max;
			 
			//get Saturation
			if(max == 0){
				saturation = 0;
				}else{
				saturation = (max - min) / max;
			}
			 
			hsv = [Math.round(hue), Math.round(saturation * 100), Math.round(value / 255 * 100)];
			return hsv;
		}
		
		
		/**
		 * Converts Hue, Saturation, Value to Red, Green, Blue
		 * @h Angle between 0-360
		 * @s percent between 0-100
		 * @v percent between 0-100
		 */
		public static function HSVtoRGB(h:Number, s:Number, v:Number):Array
		{
			var r:Number = 0;
			var g:Number = 0;
			var b:Number = 0;
			var rgb:Array = [];
			 
			var tempS:Number = s / 100;
			var tempV:Number = v / 100;
			 
			var hi:int = Math.floor(h/60) % 6;
			var f:Number = h/60 - Math.floor(h/60);
			var p:Number = (tempV * (1 - tempS));
			var q:Number = (tempV * (1 - f * tempS));
			var t:Number = (tempV * (1 - (1 - f) * tempS));
			 
			switch(hi)
			{
				case 0: r = tempV; g = t; b = p; break;
				case 1: r = q; g = tempV; b = p; break;
				case 2: r = p; g = tempV; b = t; break;
				case 3: r = p; g = q; b = tempV; break;
				case 4: r = t; g = p; b = tempV; break;
				case 5: r = tempV; g = p; b = q; break;
			}
			 
			rgb = [Math.round(r * 255), Math.round(g * 255), Math.round(b * 255)];
			return rgb;
		}
	}
	
}