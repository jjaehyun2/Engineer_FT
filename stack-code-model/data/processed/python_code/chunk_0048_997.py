package services.events.reservation
{
	import services.cairngorm.BaseEvent;

	public class GetReservationCaledarDataEvent extends BaseEvent
	{
		public var startDate:String;
				
		public function GetReservationCaledarDataEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
		}
		
	}
}