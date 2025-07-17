package services.command.search
{
	import com.adobe.cairngorm.control.CairngormEvent;

	import services.business.search.SearchDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.search.GetReservationByIdEvent;
	import services.vo.reservation.ReservationVO;

	public class GetReservationByIdCommand extends BaseCommand
	{
		override public function execute(event:CairngormEvent):void
		{
			_event = event as GetReservationByIdEvent;
			var delegate:SearchDelegate = new SearchDelegate( this );
			delegate.getReservationById(event as GetReservationByIdEvent);
			super.execute(event);
		}

		override public function result(data:Object):void
		{
			model.reservationEditModule.reservationForEdit = data as ReservationVO;
			super.result(data);
		}

	}
}