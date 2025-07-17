package game
{
	import flash.events.Event;
	
	public class GameEvent extends Event
	{
		public static var CLICK_STARTPANEL_PLAY:String = "CLICK_STARTPANEL_PLAY";
		public function GameEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
		}
	}
}