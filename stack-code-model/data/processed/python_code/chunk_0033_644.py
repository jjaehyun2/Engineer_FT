package com.illuzor.solarsystem.tools {
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	
	public class Bitmaps {
		
		[Embed(source = "../../../../../assets/Background.jpg")] private static const BackgroundTextureClass:Class;
		[Embed(source = "../../../../../assets/sunTexture.jpg")] private static const SunTextureClass:Class;
		[Embed(source="../../../../../assets/earthTexture.jpg")] private static const EarthTextureClass:Class;
		
		public static function get backgroundTexture():BitmapData {
			return (new BackgroundTextureClass() as Bitmap).bitmapData;
		}

		public static function get sunTexture():BitmapData {
			return (new SunTextureClass() as Bitmap).bitmapData;
		}
		
		public static function get earthTexture():BitmapData {
			return (new EarthTextureClass() as Bitmap).bitmapData;
		}
		
	}
}