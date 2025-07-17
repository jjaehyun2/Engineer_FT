package services.events.inHouse
{
	import services.cairngorm.BaseEvent;

	public class GetAvailableRoomsListEvent extends BaseEvent
	{
		public var profileId:Number;
		public var orderId:Number;
		public var hotelId:Number;
		public var stage:Number;
		
		public function GetAvailableRoomsListEvent(type:String)
		{
			super(type);
		}
	}
}