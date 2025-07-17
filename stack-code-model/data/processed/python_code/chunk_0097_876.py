package Layers 
{
	import Assets;
	import flash.display.BitmapData;
	import flash.geom.Point;
	import net.flashpunk.Entity;
	import net.flashpunk.FP;
	import net.flashpunk.graphics.Image;
	import net.flashpunk.masks.Pixelmask;
	
	/**
	 * ...
	 * @author Joseph O'Connor
	 */
	public class LayerHazards extends Entity 
	{
		public var hazardsImage:Image;
		public var isVertical:Boolean;
		
		public function LayerHazards(HAZARDSIMAGE:BitmapData, ISVERTICAL:Boolean = false, X:int = 0, Y:int = 0) 
		{
			hazardsImage = new Image(HAZARDSIMAGE);
			graphic = hazardsImage;
			
			x = X;
			y = Y;
			
			isVertical = ISVERTICAL;
			
			layer = 10;
			type = "Hazard";
			
			updateMask();
		}
		
		private function updateMask():void
		{
			var bmd:BitmapData = new BitmapData(hazardsImage.width, hazardsImage.height, true, 0);
			hazardsImage.render(bmd, new Point(0, 0), new Point(FP.camera.x, FP.camera.y));
			mask = new Pixelmask(bmd);
		}
		
	}

}