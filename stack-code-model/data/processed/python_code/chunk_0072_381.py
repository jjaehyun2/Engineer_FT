package controls.timers.events {
	import flash.events.Event;
	
	public class OpenEditorEvent extends Event {
		public function OpenEditorEvent(type:String, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
		}
		
		public static const TYPE_OPEN_EDITOR:String = "OpenEditorEvent";
		
		override public function clone():Event {
			return new OpenEditorEvent(type);
		}
	}
}