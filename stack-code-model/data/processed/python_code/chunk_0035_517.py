package services.command.rates.companyRates
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.rates.companyRates.CompanyRatesDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.rates.companyRates.SaveCompanyRateEvent;
	import services.vo.rates.companyRates.CompanyRateGroupVO;
	import services.vo.rates.companyRates.CompanyRateObjectVO;

	public class SaveCompanyRateCommand extends BaseCommand
	{
		override public function execute(event:CairngormEvent):void
		{
			_event = SaveCompanyRateEvent( event );
			var delegate:CompanyRatesDelegate = new CompanyRatesDelegate( this );
			
			delegate.saveCompanyRate( _event as SaveCompanyRateEvent );
			super.execute( event );
		}
		
		override public function result(data:Object):void
		{
			if ((_event as SaveCompanyRateEvent).companyRate.iRateId == 0)
			{
				model.ratesModule.ratesData.addItemAt (data as CompanyRateObjectVO ,0);
			}
			else
			{
				for (var i:int = 0; i < model.ratesModule.ratesData.length; i++)
				{
					if ((_event as SaveCompanyRateEvent).companyRate.iRateId ==  (model.ratesModule.ratesData.getItemAt(i) as CompanyRateGroupVO).iRateId)
						model.ratesModule.ratesData.setItemAt(data, i);
				}
			}
			super.result( data );	
		}
		
	}
}