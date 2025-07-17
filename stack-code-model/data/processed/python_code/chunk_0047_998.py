package services.events.BDC
{
	import services.controller.AppController;
	import services.cairngorm.BaseEvent;

	public class CheckProfilesEvent extends BaseEvent
	{
		
		public function CheckProfilesEvent( )
		{
			super(AppController.BDC_CHECK_PROFILES);
		}
	}
}