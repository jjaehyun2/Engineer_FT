package 
{
	
	import flash.display.Loader;
	import flash.display.Loader;
	import flash.display.Loader;
	import flash.display.MovieClip;
	import flash.display.MovieClip;
	import flash.display.Stage;
	import flash.events.Event;
	import flash.net.URLRequest;
	
	public class Cowboys extends MovieClip
	{
	
		public var fatEnemy:Loader = new Loader;
		public var slimEnemy:Loader = new Loader;
		private var bob:Number = Math.random() * 500;
		
		public function Cowboys() : void
		{
			this.addEventListener(Event.ADDED_TO_STAGE, init);
			
			fatEnemy.load(new URLRequest("../animations/enemy/fat/enemy_animations_(_Run_).swf"));
			slimEnemy.load(new URLRequest("../animations/enemy/slim/enemy.swf"));
			
			
			
			
		}
		
		private function init(e:Event):void 
		{
			removeEventListener(Event.ADDED_TO_STAGE, init);
			
			//fatEnemy.y = Math.random() * (stage.stageHeight + 200);
			//slimEnemy.y = Math.random() * (stage.stageHeight + 200);
			if( Math.random() < 0.5){
				addChild(fatEnemy);
			}
			else{
				addChild(slimEnemy);
			}
			
			
			this.addEventListener(Event.ENTER_FRAME, loop);
			
		}
		
		private function loop(e:Event):void 
		{
			if (this.x < 500 - bob)
			{
				this.x += 7;
			}
		}
		
		//public function adjust():void
		//{
			//if (this.x - this.width / 2 < -1000)
			//{
				//this.x = -1000 + this.width / 2;
			//}
			//
			//if (this.x + this.width / 2 > 500)
			//{
				//this.x = 500 - this.width / 2;
			//}
			//
			//if (this.y - this.height / 2 < 10)
			//{
				//this.y = 10 + this.height / 2;
			//}
			//
			//if (this.y + this.height / 2 > 1210)
			//{
				//this.y = 1210 - this.height / 2;
			//}	
		//}
		
	}
	
}