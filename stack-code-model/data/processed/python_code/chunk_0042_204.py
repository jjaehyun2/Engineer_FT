package services.command.items.itemGroups
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.items.ItemsDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.items.itemGroups.DeleteHotelSubGroupEvent;
	import services.vo.items.ItemsGroupVO;

	public class DeleteHotelSubGroupCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = DeleteHotelSubGroupEvent(event);
			var delegate:ItemsDelegate = new ItemsDelegate(this);
			delegate.deleteHotelSubGroup(_event as DeleteHotelSubGroupEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			var item:ItemsGroupVO = model.transactionModule.hotelGroupsList.getItemAt((_event as DeleteHotelSubGroupEvent).groupIndex) as ItemsGroupVO;
			item.aSubGroups.splice((_event as DeleteHotelSubGroupEvent).subGroupIndex, 1); 
			model.transactionModule.hotelGroupsList.refresh();
			
			super.result(data);
		}
	}
}