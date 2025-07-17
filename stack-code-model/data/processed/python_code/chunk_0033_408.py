package services.command.items.itemGroups
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.items.ItemsDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.items.itemGroups.DeleteSystemSubGroupEvent;
	import services.vo.items.ItemsGroupVO;

	public class DeleteSystemSubGroupCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = DeleteSystemSubGroupEvent(event);
			var delegate:ItemsDelegate = new ItemsDelegate(this);
			delegate.deleteSystemSubGroup(_event as DeleteSystemSubGroupEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			var item:ItemsGroupVO = model.transactionModule.systemGroupsList.getItemAt((_event as DeleteSystemSubGroupEvent).groupIndex) as ItemsGroupVO;
			item.aSubGroups.splice((_event as DeleteSystemSubGroupEvent).subGroupIndex, 1);
			model.transactionModule.systemGroupsList.setItemAt(item, (_event as DeleteSystemSubGroupEvent).groupIndex); 
			model.transactionModule.systemGroupsList.refresh();
			
			super.result(data);
		}
	}
}