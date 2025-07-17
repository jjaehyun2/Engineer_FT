package services.command.reservation
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.reservation.SaveReservationDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.reservation.SaveReservationEvent;
	
	public class SaveReservationCommand extends BaseCommand
	{
		override public function execute(event:CairngormEvent):void
		{
			_event = SaveReservationEvent(event);
			var delegate:SaveReservationDelegate = new SaveReservationDelegate( this );
			delegate.saveReservation(_event as SaveReservationEvent);
		}

		override public function result(data:Object):void
		{
			model.reservationCreateModule.newReservationID = data as int;
			super.result(data);
		}
	}
}