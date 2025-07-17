package services.command.rates.companyRates
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.rates.companyRates.CompanyRatesDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.rates.companyRates.DeleteTransactionCompanyRateEvent;
	import services.vo.rates.companyRates.CompanyRateItemVO;

	public class DeleteTransactionCompanyRateCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = DeleteTransactionCompanyRateEvent( event );
			var delegate:CompanyRatesDelegate = new CompanyRatesDelegate( this );
			
			delegate.deleteTransactionCompanyRate(_event as DeleteTransactionCompanyRateEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			for (var i:int = 0; i < model.ratesModule.ratesData.length; i++)
				if ((model.ratesModule.currentTransactionList.getItemAt(i) as CompanyRateItemVO).iId == (_event as DeleteTransactionCompanyRateEvent).transactionToDeleteId) 
				{
					model.ratesModule.currentTransactionList.removeItemAt(i);
					break;
				}
			model.ratesModule.currentRate.iRateId = int(data);
			super.result(data);
		}	
		
		
	}
}