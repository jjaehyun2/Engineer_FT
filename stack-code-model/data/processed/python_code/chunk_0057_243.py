package controls.google.buttons.events {
	import flash.events.Event;

	public class PauseButtonClickedEvent extends Event {
		public function PauseButtonClickedEvent(type:String, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
		}
		
        public static const TYPE_PAUSE_BUTTON_CLICKED:String = "pauseButtonClicked";
        
        override public function clone():Event {
            return new PauseButtonClickedEvent(type);
        }
	}
}