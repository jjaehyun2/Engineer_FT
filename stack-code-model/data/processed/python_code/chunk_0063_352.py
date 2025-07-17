package controls.resizers.events {
	import flash.events.Event;

	public class ResizerUpdatedEvent extends Event {
		public function ResizerUpdatedEvent(type:String, value:Number, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
			this.value = value;
		}
		
        public static const TYPE_RESIZER_UPDATED:String = "resizerUpdated";
		
		public var value:Number;

        override public function clone():Event {
            return new ResizerUpdatedEvent(type,value);
        }
	}
}