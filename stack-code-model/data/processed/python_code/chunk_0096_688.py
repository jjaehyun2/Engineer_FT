package services.events.cashShift
{
	import services.controller.AppController;
	import services.cairngorm.BaseEvent;

	public class CloseShiftEvent extends BaseEvent
	{
		public var hotelId:int;
		public var iShiftNumber:int;

		public function CloseShiftEvent( )
		{
			super(AppController.CASHSHIFT_CLOSE_SHIFT);
		}

	}
}