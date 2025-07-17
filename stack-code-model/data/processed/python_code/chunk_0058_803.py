package services.events.common
{
	import services.cairngorm.BaseEvent;

	public class GetSystemDateEvent extends BaseEvent
	{
		public function GetSystemDateEvent(type:String)
		{
			super(type);
		}
	}
}