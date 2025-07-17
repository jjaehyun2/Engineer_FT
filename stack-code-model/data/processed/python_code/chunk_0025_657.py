package services.command.profiles.company
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.profiles.ProfileDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.profiles.company.GetCompanyListEvent;
	import services.vo.common.PagerVO;
	import services.vo.profiles.CompanyProfileViewVO;
	
	import mx.collections.ArrayCollection;
	/**
	 *  Command for get list of countries.
	 *  
	 *  @author Artemyev Dmitriy
	 *  @date 08.06.2009
	 */
	public class GetCompanyListCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = GetCompanyListEvent(event);
			var delegate:ProfileDelegate = new ProfileDelegate(this);
			delegate.getCompanyProfileList(_event as GetCompanyListEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			var company:CompanyProfileViewVO;
			var context:PagerVO = data as PagerVO;
			
			model.profilesModule.companyProfileCount = context.lCount;
			model.profilesModule.companyProfileList = new ArrayCollection(context.aObjects);
			
			super.result(data);
		}
	}
}