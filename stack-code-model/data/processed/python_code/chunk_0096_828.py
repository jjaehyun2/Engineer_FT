/*
 *	Temple Library for ActionScript 3.0
 *	Copyright © MediaMonks B.V.
 *	All rights reserved.
 *	
 *	Redistribution and use in source and binary forms, with or without
 *	modification, are permitted provided that the following conditions are met:
 *	1. Redistributions of source code must retain the above copyright
 *	   notice, this list of conditions and the following disclaimer.
 *	2. Redistributions in binary form must reproduce the above copyright
 *	   notice, this list of conditions and the following disclaimer in the
 *	   documentation and/or other materials provided with the distribution.
 *	3. All advertising materials mentioning features or use of this software
 *	   must display the following acknowledgement:
 *	   This product includes software developed by MediaMonks B.V.
 *	4. Neither the name of MediaMonks B.V. nor the
 *	   names of its contributors may be used to endorse or promote products
 *	   derived from this software without specific prior written permission.
 *	
 *	THIS SOFTWARE IS PROVIDED BY MEDIAMONKS B.V. ''AS IS'' AND ANY
 *	EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 *	WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 *	DISCLAIMED. IN NO EVENT SHALL MEDIAMONKS B.V. BE LIABLE FOR ANY
 *	DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 *	(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 *	LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 *	ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 *	(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 *	SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *	
 *	
 *	Note: This license does not apply to 3rd party classes inside the Temple
 *	repository with their own license!
 */

