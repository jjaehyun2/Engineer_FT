package services.command.items.itemGroups
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.items.ItemsDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.items.itemGroups.GetSystemGroupsListEvent;
	
	import mx.collections.ArrayCollection;

	public class GetSystemGroupsListCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = GetSystemGroupsListEvent(event);
			var delegate:ItemsDelegate = new ItemsDelegate(this);
			delegate.getSystemItemsGroups(_event as GetSystemGroupsListEvent);
			
			super.execute(event);
		}
		
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			model.transactionModule.systemGroupsList = new ArrayCollection(data as Array);
			
			super.result(data);
		}
	}
}