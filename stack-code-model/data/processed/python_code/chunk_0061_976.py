package services.command.reservation
{
	import com.adobe.cairngorm.control.CairngormEvent;

	import services.business.reservation.GetCompanyRatesForReservationDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.reservation.GetCompanyRatesForReservationEvent;

	import mx.collections.ArrayCollection;

	public class GetCompanyRatesForReservationCommand extends BaseCommand
	{
		override public function execute(event:CairngormEvent):void
		{
			_event = GetCompanyRatesForReservationEvent(event);
			var evt:GetCompanyRatesForReservationEvent = GetCompanyRatesForReservationEvent( event );
			var delegate:GetCompanyRatesForReservationDelegate = new GetCompanyRatesForReservationDelegate( this );

			delegate.getCompanyRatesForReservation(evt);
			super.execute(event);

		}

		override public function result(data:Object):void
		{
			super.result(data);
			model.reservationCreateModule.companyRates = new ArrayCollection(data as Array);
		}

	}
}