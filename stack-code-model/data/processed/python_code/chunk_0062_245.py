package controls.login.widgets.event {
	import flash.events.Event;

	public class ValidatePasswordRequestedEvent extends Event {
		public function ValidatePasswordRequestedEvent(type:String, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
		}
		
        public static const TYPE_VALIDATE_PASSWORD_REQUESTED_ERROR:String = "validatePasswordRequested";
        
        override public function clone():Event {
            return new ValidatePasswordRequestedEvent(type);
        }
	}
}