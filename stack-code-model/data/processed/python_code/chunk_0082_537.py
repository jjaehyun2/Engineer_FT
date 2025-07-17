package services.events.inHouse
{
	import services.cairngorm.BaseEvent;
	import services.vo.inHouse.RateChangeVO;

	public class MoveRoomEvent extends BaseEvent
	{
		public var roomIdFrom:Number;
		public var roomIdTo:Number;
		public var orderDateDep:String;
		public var isNeedToUnassign:Boolean;
		public var isNeedToChangeRate:Boolean;
		public var rateChange:RateChangeVO = new RateChangeVO();
		
		public function MoveRoomEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
		}
		
	}
}