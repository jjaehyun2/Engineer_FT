package services.command.reservation
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import mx.collections.ArrayCollection;
	
	import services.business.reservation.GetReservationCaledarDataDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.reservation.GetReservationCaledarDataEvent;
	import services.vo.reservation.ReservationCalendarVO;

	public class GetReservationCaledarDataCommand extends BaseCommand
	{
		override public function execute(event:CairngormEvent):void
		{
			_event = GetReservationCaledarDataEvent(event);
			var delegate:GetReservationCaledarDataDelegate = new GetReservationCaledarDataDelegate(this);
			delegate.getReservationCaledarData(_event as GetReservationCaledarDataEvent);
			super.execute(event);
		}

		override public function result(data:Object):void
		{			
			model.reservationCreateModule.aCalendarRoomStatus.removeAll();
			model.reservationCreateModule.aCalendar.removeAll();
			model.reservationCreateModule.aGroupCalendar.removeAll();
			
			//	Add
			if((data as ReservationCalendarVO).aCalendarRoomStatus != null)
			{
				model.reservationCreateModule.aCalendarRoomStatus = new ArrayCollection((data as ReservationCalendarVO).aCalendarRoomStatus);
			}
			
			if((data as ReservationCalendarVO).aCalendar != null)
			{
				model.reservationCreateModule.aCalendar = new ArrayCollection((data as ReservationCalendarVO).aCalendar);
			}
			
			if((data as ReservationCalendarVO).aGroupCalendar != null)
			{
				model.reservationCreateModule.aGroupCalendar = new ArrayCollection((data as ReservationCalendarVO).aGroupCalendar);
			}			
			super.result(data);
		}
	}
}