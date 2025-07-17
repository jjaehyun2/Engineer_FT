package com 
{
	import flash.display.Bitmap;
	import flash.display.Loader;
	import flash.display.Sprite;
	import flash.net.URLRequest;
	import flash.events.Event;
	/**
	 * ...
	 * @author iLLuzor // http://illuzor.com // illuzor@gmail.com
	 */
	public class NewLoader extends Sprite {
		
		public function NewLoader() {
			var pLoader:Loader = new Loader();
			pLoader.load(new URLRequest("marker.png"));
			pLoader.contentLoaderInfo.addEventListener(Event.COMPLETE, imageLoaded);
		}
		
		private function imageLoaded(e:Event):void {
			var container:Sprite = new Sprite();
			addChild(container);
			
			var bitmap:Bitmap = e.target.content;
			container.addChild(bitmap);
			
			var bitmap2:Bitmap = new Bitmap(bitmap.bitmapData);
			bitmap2.x = 200;
			container.addChild(bitmap2);
		}
		
	}

}