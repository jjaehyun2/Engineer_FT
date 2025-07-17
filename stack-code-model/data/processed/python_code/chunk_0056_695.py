package  
{
	/**
	 * ...
	 * @author Jake
	 */
	import flash.display.Sprite;
	import flash.events.IOErrorEvent;

	
	public class ImageSelector extends Sprite 
	{
		private var image:ImageLoader;
		
		public function ImageSelector(x:int,y:int) 
		{
			this.x = x + 5.5;
			this.y = y + 35;
		}
		
		public function findImage(model:String):void 
		{
			image = new ImageLoader("PrinterAssets/" + model +".png");
			image.addEventListener(IOErrorEvent.IO_ERROR, setDefault);
			addChild(image);
		}
		
		private function setDefault(e:IOErrorEvent):void 
		{
			image = new ImageLoader("PrinterAssets/Default.png");
			addChild(image);
		}
	}

}