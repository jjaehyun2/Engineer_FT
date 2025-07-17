package services.events.checkOut
{
	import services.cairngorm.BaseEvent;

	public class AddPaymentsEvent extends BaseEvent
	{
		public var payments:Array = [];
		public var hotelId:Number;
		public var isNeedToPrintReport:Boolean = false;
		public var cashierShiftId:Number = 0;
		
		public function AddPaymentsEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
		}
	}
}