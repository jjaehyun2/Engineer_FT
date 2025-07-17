package controls.login.widgets.event {
	import flash.events.Event;

	public class UpdatePasswordTextValueEvent extends Event {
		public function UpdatePasswordTextValueEvent(type:String, value:String, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
			
			this.value = value;
		}
		
        public static const TYPE_UPDATE_PASSWORD_TEXT_VALUE:String = "updatePasswordTextValue";
        
        public var value:String;

        override public function clone():Event {
            return new UpdatePasswordTextValueEvent(type, this.value);
        }
	}
}