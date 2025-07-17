package services.events.hotels
{
	import services.cairngorm.BaseEvent;

	public class AddRoomTypesToHotelEvent extends BaseEvent
	{
		public static var MOVE_ROOM_TYPE:String = "moveRoomType";
		
		public function AddRoomTypesToHotelEvent(type:String)
		{
			super(type);
		}
		
	}
}