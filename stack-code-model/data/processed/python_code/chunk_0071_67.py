package  {
	import flash.display.DisplayObject;
	import flash.display.Loader;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.net.URLRequest;
	import flash.text.TextField;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	public class Preloader extends Sprite {
		
		public function Preloader() {
			
			var text:TextField = new TextField();
			text.text = "Loading";
			text.textColor = 0x808000;
			addChild(text);
			
			var loader:Loader = new Loader();
			loader.load(new URLRequest("SWFLoadingTest.swf"));
			loader.contentLoaderInfo.addEventListener(Event.COMPLETE, onLoaded);
			addChild(loader)
		}
		
		private function onLoaded(e:Event):void {
			//addChild(e.target.content as DisplayObject);
		}
		
	}

}