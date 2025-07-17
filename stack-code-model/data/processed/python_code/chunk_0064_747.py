package controls.login.widgets.event {
	import flash.events.Event;

	public class HidePasswordErrorTipEvent extends Event {
		public function HidePasswordErrorTipEvent(type:String, value:Boolean, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
			
			this.value = value;
		}
		
        public static const TYPE_HIDE_PASSWORD_ERRORTIP:String = "hidePasswordErrorTip";
        
        public var value:Boolean;

        override public function clone():Event {
            return new HidePasswordErrorTipEvent(type, this.value);
        }
	}
}