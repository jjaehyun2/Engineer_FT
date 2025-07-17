package services.events.roomTypes
{
	import services.cairngorm.BaseEvent;

	public class SetRoomTypeCapacityEvent extends BaseEvent
	{
		public var roomTypeId:int;
		public var capacity:int;
		
		public function SetRoomTypeCapacityEvent(type:String)
		{
			super(type);
		}
		
	}
}