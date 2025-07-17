package services.command.rates.companyRates
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.rates.companyRates.CompanyRatesDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.rates.companyRates.GetCompanyRatesCountEvent;

	public class GetCompanyRatesCountCommand extends BaseCommand
	{
		override public function execute(event:CairngormEvent):void
		{
			_event = GetCompanyRatesCountEvent( event );
			var delegate:CompanyRatesDelegate = new CompanyRatesDelegate( this );
			
			delegate.getCompanyRatesCount( _event as GetCompanyRatesCountEvent);
			
			super.execute(event);
		}
		
		override public function result(data:Object):void
		{	
			model.ratesModule.countCompanyRates = data as int;
			
			super.result(data);
		}
		
		
	}
}