package services.command.rates.companyRates
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.rates.companyRates.CompanyRatesDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.rates.companyRates.GetGroupListCompanyRatesEvent;
	
	import mx.collections.ArrayCollection;

	public class GetGroupListCompanyRatesCommand extends BaseCommand
	{
		/**
		 *  Interface method. 
		 *  <p>Execute for forwarding the event to the method
		 *  <code>getGroupListCompanyRates()</code>.
		 * 
		 *  @see com.adobe.cairngorm.commands.ICommand
		 *  @see services.events.rates.companyRates.GetGroupListCompanyRatesEvent
		 *  
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = GetGroupListCompanyRatesEvent(event);
			var delegate:CompanyRatesDelegate = new CompanyRatesDelegate(this);
			
			delegate.getGroupListCompanyRates(_event as GetGroupListCompanyRatesEvent);
			super.execute(event);
		}
		/**
		 *  The handler for result of execution of request for
		 *  <code>getGroupListCompanyRates()</code>.
		 */
		override public function result(data:Object):void
		{
			model.transactionModule.systemGroupsList = new ArrayCollection(data as Array);
			super.result(data);
			
		}
		
	}
}