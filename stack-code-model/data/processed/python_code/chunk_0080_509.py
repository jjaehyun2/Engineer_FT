package controls.events {
	import flash.events.Event;

	public class ShowDocsListDetailsEvent extends Event {
		public function ShowDocsListDetailsEvent(type:String, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
		}
		
        public static const TYPE_SHOW_DOCSLIST_DETAILS_COMPLETED:String = "showDocsListDetails";

        override public function clone():Event {
            return new ShowDocsListDetailsEvent(type);
        }
	}
}