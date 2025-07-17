package controls.login.widgets.event {
	import flash.events.Event;

	public class UpdatePasswordVisibilityEvent extends Event {
		public function UpdatePasswordVisibilityEvent(type:String, visible:Boolean, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
			
			this.visible = visible;
		}
		
        public static const TYPE_UPDATE_PASSWORD_VISIBILITY:String = "updatePasswordVisibility";
        
        public var visible:Boolean;

        override public function clone():Event {
            return new UpdatePasswordVisibilityEvent(type, this.visible);
        }
	}
}