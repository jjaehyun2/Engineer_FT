package framework.events
{
	import flash.events.Event;
	
	public class StatusBarMessageEvent extends Event {
		
		public static const SHOW_MESSAGE:String = "StatusBarMessageEvent_showMessage";
		
		public var message:String;
		
		public function StatusBarMessageEvent(type:String, _msg:String = "", bubbles:Boolean=false, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
			message = _msg;
		}
		
		public override function clone():Event {
			return new StatusBarMessageEvent(type, message);
		}
	}
}