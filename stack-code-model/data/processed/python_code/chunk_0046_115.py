package services.command.checkOut
{
	import flash.utils.Dictionary;
	
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.checkOut.CheckOutDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.checkOut.AdjustItemEvent;
	import framework.view.pages.checkOut.control.AttachedItemsToAccountView;
	import services.vo.checkOut.itemRouting.ItemCheckOutVO;
	
	import mx.collections.ArrayCollection;

	public class AdjustItemCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = AdjustItemEvent(event);
			var delegate:CheckOutDelegate = new CheckOutDelegate(this);
			delegate.adjustItem(_event as AdjustItemEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			var newItem:ItemCheckOutVO = data as ItemCheckOutVO;
			var attachedItemsView:Dictionary = model.checkOutModule.attachedItemsView;
				
			// Check place where the function was called. If the function
			// is called from the collection of all routing items, simply
			// replace it in the collection, but if one of attached view
			// with the items attached to the account, have to make the
			// replace this item in the main and in the attached collections.
			if ((_event as AdjustItemEvent).isAttached)
			{
				var attachedView:AttachedItemsToAccountView = attachedItemsView[(_event as AdjustItemEvent).attachedId] as AttachedItemsToAccountView;
				if (attachedView)
				{
					attachedView.dataProvider.setItemAt(newItem, (_event as AdjustItemEvent).index);
				}
				// find item in the main collection of routing items.
				var routingItems:ArrayCollection = model.checkOutModule.routingItems;
				for(var i:int = 0; i < routingItems.length; i++)
				{
					var item:ItemCheckOutVO = routingItems.getItemAt(i) as ItemCheckOutVO;
					if (newItem.lId == item.lId)
					{
						var oldItem:ItemCheckOutVO = model.checkOutModule.routingItems.getItemAt(i) as ItemCheckOutVO;
						newItem.bIsChecked = oldItem.bIsChecked;
						newItem.bIsSelected = oldItem.bIsSelected;
						model.checkOutModule.routingItems.setItemAt(newItem, i);
						break;
					}
				}
			}
			else
			{
				model.checkOutModule.routingItems.setItemAt(newItem, (_event as AdjustItemEvent).index);
			}
			
			super.result(data);
		}
	}
}