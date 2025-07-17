package services.events.frontend
{
	import services.cairngorm.BaseEvent;

	public class GetRoomListByOrderEvent extends BaseEvent
	{
		public var startDate:String;
		public var endDate:String;
		public var aRoomSettings:Array = [];
		public var idStage:Number;
		public var iRoomType:Number;
		
		public function GetRoomListByOrderEvent(type:String)
		{
			super(type);
		}
		
	}
}