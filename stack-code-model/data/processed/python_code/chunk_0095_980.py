package framework.view.pages.hotels.events
{
	import flash.events.Event;

	public class HotelCheckBedTypeEvent extends Event
	{
		public static var CHECK_CLICK:String = "checkClickEvent";

		public function HotelCheckBedTypeEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
		}
		
	}
}