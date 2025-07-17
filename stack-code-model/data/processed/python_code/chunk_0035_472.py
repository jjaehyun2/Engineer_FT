package Layers 
{
	import Assets;
	import flash.display.BitmapData;
	import flash.geom.Point;
	import net.flashpunk.Entity;
	import net.flashpunk.FP;
	import net.flashpunk.graphics.Image;
	
	/**
	 * ...
	 * @author Joseph O'Connor
	 */
	public class LayerLocations extends Entity 
	{
		public var locationsImage:Image;
		
		public var startPoint:Point = null;
		public var  exitPoint:Point = null;
		
		public function LayerLocations(LOCATIONSIMAGE:BitmapData, X:int = 0, Y:int = 0) 
		{
			locationsImage = new Image(LOCATIONSIMAGE);
			graphic = locationsImage;
			
			x = X;
			y = Y;
			
			layer = 6;
			type = "Locations"
			
			getLocations();
		}
		
		private function getLocations():void
		{
			var bmd:BitmapData = new BitmapData(locationsImage.width, locationsImage.height, true, 0);
			locationsImage.render(bmd, new Point(0, 0), new Point(FP.camera.x, FP.camera.y));
			
			for (var yPos:int = 0; yPos < bmd.height; yPos+=32)
			{
				for (var xPos:int = 0;  xPos < bmd.width; xPos+=32)
				{
					var currentPixel:uint = bmd.getPixel32(xPos, yPos);
					
					var alpha:uint = currentPixel >> 24 & 0xFF;
					
					if ((alpha != 0) && (startPoint == null || exitPoint == null))
					{
						var   red:uint = currentPixel >> 16 & 0xFF;
						var green:uint = currentPixel >> 8 & 0xFF;
						var  blue:uint = currentPixel & 0xFF;
						
						if (startPoint == null && red == 0 && green == 0 && blue == 255 )
						{
							startPoint = new Point(xPos, yPos+1); // Adjust so that they start in the ground 1px
						}
						else if (exitPoint == null && red == 0 && green == 255 && blue == 0 )
						{
							exitPoint = new Point(xPos, yPos);
						}
					}
				}
				
				if (startPoint != null && exitPoint != null)
				{
					break;
				}
				
			}
		}
		
	}

}