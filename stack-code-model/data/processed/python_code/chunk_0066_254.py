package services.events.roomTypes
{
	import services.cairngorm.BaseEvent;

	public class GetRoomTypesPageEvent extends BaseEvent
	{
		public function GetRoomTypesPageEvent(type:String)
		{
			super(type);
		}
		
	}
}