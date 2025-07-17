package 
{
	import flash.display.BitmapData;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	import net.flashpunk.FP;
	
	/**
	 * ...
	 * @author Philip Ludington
	 */
	public class Global 
	{
		
		public function Global() 
		{
			trace("ERROR! You should NOT instantiate Global!!!");
		}		
		
		public static function MakeTransparent(source:*, color:uint = 0x00FF00FF) : BitmapData
		{
			// Get the bitmap data so we can fix it
			var bitmapData:BitmapData
			if (source is Class)
			bitmapData = FP.getBitmap(source);
			else if (source is BitmapData)
			bitmapData = source;

			// We aren’t use the transparent feature, hence the color
			var bitmapDataNew:BitmapData = new BitmapData(bitmapData.width,
			bitmapData.height, true, 0x00000000);
			var pt:Point = new Point(0, 0);
			var rect:Rectangle = new Rectangle(0, 0, bitmapData.width,
			bitmapData.height);
			var transparent:uint = 0x00000000;
			var maskColor:uint = 0x00FFFFFF;
			bitmapDataNew.threshold(bitmapData, rect, pt, "==", color, transparent, maskColor, true);

			return bitmapDataNew;
		}		
		
		public static function isDebugBuild() : Boolean
		{
			return new Error().getStackTrace().search(/:[0-9]+]$/m) > -1;
		}
	}

}