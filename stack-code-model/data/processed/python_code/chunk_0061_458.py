package {
	
	import flash.display.Sprite;
	import flash.events.Event;
	import starling.core.Starling;
	import net.hires.debug.Stats;
	import flash.events.MouseEvent;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	public class Main extends Sprite {
		
		public function Main():void {
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void {
			removeEventListener(Event.ADDED_TO_STAGE, init);
			// entry point
			
			var starling:Starling = new Starling(Game, stage);
			starling.antiAliasing = 8;
			starling.start();
			starling.showStats = true;
			
			//addChild(new Stats());
		}
		
	}
}