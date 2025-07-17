package services.command.items.management
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.items.ItemsDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.items.management.SaveHotelTransactionEvent;
	import services.vo.items.HotelItemVO;
	
	import mx.collections.ArrayCollection;

	public class SaveHotelTransactionCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = SaveHotelTransactionEvent(event);
			var delegate:ItemsDelegate = new ItemsDelegate(this);
			delegate.saveHotelTransaction(_event as SaveHotelTransactionEvent);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			var item:HotelItemVO = data as HotelItemVO;
			var provider:ArrayCollection = model.transactionModule.transactionList as ArrayCollection;
			if ((_event as SaveHotelTransactionEvent).index != provider.length)
			{
				// edit mode
				provider.setItemAt(item, (_event as SaveHotelTransactionEvent).index);
			}
			else 
			{
				// add mode
				provider.addItemAt(item, (_event as SaveHotelTransactionEvent).index);
			}
			
			super.result(data);
		}
	}
}