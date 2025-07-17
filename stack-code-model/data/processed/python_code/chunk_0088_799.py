package com.lowoui_as.animation 
{
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.utils.getDefinitionByName;
	
	public class Particles extends MovieClip
	{
		/**
		 * ---------------------
		 *         sytle
		 * ---------------------
		 * snow flow
		 * fire burning
		 * smoke
		 */
		private var snowflakes:Array;
		
		private var _width:uint;
		private var _height:uint;
		
		public function Particles() 
		{
			snowflakes = [];
			
			if (stage) { addedToStage(null); }
			else       { addEventListener(Event.ADDED_TO_STAGE, addedToStage, false, 0, true); }
			
			StartSnow();
		}
		protected function addedToStage(evt:Event = null) : void
		{
			_width = stage.stageWidth;
			_height = stage.stageHeight+200;
		}
		
		
		function UpdateSnow(e:Event) : void
		{
			var len:Number = snowflakes.length;
			for (var i=0; i < len; i++)
			{
				snowflakes[i].MoveFunc();
			}
		}

		function InitSnow() 
		{
			// pixels 
			var max_snowsize = 10;
			// pixels 
			var num_snowflakes = 150;
			// quantity 
			
			var id:int;
			
			for (var i=0; i<num_snowflakes; i++) {
				var selector:Number = Math.random() * 20;
				if (selector > 18) {
					id = 1;
				} else if (selector > 15) {
					id = 2;
				} else {
					id = 3;
				}
				//id = Math.ceil(Math.random() * 3.9 + 0.1);
				var cc:Class = getDefinitionByName("snow_M" + id) as Class;
				var t:MovieClip = new cc();
				this.addChild(t);
				
				t.gotoAndPlay( Math.ceil(Math.random() * t.totalframes) );
				t.alpha = (40+Math.random()*60)/100;
				t.x = -(_width)+Math.random()*(2*_width);
				t.y = (_height/2)+Math.random()*(1.5*_height);
				//t.scaleX = t.scaleY=(50+Math.random()*(max_snowsize*10))/100;
				t.k = 0.5+Math.random()*1; // wind speed
				t.wind = -1.5+Math.random()*3;
				t.nextwind = -1.5+Math.random()*3;
				t.winddev = 0.1+Math.random()*0.9;
				t.z = -10;
				snowflakes.push(t);
			}
		}

		function StartSnow()
		{
			InitSnow();
			this.addEventListener(Event.ENTER_FRAME, UpdateSnow);
		}

		function StopSnow()
		{
			while (snowflakes.length > 0)
			{
				var mc = snowflakes.pop();
				this.removeChild(mc);
			}
			
			this.removeEventListener(Event.ENTER_FRAME, UpdateSnow);
		}
	}
}