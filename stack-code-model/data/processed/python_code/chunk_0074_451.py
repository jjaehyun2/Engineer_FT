package 
{
	import flash.display.Bitmap;
	import flash.display.Sprite;
	import flash.events.Event;
	
	/**
	 * ...
	 * @author 
	 */
	public class Border extends Sprite
	{
		
		//[Embed(source="lib/achtergrond.png")]
		[Embed(source="lib/UI_border.png")]
		
		private var borderImage:Class;
		private var _border:Bitmap;
		
		
		public function Border() 
		{
			this.addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event):void
		{
			_border = new borderImage();
			
			_border.x = -400;
			
			addChild(_border);
			
			var scale:Number =  stage.stageWidth / _border.width;

			// if the height of the image will be taller than the stage,
			// set the scale to fit the height of the image to the height of the stage
			if(_border.height * scale <= stage.stageHeight){
				scale = stage.stageHeight / _border.height;
			}

			// apply the scale to the image
			_border.scaleX = 1.39;
			_border.scaleY = scale;
		}
		
		
	}

}