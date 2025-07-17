package views.events {
	import flash.events.Event;

	public class MenuOpenedEvent extends Event {
		public var menu:* = {};
        public static const TYPE_MENU_OPENED_EVENT:String = "menuOpenedEvent";
		
		public function MenuOpenedEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
		}
		
        override public function clone():Event {
            return new MenuOpenedEvent(type);
        }
	}
}