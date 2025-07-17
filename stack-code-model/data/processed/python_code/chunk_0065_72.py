package services.events.backend
{
	import services.cairngorm.BaseEvent;

	public class GetHotelCommonRoomTypesEvent extends BaseEvent
	{
		public var hotelIds:Array = [];
		
		public function GetHotelCommonRoomTypesEvent(type:String)
		{
			super(type);
		}
		
	}
}