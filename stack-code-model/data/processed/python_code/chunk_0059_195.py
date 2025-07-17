package com.illuzor.engine3d.ui.screens {
	
	import flash.display.Sprite;
	import flash.events.Event;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	
	internal class AboutScreen extends Sprite {
		
		public function AboutScreen() {
			addEventListener(Event.ADDED_TO_STAGE, added);
		}
		
		private function added(e:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, added);
			
		}
		
	}
}