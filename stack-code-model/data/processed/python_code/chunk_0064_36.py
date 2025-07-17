package services.events.checkOut
{
	import services.cairngorm.BaseEvent;

	public class DetachPackageFromAccountEvent extends BaseEvent
	{
		public var packageId:Number;
		public var paymentLineId:Number;
		public var accountId:Number;
		
		public function DetachPackageFromAccountEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
		}
		
	}
}