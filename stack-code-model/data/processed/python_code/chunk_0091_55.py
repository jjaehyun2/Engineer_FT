package com.illuzor.gaftest {
	
	import flash.display.Bitmap;
	import flash.utils.ByteArray;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class Assets {
		
		[Embed(source = "../../../../assets/bee_mc.png")]
		private static const BeeMcClass:Class;
		
		public static function get beeMcBitmap():Bitmap {
			return new BeeMcClass() as Bitmap;
		}
		
		[Embed(source = "../../../../assets/bee_mc.xml", mimeType = "application/octet-stream")]
		private static const XmlClass:Class;
		
		public static function get xml():XML {
			return XML(new XmlClass);
		}
		
		[Embed(source = "../../../../assets/bee_fly.png")]
		private static const GafImgClass:Class;
		
		public static function get gafBitmap():Bitmap {
			return new GafImgClass() as Bitmap;
		}
		
		[Embed(source = "../../../../assets/bee_fly.gaf", mimeType = "application/octet-stream")]
		private static const GafConfigClass:Class;
		
		public static function get gafConfig():ByteArray {
			return new GafConfigClass();
		}
		
	}
}