package services.events.hotels
{
	import services.cairngorm.BaseEvent;

	public class GetHotelStageListEvent extends BaseEvent
	{
		
		public function GetHotelStageListEvent(type:String)
		{
			super(type);
		}
		
	}
}