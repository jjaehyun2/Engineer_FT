package{
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.HTTPStatusEvent;
	import flash.events.IOErrorEvent;
	import flash.events.MouseEvent;
	import flash.events.SecurityErrorEvent;
	import flash.net.URLLoader;
	import flash.net.URLLoaderDataFormat;
	import flash.net.URLRequest;
	import flash.net.URLRequestMethod;
	import flash.net.URLVariables;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	public class Main extends Sprite {
		
		public function Main() {
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void {
			removeEventListener(Event.ADDED_TO_STAGE, init);
			var sprite:Sprite = new Sprite();
			addChild(sprite);
			sprite.x = sprite.y = 100;
			sprite.graphics.beginFill(0x0);
			sprite.graphics.drawRect(0, 0, 100, 100);
			sprite.graphics.endFill();
			sprite.addEventListener(MouseEvent.CLICK, onClick);
			
			
			var str:String = "(dasfaf";
			var xml:XML = XML(str);
			trace(xml.child("f"))
			trace(xml.toString())
		}
		
		private function onClick(e:MouseEvent):void {
			trace("click");
			var url:String = "http://www.inspider.ru/authorization/login/ajax/true/";
			var request:URLRequest = new URLRequest(url);
			var requestVars:URLVariables = new URLVariables();
			requestVars.email = "illuzor@gmail.com";
			requestVars.password = "illusion102";
			request.data = requestVars;
			request.method = URLRequestMethod.POST;
			
			var urlLoader:URLLoader = new URLLoader();
			urlLoader = new URLLoader();
			urlLoader.dataFormat = URLLoaderDataFormat.TEXT;
			urlLoader.addEventListener(Event.COMPLETE, loaderCompleteHandler);
			urlLoader.addEventListener(HTTPStatusEvent.HTTP_STATUS, httpStatusHandler);
			urlLoader.addEventListener(SecurityErrorEvent.SECURITY_ERROR, securityErrorHandler);
			urlLoader.addEventListener(IOErrorEvent.IO_ERROR, ioErrorHandler);
			
			urlLoader.load(request);
		}
		
		private function ioErrorHandler(e:IOErrorEvent):void {
			trace("io error");
		}
		
		private function securityErrorHandler(e:SecurityErrorEvent):void {
			trace("secure error");
		}
		
		private function httpStatusHandler(e:HTTPStatusEvent):void {
			trace("httpStatusHandler:", e.status);
		}
		
		private function loaderCompleteHandler(e:Event):void {
			trace("load complete");
			trace(e.target.data)
		}
		
	}
	
}