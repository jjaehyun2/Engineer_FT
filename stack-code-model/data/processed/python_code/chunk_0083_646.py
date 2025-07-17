package com.mnogomir.menu {
	
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.utils.Dictionary;
	import flash.utils.getDefinitionByName;
	
	/**
	 * ...
	 * @author illuzor // illuzor.com // illuzor@gmail.com
	 */
	
	public class Assets {
		
		[Embed(source = "../../../../assets/images/background.jpg")]
		public static const Background:Class;
		
		[Embed(source = "../../../../assets/images/MainButton.png")]
		public static const MainButton:Class;
		
		private static var images:Dictionary = new Dictionary();
		
		public static function getImage(name:String):Bitmap {
			if (images[name] == undefined){
				var bitmap:Bitmap = new Assets[name]();
				images[name] = bitmap;
			}
			return images[name];
		}
		
	}
}