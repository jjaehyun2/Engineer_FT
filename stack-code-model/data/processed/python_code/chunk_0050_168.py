package services.command.profiles.individual
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.profiles.ProfileDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.profiles.individual.GetProfilesPageEvent;
	import services.vo.common.PagerVO;
	
	import mx.collections.ArrayCollection;

	public class GetProfilesPageCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = GetProfilesPageEvent(event);
			var delegate:ProfileDelegate = new ProfileDelegate(this);
			delegate.getProfilesPage(_event as GetProfilesPageEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			var pageContext:PagerVO = data as PagerVO;
			model.profilesModule.individualProfilesCount = pageContext.lCount;
			model.profilesModule.individualPageList = new ArrayCollection(pageContext.aObjects);
			
			super.result(data);
		}
	}
}