package controls.login.widgets.event {
	import flash.events.Event;

	public class ValidateActivationKeyRequestedEvent extends Event {
		public function ValidateActivationKeyRequestedEvent(type:String, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
		}
		
        public static const TYPE_VALIDATE_ACTIVATION_REQUESTED:String = "validateActivationRequested";

        override public function clone():Event {
            return new ValidateActivationKeyRequestedEvent(type);
        }
	}
}