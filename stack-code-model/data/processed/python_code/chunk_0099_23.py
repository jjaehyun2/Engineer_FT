package services.command.profiles.travelAgency
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.profiles.ProfileDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.profiles.company.GetCompanyByIdEvent;
	import services.vo.profiles.CompanyProfileVO;

	public class GetTravelAgencyByIdComand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = GetCompanyByIdEvent(event);
			var delegate:ProfileDelegate = new ProfileDelegate(this);
			delegate.getCompanyById(_event as GetCompanyByIdEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			model.profilesModule.curTravelAgency = data as CompanyProfileVO;
			
			super.result(data);
		}
	}
}