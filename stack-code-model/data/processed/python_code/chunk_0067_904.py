package services.events.rates.companyRates
{
	import services.cairngorm.BaseEvent;
	import services.vo.rates.companyRates.CompanyRateItemVO;

	public class SaveTransactionCompanyRateEvent extends BaseEvent
	{
		public var newItem:CompanyRateItemVO = new CompanyRateItemVO();
		
		public var remId:int;
		
		public function SaveTransactionCompanyRateEvent(type:String)
		{
			super(type);
		}
		
	}
}