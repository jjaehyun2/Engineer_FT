package services.command.profiles.company
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.profiles.ProfileDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.profiles.company.GetSourceGroupListEvent;
	import services.vo.GlobalStorage;
	
	import mx.collections.ArrayCollection;

	public class GetSourceGroupListCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			var evt:GetSourceGroupListEvent = GetSourceGroupListEvent(event);
			var delegate:ProfileDelegate = new ProfileDelegate(this);
			delegate.getSourceGroupList(evt as GetSourceGroupListEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			GlobalStorage.sourceCodesGroups = new ArrayCollection(data as Array);
			
			super.result(data);
		}
	}
}