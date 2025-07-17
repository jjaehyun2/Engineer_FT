package controls.login.events {
	import flash.events.Event;

	public class ActivationCompletedEvent extends Event {
		public function ActivationCompletedEvent(type:String, datum:Object, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
			
			this.datum = datum;
		}
		
        public static const TYPE_ACTIVATION_COMPLETED:String = "activationCompleted";
        
        public var datum:Object;

        override public function clone():Event {
            return new ActivationCompletedEvent(type, datum);
        }
	}
}