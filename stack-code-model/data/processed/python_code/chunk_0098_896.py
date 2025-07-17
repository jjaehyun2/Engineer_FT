package flexUnit
{
	import services.cairngorm.BaseEvent;

	public class CompleteEvent extends BaseEvent
	{
		public static const OK:int = 1;
		public static const FAULT:int = 2;
		
		public var status:int;
		
		public function CompleteEvent(type:String, status:int = 0)
		{
			super(type, false, false);
			this.status = status;
		}
		
	}
}