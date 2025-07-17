package services.events.profiles.company
{
	import services.cairngorm.BaseEvent;

	public class GetCompanyListEvent extends BaseEvent
	{
		public var page:int;
		public var count:int;
		public var pattern:String = "";
		
		public function GetCompanyListEvent(type:String)
		{
			super(type);
		}
	}
}