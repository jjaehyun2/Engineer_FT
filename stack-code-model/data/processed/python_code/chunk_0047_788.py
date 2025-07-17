package masputih.patterns.commands {
	import flash.events.Event;

	/**
	 * ...
	 * @author Anggie Bratadinata
	 */
	public class CommandEvent extends Event {

		public static const COMPLETE:String = "commandComplete";
		public static const ERROR:String = "commandError";
		
		public function CommandEvent(type:String){
			super(type, true);

		}

		public override function clone():Event {
			return new CommandEvent(type);
		}

		public override function toString():String {
			return formatToString("CommandEvent", "type", "bubbles", "cancelable", "eventPhase");
		}

	}

}