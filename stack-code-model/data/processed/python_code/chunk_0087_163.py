package services.command.items.management
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.items.management.GetSystemTransactionsCountDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.items.management.GetSystemTransactionsCountEvent;
	import framework.model.AppModelLocator;

	public class GetSystemTransactionsCountCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = GetSystemTransactionsCountEvent(event);
			var delegate:GetSystemTransactionsCountDelegate = new GetSystemTransactionsCountDelegate(this);
			delegate.getSystemTransactionsCount(_event as GetSystemTransactionsCountEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			model.transactionModule.transactionCount = int(data);
			
			super.result(data);
		}
	}
}