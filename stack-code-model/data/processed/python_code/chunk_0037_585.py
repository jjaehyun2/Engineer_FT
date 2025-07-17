package services.command.rates.companyRates
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.rates.companyRates.CompanyRatesDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.rates.companyRates.GetItemCountCompanyRatesEvent;

	public class GetItemCountCompanyRatesCommand extends BaseCommand
	{	
		/**
		 *  Interface method. 
		 *  <p>Execute for forwarding the event to the method
		 *  <code>getSystemTransactionsCount()</code>.
		 *  
		 *  @param event:CairngormEvent
		 *  
		 *  @see services.events.rates.companyRates.GetItemCountCompanyRatesEvent
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = GetItemCountCompanyRatesEvent(event);
			var delegate:CompanyRatesDelegate = new CompanyRatesDelegate(this);
			delegate.getItemCountCompanyRates(_event as GetItemCountCompanyRatesEvent);
			super.execute(event);
		}
		/**
		 *  The handler to get result of the execution by remote call for
		 *  <code>GetItemCountCompanyRates()</code>.
		 *  <p>This method is called by a service when the return value
		 *  has been received.
		 *  
		 *  @param data:Object - result of the remote call.
		 */
		override public function result(data:Object):void
		{
			model.transactionModule.transactionCount = int(data);
			
			super.result(data);
		}
	
	}
}