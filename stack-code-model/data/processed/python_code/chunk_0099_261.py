package services.events.rates.companyRates
{
	import services.cairngorm.BaseEvent;

	public class GetGroupListCompanyRatesEvent extends BaseEvent
	{
		
		public var groupName:String;
		
		public var rateId:int;
		
		public function GetGroupListCompanyRatesEvent(type:String)
		{
			super(type);
		}
		
	}
}