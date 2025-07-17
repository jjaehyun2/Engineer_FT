package  {
	
	import flash.events.Event;
	
	public class StartGameEvent extends Event{
		public static const onbtpressed : String = "pleasestartgame";
		public function StartGameEvent(type:String) {
			// constructor code
					super(type);
		}

	}
	
}