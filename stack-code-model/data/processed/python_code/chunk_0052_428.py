package services.events.hotels
{
	import services.cairngorm.BaseEvent;
	import services.vo.hotels.HotelRoomObjectVO;

	public class AddRoomListEvent extends BaseEvent
	{
		public var room:HotelRoomObjectVO = new HotelRoomObjectVO();
		
		public var firstNumber:int=0;
		public var lastNumber:int=0;
		public var increment:int=0;
		
		
		public function AddRoomListEvent(type:String)
		{
			super(type);
		}
		
	}
}