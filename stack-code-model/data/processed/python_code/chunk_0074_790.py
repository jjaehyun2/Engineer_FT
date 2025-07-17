package com.illuzor.otherside {
	
	import com.illuzor.otherside.controllers.AppController;
	import starling.display.Sprite;
	import starling.events.Event;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class Game extends Sprite {
		
		public function Game() {
			addEventListener(Event.ADDED_TO_STAGE, addedToStage);
		}
		
		private function addedToStage(e:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, addedToStage);
			AppController.init(this);
		}
		
	}
}