package controls.login.widgets.event {
	import flash.events.Event;

	public class UpdateUserNameRequiredFieldErrorEvent extends Event {
		public function UpdateUserNameRequiredFieldErrorEvent(type:String, value:String, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
			
			this.value = value;
		}
		
        public static const TYPE_UPDATE_USERNAME_REQUIRED_FIELD_ERROR:String = "updateUserNameRequiredFieldError";
        
        public var value:String;

        override public function clone():Event {
            return new UpdateUserNameRequiredFieldErrorEvent(type, this.value);
        }
	}
}