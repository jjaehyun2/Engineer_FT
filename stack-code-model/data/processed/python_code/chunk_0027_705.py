package net.qb9.hades.push
{
	import flash.events.EventDispatcher;
	import flash.events.StatusEvent;
	
	public class PushExtension extends EventDispatcher
	{
		
		private static var instance:PushExtension = null;
		
		public static function getInstance():PushExtension {
			if ( instance == null ) instance = new PushExtension(new SingletonEnforcer());
			return instance;
		}
		
		public function PushExtension(enforcer:SingletonEnforcer) {
			log("CONSTRUCTOR");
		}
		
		private function log(msg:*):void{
			trace("[ PushExtensionDefault ] " + msg);
		}
		
		public function statusHandle(e:StatusEvent):void{
			log("statusHandle e.type: "+e.type);
			dispatchEvent(e);
		}
		
		public function initExtension():void {
			log("initExtension");
		}
		
		public function getToken():String {
			return "token";
		}
		
	}
}

class SingletonEnforcer {}