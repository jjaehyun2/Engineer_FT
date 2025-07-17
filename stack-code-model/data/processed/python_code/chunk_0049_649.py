package h2olib.events
{
	import flash.events.Event;

	public class SearchBoxEvent extends Event
	{
		public static const CHANGE_BY_FOCUS:String = "changeByFocus";
		
		public function SearchBoxEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
		}
	}
}