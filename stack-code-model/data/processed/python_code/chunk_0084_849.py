package services.events.BDC
{
	import services.controller.AppController;
	import services.cairngorm.BaseEvent;

	public class TotalLogoutEvent extends BaseEvent
	{
		
		public function TotalLogoutEvent( )
		{
			super(AppController.BDC_TOTAL_LOGOUT);
		}
	}
}