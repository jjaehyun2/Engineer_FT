package services.events.hotels
{
	import services.cairngorm.BaseEvent;

	public class GetRealRoomTypeListEvent extends BaseEvent
	{
		public static const NAME:String = "GetRealRoomTypeListEvent";

		public var iHotelId:int;

		public function GetRealRoomTypeListEvent(bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(NAME, bubbles, cancelable);
		}

	}
}