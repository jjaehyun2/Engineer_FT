package services.command.checkOut
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.checkOut.CheckOutDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.checkOut.DeleteItemEvent;

	public class DeleteItemCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = DeleteItemEvent(event);
			var delegate:CheckOutDelegate = new CheckOutDelegate(this);
			delegate.deleteItem(_event as DeleteItemEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			model.checkOutModule.routingItems.removeItemAt((_event as DeleteItemEvent).index);
			
			super.result(data);
		}
	}
}