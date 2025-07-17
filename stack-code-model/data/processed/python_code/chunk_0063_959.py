package com.lowoui_as.animation 
{
	import flash.display.MovieClip;
	import flash.events.Event;
	
	public class ParticleObj extends MovieClip
	{
		public var k:Number;
		public var wind:Number;
		public var nextwind:Number;
		public var winddev:Number;
		
		private var _width:uint;
		private var _height:uint;
		
		public function ParticleObj() 
		{			
			if (stage) { addedToStage(null); }
			else       { addEventListener(Event.ADDED_TO_STAGE, addedToStage, false, 0, true); }
		}
		protected function addedToStage(evt:Event = null) : void
		{
			_width = stage.stageWidth;
			_height = stage.stageHeight+200;
		}
		
		public function MoveFunc()
		{
			//trace("flowing..."+snowflakes.length);
			this.y -= k;
			this.x -= wind;
			this.x += k;
			
			if (nextwind > 0)
			{
				if (wind >= nextwind)
				{
					nextwind = -1.5+Math.random()*3;
				}
				wind += winddev;
				winddev = 0.01+Math.random()*0.05;
			}
			else
			{
				if (wind <= nextwind)
				{
					nextwind = -1.5+Math.random()*3;
				}
				wind -= winddev;
				winddev = 0.01+Math.random()*0.05;		
			}
			
			if (this.y < 0) {
				this.y = _height + 20;
			}
			if (this.x>_width+20) {
				this.x = -(_width)+Math.random()*(2*_width);
				this.y = _height + 20;
			} else if (this.x<-_width) {
				this.x = -(_width/2)+Math.random()*(1.5*_width);
				this.y = _height + 20;
			}
		}
	}
}