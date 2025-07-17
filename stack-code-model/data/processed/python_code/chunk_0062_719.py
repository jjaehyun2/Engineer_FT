package com.illuzor.otherside.tools {
	
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class Assets {
		
		[Embed(source = "../../../../../assets/loadingImage.png")]
		private static const LoadingImageClass:Class;
		
		private static var loadingImageBdata:BitmapData;
		
		public static function get loadingBitmapData():BitmapData {
			if (!loadingImageBdata) loadingImageBdata = (new LoadingImageClass() as Bitmap).bitmapData;
			return loadingImageBdata;
		}
		
	}
}