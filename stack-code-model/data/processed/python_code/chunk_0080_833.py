package services.events.hotels
{
	import services.cairngorm.BaseEvent;

	public class GetHotelRoomTypesEvent extends BaseEvent
	{
		public function GetHotelRoomTypesEvent(type:String)
		{
			super(type);
		}
	}
}