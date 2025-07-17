package com.massiveProCreation.ball.sections {
	/*/  IMPORTS /*/
	
	import com.massiveProCreation.ball.sections.gallery.GalleryHome;
	import com.massiveProCreation.events.CustomEvent;
	
	import flash.display.Sprite;
	
	
	public class Home extends Sprite {
	
		private var _gallery:GalleryHome;
		
		public function Home () {
		}
		public function construct(url:String, effect:String):void {
			// we add the image slide show,add event listeners and setup the effect of the transition, finally we start the gallery slide show
			_gallery = new GalleryHome(url,5000);
			_gallery.addEventListener(CustomEvent.IMAGE_LOADED, loaded, false, 0, true);
			addChild(_gallery);
			_gallery.slideShowStart();
			_gallery.effect = effect;			
		}
		
		private function loaded(e:CustomEvent):void {
			// dispatch event that section is ready to be displayed.
			dispatchEvent(new CustomEvent(CustomEvent.READY_TO_DISPLAY, true, false));				
		}
	}
}