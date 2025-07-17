package services.command.items.management
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.items.ItemsDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.items.management.DeleteSystemTransactionEvent;
	import services.vo.items.HotelItemVO;
	
	import mx.collections.ArrayCollection;

	public class DeleteSystemTransactionCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = DeleteSystemTransactionEvent(event);
			var delegate:ItemsDelegate = new ItemsDelegate(this);
			delegate.deleteSystemTransaction(_event as DeleteSystemTransactionEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			var provider:ArrayCollection = model.transactionModule.transactionList as ArrayCollection;
			// delete transaction from list
			for(var i:int = 0; i < provider.length; i++)
			{
				var transaction:HotelItemVO = provider.getItemAt(i) as HotelItemVO;
				if ((_event as DeleteSystemTransactionEvent).sysGroupId == transaction.lId)
				{
					provider.removeItemAt(i);
					break;
				}
			}
			
			super.result(data);
		}
	}
}