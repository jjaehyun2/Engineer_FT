package services.events.common
{
	import services.cairngorm.BaseEvent;

	public class GetSourceCodesEvent extends BaseEvent
	{
		public function GetSourceCodesEvent(type:String)
		{
			super(type);
		}
	}
}