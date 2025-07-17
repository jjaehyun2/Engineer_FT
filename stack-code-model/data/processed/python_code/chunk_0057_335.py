package services.events.search
{
	import services.controller.AppController;
	import services.cairngorm.BaseEvent;
	import services.vo.search.CancelationReason;

	public class CancelReservationEvent extends BaseEvent
	{
		public var reservationId:int;
		public var reason:CancelationReason;

		public function CancelReservationEvent(bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(AppController.CANCEL_RESERVATION, bubbles, cancelable);
		}

	}
}