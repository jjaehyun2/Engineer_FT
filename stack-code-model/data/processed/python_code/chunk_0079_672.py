package com.illuzor.bubbles {
	
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.geom.Rectangle;
	import starling.core.Starling;
	
	/**
	 * Основной класс
	 */
	
	public class Main extends Sprite {
		
		public function Main() {
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void {
			removeEventListener(Event.ADDED_TO_STAGE, init);
			
			// инициализация старлинга
			var startling:Starling = new Starling(Game, stage, new Rectangle(0, 0, stage.stageWidth, stage.stageWidth));
			startling.antiAliasing = 16;
			startling.showStats = true;
			startling.start();
		}
		
	}
}