package services.events.roomTypes
{
	import services.cairngorm.BaseEvent;
	import services.vo.backend.RoomWithBedTypesObjectVO;

	public class AddRoomTypeEvent extends BaseEvent
	{
		public var roomType:RoomWithBedTypesObjectVO = new RoomWithBedTypesObjectVO();
		
		public function AddRoomTypeEvent(type:String)
		{
			super(type);
		}
		
	}
}