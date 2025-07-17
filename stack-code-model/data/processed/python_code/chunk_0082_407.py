package services.events.hotels
{
	import services.cairngorm.BaseEvent;
	import services.vo.hotels.HotelStageObjectVO;

	public class AddFloorEvent extends BaseEvent
	{
		public var stage:HotelStageObjectVO = new HotelStageObjectVO();
		
		public function AddFloorEvent(type:String)
		{
			super(type);
		}
		
	}
}