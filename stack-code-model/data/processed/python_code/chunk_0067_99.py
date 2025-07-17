package views.events {
	import flash.events.Event;

	public class CreationCompleteEvent extends Event {
		public function CreationCompleteEvent(type:String, datum:Object, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
			
			this.datum = datum;
		}
		
        public static const TYPE_CREATION_COMPLETE:String = "CreationComplete";
        
        public var datum:Object;

        override public function clone():Event {
            return new CreationCompleteEvent(type, datum);
        }
	}
}