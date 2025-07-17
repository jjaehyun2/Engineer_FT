package services.events.rates.companyRates
{
	import services.cairngorm.BaseEvent;

	public class GetTransactionListCompanyRateEvent extends BaseEvent
	{
		public var rateId:int;
		
		public function GetTransactionListCompanyRateEvent(type:String)
		{
			super(type);
		}
		
	}
}