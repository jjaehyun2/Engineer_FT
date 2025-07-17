package services.command.profiles.individual
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.profiles.ProfileDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.profiles.individual.FindProfileBySurnameEvent;
	import services.vo.common.PagerVO;
	
	import mx.collections.ArrayCollection;

	public class FindProfileBySurnameCommand extends BaseCommand
	{
		/**
		 *  @override
		 *  
		 *  @see services.command.BaseCommand#execute
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = FindProfileBySurnameEvent(event);
			var delegate:ProfileDelegate = new ProfileDelegate(this);
			delegate.findProfileBySurname(_event as FindProfileBySurnameEvent);
			
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