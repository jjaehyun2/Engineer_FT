package services.events.backend
{
	import services.cairngorm.BaseEvent;

	public class GetCommonDictionariesEvent extends BaseEvent
	{
		
		public function GetCommonDictionariesEvent(type:String)
		{
			super(type);
		}
	}
}