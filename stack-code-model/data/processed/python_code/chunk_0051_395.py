package services.events.roomTypes
{
	import services.cairngorm.BaseEvent;
	import services.vo.backend.RoomTypesObjectVO;

	public class DeleteRoomTypeEvent extends BaseEvent
	{
		public var roomType:RoomTypesObjectVO = new RoomTypesObjectVO();
		
		public function DeleteRoomTypeEvent(type:String)
		{
			super(type);
		}		
	}
}