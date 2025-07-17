package services.command.BDC
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.BDC.BDCDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.BDC.PostTransactionsEvent;

	public class PostTransactionsCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = PostTransactionsEvent(event);
			var delegate:BDCDelegate= new BDCDelegate(this);
			delegate.postTransactions(_event as PostTransactionsEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			super.result(data);
		}
	}
}