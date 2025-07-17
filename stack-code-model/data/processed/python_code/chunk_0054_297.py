package services.events.inHouse
{
	import services.cairngorm.BaseEvent;

	public class GetVirtualRoutingEvent extends BaseEvent
	{
		public var roomId:Number;
		public var date:String;
		
		public function GetVirtualRoutingEvent(type:String)
		{
			super(type, bubbles, cancelable);
		}
	}
}