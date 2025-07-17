package vyperlogix.events {
	import flash.events.Event;

	public class SuperUserLoggedInEvent extends Event {
		public function SuperUserLoggedInEvent(type:String, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
		}
		
        public static const TYPE_SUPER_USER_LOGGED_IN:String = "superUserLogged_In";

        override public function clone():Event {
            return new SuperUserLoggedInEvent(type);
        }
	}
}