package 
{
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	/**
	 * ...
	 * @author Mo Kakwan
	 */
	public class ImageAssets 
	{
		
		public function ImageAssets() 
		{
		}
		
		[Embed(source = "../assets/ship.png")]
		private static var ship:Class;

		[Embed(source = "../assets/space.jpg")]
		private static var space:Class;

		public static var shipTexture:BitmapData;
		public static var spaceTexture:BitmapData;

		public static function init():void
		{
			shipTexture = (new ship() as Bitmap).bitmapData;
			spaceTexture = (new space() as Bitmap).bitmapData;
		}
		
	}

}