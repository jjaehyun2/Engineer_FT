package services.command.checkOut
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.checkOut.CheckOutDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.checkOut.AddNewItemsEvent;
	import services.vo.checkOut.itemRouting.ItemCheckOutVO;

	public class AddNewItemsCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = AddNewItemsEvent(event);
			var delegate:CheckOutDelegate = new CheckOutDelegate(this);
			delegate.addNewItems(_event as AddNewItemsEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			var addedItems:Array = data as Array;
			
			for(var i:int = 0; i < addedItems.length; i++)
			{
				model.checkOutModule.routingItems.addItem(addedItems[i] as ItemCheckOutVO);
			}
			
			super.result(data);
		}
	}
}