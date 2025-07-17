package services.events.roomTypes
{
	import services.cairngorm.BaseEvent;

	public class SetRoomTypeDescriptionEvent extends BaseEvent
	{
		public var roomTypeId:int;
		public var description:String;
		
		public function SetRoomTypeDescriptionEvent(type:String)
		{
			super(type);
		}
		
	}
}