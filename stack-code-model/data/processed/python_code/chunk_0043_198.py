package services.events.hotels
{
	import services.cairngorm.BaseEvent;

	public class GetHotelRoomListEvent extends BaseEvent
	{
		public function GetHotelRoomListEvent(type:String)
		{
			super(type);
		}
		
	}
}