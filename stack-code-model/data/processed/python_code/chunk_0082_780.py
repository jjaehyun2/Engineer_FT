package com.illuzor.otherside.tools  {
	
	import flash.display.Bitmap;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public final class AssetsMobile {
		
		[Embed(source = "../../../../../assets/graphics/loadingImage.png")]
		private static const LoadingImageClass:Class;
		
		public static function get loadingImage():Bitmap {
			return new LoadingImageClass() as Bitmap;
		}
		
	}
}