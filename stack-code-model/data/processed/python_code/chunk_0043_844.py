package services.command.profiles.travelAgency
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.profiles.ProfileDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.profiles.company.SaveCompanyProfileEvent;
	import services.vo.profiles.CompanyProfileViewVO;
	
	import mx.collections.ArrayCollection;

	public class SaveTravelAgencyCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = SaveCompanyProfileEvent(event);
			var delegate:ProfileDelegate = new ProfileDelegate(this);
			delegate.saveCompanyProfile(_event as SaveCompanyProfileEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			var item:CompanyProfileViewVO = data as CompanyProfileViewVO;
			var provider:ArrayCollection = model.profilesModule.travelAgencyList;
			if ((_event as SaveCompanyProfileEvent).index != provider.length)
			{
				// edit mode
				provider.removeItemAt((_event as SaveCompanyProfileEvent).index);
				provider.addItemAt(item, (_event as SaveCompanyProfileEvent).index);
			}
			else
			{
				// add mode
				provider.addItemAt(item, (_event as SaveCompanyProfileEvent).index);
			}
			model.profilesModule.travelAgencyList.refresh();
			
			super.result(data);
		}
	}
}