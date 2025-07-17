package com.illuzor.funnytests{
	import flash.display.Sprite;
	import flash.events.Event;

	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	[Frame(factoryClass="com.illuzor.funnytests.Preloader")]
	public class Main extends Sprite {

		public function Main() {
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}

		private function init(e:Event = null):void {
			removeEventListener(Event.ADDED_TO_STAGE, init);
			// entry point
		}

	}

}