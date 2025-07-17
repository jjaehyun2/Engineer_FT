package com.illuzor.directtest{
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.geom.Rectangle;
	import starling.core.Starling;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	public class Main extends Sprite {
		
		public function Main():void {
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void {
			removeEventListener(Event.ADDED_TO_STAGE, init);
			// entry point
			
			var starling:Starling = new Starling(StarlingClass, stage, new Rectangle(0, 0, stage.stageWidth, stage.stageHeight));
			starling.antiAliasing = 16;
			starling.start();
		}
		
	}
	
}