package temple.utils.color
{
	import temple.core.debug.objectToString;
	import temple.utils.types.NumberUtils;

	import flash.geom.ColorTransform;

	/**
	 * Utility class for handling colors.
	 * 
	 * @author Thijs Broerse
	 */
	public final class ColorUtils
	{
		public static function colorTransform(color:uint, alpha:Number = 1):ColorTransform
		{
			var argb:ARGB = ColorUtils.getARGB(color);

			return new ColorTransform(1 - alpha, 1 - alpha, 1 - alpha, 1, argb.red * alpha, argb.green * alpha, argb.blue * alpha, 0);
		}

		/**
		 * Interpolates (tints) between two colors.
		 * 	
		 * @param begin: The start color.
		 * @param end: The finish color.
		 * @param amount: The level of interpolation between the two colors.
		 * @return The new interpolated color.
		 * @example
		 * <listing version="3.0">
		 * var myColor:ColorTransform = new ColorTransform();
		 * myColor.color              = 0xFF0000;
		 * 			
		 * var box:Sprite = new Sprite();
		 * box.graphics.beginFill(0x0000FF);
		 * box.graphics.drawRect(10, 10, 250, 250);
		 * box.graphics.endFill();
		 * 			
		 * box.transform.colorTransform = ColorUtil.interpolateColor(new ColorTransform(), myColor, new Percent(0.5));
		 * 			
		 * addChild(box);
		 * </listing>
		 */
		public static function interpolateColor(begin:ColorTransform, end:ColorTransform, factor:Number):ColorTransform
		{
			var interpolation:ColorTransform = new ColorTransform();

			interpolation.redMultiplier = NumberUtils.interpolate(factor, begin.redMultiplier, end.redMultiplier);
			interpolation.greenMultiplier = NumberUtils.interpolate(factor, begin.greenMultiplier, end.greenMultiplier);
			interpolation.blueMultiplier = NumberUtils.interpolate(factor, begin.blueMultiplier, end.blueMultiplier);
			interpolation.alphaMultiplier = NumberUtils.interpolate(factor, begin.alphaMultiplier, end.alphaMultiplier);
			interpolation.redOffset = NumberUtils.interpolate(factor, begin.redOffset, end.redOffset);
			interpolation.greenOffset = NumberUtils.interpolate(factor, begin.greenOffset, end.greenOffset);
			interpolation.blueOffset = NumberUtils.interpolate(factor, begin.blueOffset, end.blueOffset);
			interpolation.alphaOffset = NumberUtils.interpolate(factor, begin.alphaOffset, end.alphaOffset);

			return interpolation;
		}

		public static function interpolateColorHex(fromColor:uint, toColor:uint, progress:Number):uint
		{
			progress = Math.min(Math.max(0, progress), 1);
			var q:Number = 1 - progress;
			var resultA:uint = ((fromColor >> 24) & 0xFF) * q + ((toColor >> 24) & 0xFF) * progress;
			var resultR:uint = ((fromColor >> 16) & 0xFF) * q + ((toColor >> 16) & 0xFF) * progress;
			var resultG:uint = ((fromColor >> 8) & 0xFF) * q + ((toColor >> 8) & 0xFF) * progress;
			var resultB:uint = (fromColor & 0xFF) * q + (toColor & 0xFF) * progress;
			return resultA << 24 | resultR << 16 | resultG << 8 | resultB;
		}

		/**
		 * Converts a color into a ColorTransform, using the color as offset values.
		 * When applying this ColorTransform to the 'transform.colortransform' property of a clip, black will become the color and all grey shades, shades of that color
		 * 
		 * @param color A uint representing the color value
		 * 
		 * @example
		 * mcGreyscaleClip --> a designer clip using black and greyscale values;
		 * <listing version="3.0">mcGreyscaleClip.transform.colorTransform = ColorUtils.colorize(0xFF0000);</listing>
		 */
		public static function colorize(color:uint):ColorTransform
		{
			var colTransf:ColorTransform = new ColorTransform();
			var rgbColor:Object = ColorUtils.getRGB(color);

			colTransf.redOffset = rgbColor.r;
			colTransf.greenOffset = rgbColor.g;
			colTransf.blueOffset = rgbColor.b;

			return colTransf;
		}

		/**
		 * Converts a series of individual RGB(A) values to a 32-bit ARGB color value.
		 * 	
		 * @param r: A uint from 0 to 255 representing the red color value.
		 * @param g: A uint from 0 to 255 representing the green color value.
		 * @param b: A uint from 0 to 255 representing the blue color value.
		 * @param a: A uint from 0 to 255 representing the alpha value. Default is {@code 255}.
		 * @return Returns a hexidecimal color as a String.
		 * @example
		 * <listing version="3.0">
		 * var hexColor : String = ColorUtil.getHexStringFromARGB(128, 255, 0, 255);
		 * trace(hexColor); // Traces 80FF00FF
		 * </listing>
		 */
		public static function getColor(r:uint, g:uint, b:uint, a:uint = 255):uint
		{
			return (a << 24) | (r << 16) | (g << 8) | b;
		}

		/**
		 * Converts a 32-bit ARGB color value into an ARGB object.
		 * 	
		 * @param color: The 32-bit ARGB color value.
		 * @return Returns an object with the properties a, r, g, and b defined.
		 * @example
		 * <listing version="3.0">
		 * var myRGB:Object = ColorUtil.getARGB(0xCCFF00FF);
		 * trace("Alpha = " + myRGB.a);
		 * trace("Red = " + myRGB.r);
		 * trace("Green = " + myRGB.g);
		 * trace("Blue = " + myRGB.b);
		 * </listing>
		 */
		public static function getARGB(color:uint):ARGB
		{
			var c:ARGB = new ARGB();
			c.alpha = color >> 24 & 0xFF;
			c.red = color >> 16 & 0xFF;
			c.green = color >> 8 & 0xFF;
			c.blue = color & 0xFF;
			return c;
		}

		/**
		 * Converts a 24-bit RGB color value into an RGB object.
		 * 	
		 * @param color: The 24-bit RGB color value.
		 * @return Returns an object with the properties r, g, and b defined.
		 * @example
		 * <listing version="3.0">
		 * var myRGB:Object = ColorUtil.getRGB(0xFF00FF);
		 * trace("Red = " + myRGB.r);
		 * trace("Green = " + myRGB.g);
		 * trace("Blue = " + myRGB.b);
		 * </listing>
		 */
		public static function getRGB(color:uint):Object
		{
			var c:Object = {};
			c.r = color >> 16 & 0xFF;
			c.g = color >> 8 & 0xFF;
			c.b = color & 0xFF;
			return c;
		}

		/**
		 * Converts a 32-bit ARGB color value into a hexidecimal String representation.
		 * 	
		 * @param a: A uint from 0 to 255 representing the alpha value.
		 * @param r: A uint from 0 to 255 representing the red color value.
		 * @param g: A uint from 0 to 255 representing the green color value.
		 * @param b: A uint from 0 to 255 representing the blue color value.
		 * @return Returns a hexidecimal color as a String.
		 * @example
		 * <listing version="3.0">
		 * var hexColor : String = ColorUtil.getHexStringFromARGB(128, 255, 0, 255);
		 * trace(hexColor); // Traces 80FF00FF
		 * </listing>
		 */
		public static function getHexStringFromARGB(a:uint, r:uint, g:uint, b:uint):String
		{
			var aa:String = a.toString(16);
			var rr:String = r.toString(16);
			var gg:String = g.toString(16);
			var bb:String = b.toString(16);
			aa = (aa.length == 1) ? '0' + aa : aa;
			rr = (rr.length == 1) ? '0' + rr : rr;
			gg = (gg.length == 1) ? '0' + gg : gg;
			bb = (bb.length == 1) ? '0' + bb : bb;
			return (aa + rr + gg + bb).toUpperCase();
		}

		/**
		 * Converts an RGB color value into a hexidecimal String representation.
		 * 	
		 * @param r: A uint from 0 to 255 representing the red color value.
		 * @param g: A uint from 0 to 255 representing the green color value.
		 * @param b: A uint from 0 to 255 representing the blue color value.
		 * @return Returns a hexidecimal color as a String.
		 * @example
		 * <listing version="3.0">
		 * var hexColor : String = ColorUtil.getHexStringFromRGB(255, 0, 255);
		 * trace(hexColor); // Traces FF00FF
		 * </listing>
		 */
		public static function getHexStringFromRGB(r:uint, g:uint, b:uint):String
		{
			var rr:String = r.toString(16);
			var gg:String = g.toString(16);
			var bb:String = b.toString(16);
			rr = (rr.length == 1) ? '0' + rr : rr;
			gg = (gg.length == 1) ? '0' + gg : gg;
			bb = (bb.length == 1) ? '0' + bb : bb;
			return (rr + gg + bb).toUpperCase();
		}

		/**
		 * Convert HSB to RGB
		 */
		public static function HSBToRGB(h:int, s:int, b:int):ARGB
		{
			var rgb:Object = {};

			var max:Number = (b * 0.01) * 255;
			var min:Number = max * (1 - (s * 0.01));

			if (h == 360)
			{
				h = 0;
			}

			if (s == 0)
			{
				rgb.r = rgb.g = rgb.b = b * (255 * 0.01) ;
			}
			else
			{
				var _h:Number = Math.floor(h / 60);

				switch (_h)
				{
					case 0:
						rgb.r = max	;
						rgb.g = min + h * (max - min) / 60;
						rgb.b = min;
						break;
					case 1:
						rgb.r = max - (h - 60) * (max - min) / 60;
						rgb.g = max;
						rgb.b = min;
						break;
					case 2:
						rgb.r = min ;
						rgb.g = max;
						rgb.b = min + (h - 120) * (max - min) / 60;
						break;
					case 3:
						rgb.r = min;
						rgb.g = max - (h - 180) * (max - min) / 60;
						rgb.b = max;
						break;
					case 4:
						rgb.r = min + (h - 240) * (max - min) / 60;
						rgb.g = min;
						rgb.b = max;
						break;
					case 5:
						rgb.r = max;
						rgb.g = min;
						rgb.b = max - (h - 300) * (max - min) / 60;
						break;
					case 6:
						rgb.r = max;
						rgb.g = min + h * (max - min) / 60;
						rgb.b = min;
						break;
				}

				rgb.r = Math.min(255, Math.max(0, Math.round(rgb.r)));
				rgb.g = Math.min(255, Math.max(0, Math.round(rgb.g)));
				rgb.b = Math.min(255, Math.max(0, Math.round(rgb.b)));
			}
			return new ARGB(rgb.r, rgb.g, rgb.b);
		}
		
		/**
		 * Convert RGB to HSB
		 */
		public static function RGBtoHSB(r:int, g:int, b:int):Object
		{
			var hsb:Object = {};
			var _max:Number = Math.max(r,g,b);
			var _min:Number = Math.min(r,g,b);
			 
			hsb.s = (_max != 0) ? (_max - _min) / _max * 100: 0;
			hsb.b = _max / 255 * 100;
			 
			if(hsb.s == 0)
			{
				hsb.h = 0;
			}
			else
			{
				switch(_max)
				{
					case r:
					{
						hsb.h = (g - b)/(_max - _min)*60 + 0;
						break;
					}
					case g:
					{
						hsb.h = (b - r)/(_max - _min)*60 + 120;
						break;
					}
					case b:
					{
						hsb.h = (r - g)/(_max - _min)*60 + 240;
						break;
					}
				}
			}
			 
			hsb.h = Math.min(360, Math.max(0, Math.round(hsb.h)));
			hsb.s = Math.min(100, Math.max(0, Math.round(hsb.s)));
			hsb.b = Math.min(100, Math.max(0, Math.round(hsb.b)));
			 
			return hsb;
		}

		/**
		 * Generates a random color with a specific saturation and brightness
		 */
		public static function getRandomColor(saturation:int = 255, brightness:int = 255):uint
		{
			return ColorUtils.HSBToRGB(Math.random() * 255, saturation, brightness).color;
		}
		
		/**
		 * @private
		 */
		public static function toString():String
		{
			return objectToString(ColorUtils);
		}
	}
}