package controls.login.widgets.event {
	import flash.events.Event;

	public class UpdateUserNameVisibilityEvent extends Event {
		public function UpdateUserNameVisibilityEvent(type:String, visible:Boolean, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
			
			this.visible = visible;
		}
		
        public static const TYPE_UPDATE_USERNAME_VISIBILITY:String = "updateUserNameVisibility";
        
        public var visible:Boolean;

        override public function clone():Event {
            return new UpdateUserNameVisibilityEvent(type, this.visible);
        }
	}
}