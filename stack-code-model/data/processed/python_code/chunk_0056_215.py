package services.command.reservation
{
	import com.adobe.cairngorm.control.CairngormEvent;

	import services.business.reservation.GetPackagesRatesForReservationDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.reservation.GetPackagesRatesForReservationEvent;

	import mx.collections.ArrayCollection;

	public class GetPackagesRatesForReservationCommand extends BaseCommand
	{
		override public function execute(event:CairngormEvent):void
		{
			_event = GetPackagesRatesForReservationEvent(event);
			var evt:GetPackagesRatesForReservationEvent = GetPackagesRatesForReservationEvent( event );
			var delegate:GetPackagesRatesForReservationDelegate = new GetPackagesRatesForReservationDelegate( this );

			delegate.getPackagesRatesForReservation(evt);
			super.execute(event);

		}

		override public function result(data:Object):void
		{
			model.reservationCreateModule.packagesRates = new ArrayCollection(data as Array);
			super.result(data);
		}

	}
}