package controls.login.events {
	import flash.events.Event;

	public class ResendActivationEvent extends Event {
		public function ResendActivationEvent(type:String, datum:Object, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
			
			this.datum = datum;
		}
		
        public static const TYPE_RESEND_ACTIVATION:String = "resendActivation";
        
        public var datum:Object;

        override public function clone():Event {
            return new ResendActivationEvent(type, datum);
        }
	}
}