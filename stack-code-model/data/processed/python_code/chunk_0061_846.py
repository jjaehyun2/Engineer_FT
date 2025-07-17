package services.command.profiles.individual
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.profiles.ProfileDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.profiles.individual.FindProfileByNameEvent;
	import services.vo.common.PagerVO;
	
	import mx.collections.ArrayCollection;

	public class FindProfileByNameCommand extends BaseCommand
	{
		/**
		 *  @override
		 *  
		 *  @see services.command.BaseCommand#execute
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = FindProfileByNameEvent(event);
			var delegate:ProfileDelegate = new ProfileDelegate(this);
			delegate.findProfileByName(_event as FindProfileByNameEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 *  
		 *  @see services.command.BaseCommand#result
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