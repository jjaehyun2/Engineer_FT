package controls.events {
	import flash.events.Event;

	public class DocsListPopulatedEvent extends Event {
		public function DocsListPopulatedEvent(type:String, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
		}
		
        public static const TYPE_DOCSLIST_POPULATED:String = "docsListPopulated";

        override public function clone():Event {
            return new DocsListPopulatedEvent(type);
        }
	}
}