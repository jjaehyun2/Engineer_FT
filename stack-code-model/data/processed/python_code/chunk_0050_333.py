package services.events.BDC
{
	import services.controller.AppController;
	import services.cairngorm.BaseEvent;

	public class PostTransactionsEvent extends BaseEvent
	{		
		
		public function PostTransactionsEvent( )
		{
			super(AppController.BDC_POST_TRANSACTIONS);
		}
	}
}