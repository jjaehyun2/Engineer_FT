package application.events {
	import flash.events.Event;

	public class CompletedNativeApplicationUpdaterEvent extends Event {
		public function CompletedNativeApplicationUpdaterEvent(type:String, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
		}
		
        public static const TYPE_COMPLETED_NATIVE_APPLICATION_UPDATER:String = "completedNativeApplicationUpdater";

        override public function clone():Event {
            return new CompletedNativeApplicationUpdaterEvent(type);
        }
	}
}