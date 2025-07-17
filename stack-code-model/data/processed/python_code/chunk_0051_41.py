package services.events.rates.bar
{
	import services.cairngorm.BaseEvent;

	public class GetBARsByDateEvent extends BaseEvent
	{		
		public var iHotelId:int;
		public var sStartDate:String;
		
		public function GetBARsByDateEvent(type:String)
		{
			super(type);
		}	
	}
}