package
{
	import flash.geom.Rectangle;
	
	import feathers.controls.ImageLoader;
	
	import starling.display.Sprite;
	
	public class MapScene extends Sprite
	{
		public function MapScene()
		{
			super();
			this.clipRect = new Rectangle(0, 0, 480, 800);
		}
		
		public function drawBg(src:String):void
		{
			var bg:ImageLoader = new ImageLoader();
			bg.source = src;
			addChild(bg);
			bg.scaleX = bg.scaleY = 0.5;
		}
	}
}