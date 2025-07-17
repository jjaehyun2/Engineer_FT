package com.maxpaynestory.arcadeshooter.core
{
	import flash.display.Bitmap;
	import flash.display.Sprite;
	import flash.events.Event;
	
	public class Background extends Sprite
	{

		private var bgImage:Bitmap;
		private var scrollspeed:Number;
		
		public function Background()
		{
			super();
			bgImage = AssetsManager.getInstance().getBackgroundImg();
			scrollspeed = 2;
			this.addEventListener(Event.ADDED_TO_STAGE,onBackroundAddedToStage);
		}
		
		protected function onBackroundAddedToStage(event:Event):void
		{
			bgImage.y = -(bgImage.height - stage.stageHeight);	
			this.addChild(bgImage);
		}
		
		public function updateFrame():void
		{
			bgImage.y += scrollspeed;
			if (bgImage.y >= 0)
			{               
				bgImage.y = -(bgImage.height - stage.stageHeight);
			}
		}
	}
}