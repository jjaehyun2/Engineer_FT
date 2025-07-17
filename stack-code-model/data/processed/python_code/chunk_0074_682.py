package com.illuzor.otherside {
	
	import flash.display.Bitmap;
	import flash.display.Loader;
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import flash.net.URLRequest;
	import flash.ui.Multitouch;
	import flash.ui.MultitouchInputMode;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class Preloader extends Sprite {
		
		[Embed(source = "../../../../assets/loadingImage.png")]
		private const LoadingImageClass:Class;
		private var loadingBitmap:Bitmap;
		
		public function Preloader() {
			stage.scaleMode = StageScaleMode.NO_SCALE;
			stage.align = StageAlign.TOP_LEFT;
			Multitouch.inputMode = MultitouchInputMode.TOUCH_POINT;
			addEventListener(Event.ADDED_TO_STAGE, onAdded);
		}
		
		private function onAdded(e:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, onAdded);
			
			loadingBitmap = new LoadingImageClass() as Bitmap;
			addChild(loadingBitmap);
			loadingBitmap.x = (stage.stageWidth - loadingBitmap.width) >> 1;
			loadingBitmap.y = (stage.stageHeight - loadingBitmap.height) >> 1;
			
			var loader:Loader = new Loader();
			loader.load(new URLRequest("game.swf"));
			loader.contentLoaderInfo.addEventListener(Event.COMPLETE, onLoaded);
		}
		
		private function onLoaded(e:Event):void {
			e.target.removeEventListener(Event.COMPLETE, onLoaded);
			removeChildren();
			loadingBitmap.bitmapData.dispose();
			addChild(e.target.content);
		}
		
	}
}