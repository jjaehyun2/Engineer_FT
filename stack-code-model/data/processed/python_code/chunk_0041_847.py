package services.events.miscellaneous.countries
{
	import services.cairngorm.BaseEvent;

	public class GetCountryEvent extends BaseEvent
	{
		public var loadDefault:Boolean = true;
		
		public function GetCountryEvent(type:String)
		{
			super(type);
		}
		
	}
}