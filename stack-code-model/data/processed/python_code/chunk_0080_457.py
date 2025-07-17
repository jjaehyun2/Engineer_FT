package services.events.checkOut
{
	import services.cairngorm.BaseEvent;

	public class PrintDebitReportEvent extends BaseEvent
	{
		public var paymentId:Number;
		public var hotelId:Number;
		public var isConference:Boolean;
		public var roomId:Number;
		
		public function PrintDebitReportEvent(type:String)
		{
			super(type, bubbles, cancelable);
		}
	}
}