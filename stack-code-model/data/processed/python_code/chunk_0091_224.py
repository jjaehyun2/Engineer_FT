package services.events.reservation
{
	/**
	* The GetPackagesRatesForReservationEvent class is 
	*
	* @author  Anton Kirzyk / Ramada
	*
	* @version $Revision 1.0 $ $Date: 2010/02/08 $
	*
	*/	
	
	import services.cairngorm.BaseEvent;
	import services.vo.backend.PackageRequestVO;
		
	public class GetPackagesRatesForReservationEvent extends BaseEvent
	{
		public static const NAME:String = "reservationGetPackagesRatesForReservationEvent";
		
		public var packageRequest:PackageRequestVO = new PackageRequestVO();
		
		public function GetPackagesRatesForReservationEvent(bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(NAME,bubbles,cancelable);
		}

	}
}