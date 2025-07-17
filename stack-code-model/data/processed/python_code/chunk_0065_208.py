package 
{
	import flash.display.Sprite;
	import flash.events.Event;
	
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class Main extends Sprite 
	{
		public var playState:PlayState = new PlayState();
		public function Main():void 
		{
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void 
		{
			removeEventListener(Event.ADDED_TO_STAGE, init);
			// entry point
			
			stage.scaleMode = "noScale";
			stage.align = "c";
			stage.showDefaultContextMenu = false;
			
			
			//var screen:SplashScreen = new SplashScreen(this);
			//stage.addChild(screen);
			proceed();
		}
		
		public function proceed():void
		{
			
			
			
			addChild(playState);
			
			//TODO add sound effects for menus
		}
	}
	
}