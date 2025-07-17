package com.massiveProCreation.ball.sections.gallery
{
	/*/  IMPORTS /*/
	import com.massiveProCreation.gallery.GalleryCore;
	import com.massiveProCreation.events.CustomEvent;
	import flash.display.Sprite;
	import flash.events.Event;
	
	public class GalleryMain extends GalleryCore
	{
		public function GalleryMain(xmlUrl:String, slideShowDelay:int)
		{
			super(xmlUrl, slideShowDelay);
		}
		/// we override the image loaded function because we need to control the default slideshow 
		override protected function imageLoaded(e:Event):void {
			_images.push(_imageLoader.content);
			_images[_ci].smoothing = true;

			if(_ci == 0 && _slideShowTimer.running){
				nextImage();
				dispatchEvent(new CustomEvent(CustomEvent.IMAGE_LOADED, true, false));	
			} else if (_ci == 0){
				dispatchEvent(new CustomEvent(CustomEvent.IMAGE_LOADED, true, false));					
			}

			loadThumbnail(_ci);
		}

	}
}