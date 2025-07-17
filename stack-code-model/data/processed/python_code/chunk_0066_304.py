package services.events.reservation
{
	/**
	* The SaveGroupReservationEvent class is 
	*
	* @author  Anton Kirzyk / Ramada
	*
	* @version $Revision 1.0 $ $Date: 2010/04/27 $
	*
	*/		
	
	import services.cairngorm.BaseEvent;
	import services.vo.reservation.GroupReservationVO;

	public class SaveGroupReservationEvent extends BaseEvent
	{
		
		public static const NAME:String = "saveGroupReservationEvent";
		
		public var oMapGroupReservation:GroupReservationVO;
		
		public function SaveGroupReservationEvent(bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(NAME, bubbles, cancelable);
		}
		
	}
}