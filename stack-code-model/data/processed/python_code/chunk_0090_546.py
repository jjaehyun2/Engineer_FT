package enemies
{
	import flash.display.Bitmap;
	import flash.display.Sprite;
	import flash.events.Event;
	
	/**
	 * ...
	 * @author Mike
	 */
	public class Groen extends Cowboys
	{
		
		[Embed(source = "../../lib/enemies/groen.png")]
		
		private var backgroundImage:Class;
		private var bgImage:Bitmap;
		
		public function Groen() 
		{
			this.addEventListener(Event.ADDED_TO_STAGE, init);
			
			this.update();
		}  
		
		public function init(e:Event):void
		{
			this.removeEventListener(Event.ADDED_TO_STAGE, init);
		
			bgImage = new backgroundImage();
			addChild(bgImage);
			
			var scale:Number =  stage.stageWidth / bgImage.width;

			// if the height of the image will be taller than the stage,
			// set the scale to fit the height of the image to the height of the stage
			if(bgImage.height * scale <= stage.stageHeight){
				scale = stage.stageHeight / bgImage.height;
			}   

			// apply the scale to the image
			bgImage.scaleX = bgImage.scaleY = scale;
			
			this.addEventListener(Event.ENTER_FRAME, update);
		}
		
		override public function update():void
		{
			trace("Enemy groen");
		}
	}
}