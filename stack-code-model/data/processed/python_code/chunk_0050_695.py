package services.command.checkOut
{
	import flash.utils.Dictionary;
	
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.checkOut.CheckOutDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.checkOut.SplitItemEvent;
	import framework.view.pages.checkOut.control.AttachedItemsToAccountView;
	import services.vo.checkOut.itemRouting.ItemCheckOutVO;
	
	import mx.collections.ArrayCollection;

	public class SplitItemCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = SplitItemEvent(event);
			var delegate:CheckOutDelegate = new CheckOutDelegate(this);
			delegate.splitItem(_event as SplitItemEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			var item:ItemCheckOutVO;
			var attachedItemsView:Dictionary = model.checkOutModule.attachedItemsView;
				
			// Check place where the function was called. If the function
			// is called from the collection of all routing items, simply
			// replace it in the collection, but if one of attached view
			// with the items attached to the account, have to make the
			// replace this item in the main and in the attached collections.
			if ((_event as SplitItemEvent).isAttached)
			{
				var attachedView:AttachedItemsToAccountView = attachedItemsView[(_event as SplitItemEvent).attachedId] as AttachedItemsToAccountView;
				if (attachedView)
				{
					attachedView.dataProvider.removeItemAt((_event as SplitItemEvent).index);
					
					for each(item in (data as Array))
					{
						attachedView.dataProvider.addItem(item);
					}
					
					attachedView.dataProvider.refresh();
				}
				// find item in the main collection of routing items.
				var oldItem:ItemCheckOutVO;
				var newItem:ItemCheckOutVO
				var routingItems:ArrayCollection = model.checkOutModule.routingItems;
				for(var i:int = 0; i < routingItems.length; i++)
				{
					item = routingItems.getItemAt(i) as ItemCheckOutVO;
					for each(newItem in (data as Array))
					{
						if (newItem.lId == item.lId)
						{
							model.checkOutModule.routingItems.removeItemAt(i);
							oldItem = item.clone() as ItemCheckOutVO;
							oldItem.bIsChecked = item.bIsChecked;
							oldItem.bIsSelected = item.bIsSelected;
							i--;
						}
					}
				}
				for each(newItem in (data as Array))
				{
					newItem.bIsChecked = oldItem.bIsChecked;
					newItem.bIsSelected = oldItem.bIsSelected;
					model.checkOutModule.routingItems.addItem(newItem);
				}
			}
			else
			{
				model.checkOutModule.routingItems.removeItemAt((_event as SplitItemEvent).index);
				
				for each(item in (data as Array))
				{
					model.checkOutModule.routingItems.addItem(item);
				}
			}
			
			model.checkOutModule.routingItems.refresh();
			
			super.result(data);
		}
	}
}