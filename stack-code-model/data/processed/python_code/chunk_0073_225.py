package com.exceptions {
	import flash.display.LoaderInfo;
	import flash.events.UncaughtErrorEvent;
	
	import mx.managers.ISystemManager;
	
	[Mixin]
	[DefaultProperty("handlerActions")]
	public class GlobalExceptionHandler {
		private static var loaderInfo:LoaderInfo;
		
		//[ArrayElementType("com.adobe.ac.logging.GlobalExceptionHandlerAction")]
		public var handlerActions:Array;
		
		public var preventDefault:Boolean;
		
		public static function init(sm:ISystemManager):void {
			loaderInfo = sm.loaderInfo;
		}
		
		public function GlobalExceptionHandler() {
			loaderInfo.uncaughtErrorEvents.addEventListener(UncaughtErrorEvent.UNCAUGHT_ERROR,
				uncaughtErrorHandler);
		}
		
		private function uncaughtErrorHandler(event:UncaughtErrorEvent):void {
			for each (var action:* in handlerActions) {
				try {
					action.handle(event.error);
				} catch (err:Error) {
					action(event.error);
				}
			}
			
			if (preventDefault == true) {
				event.preventDefault();
			}
		}
	}
}