package services.vo.reservation
{
	import com.adobe.cairngorm.vo.IValueObject;

	[RemoteClass(alias="MapGroupReservation")]
	[Bindable]
	public class GroupReservationVO implements IValueObject
	{
		public var iId:int;
		public var iReservationId:int; 
			
		public var sGroupName:String;
		public var sShowId:String;
		public var bIsRegistrationCard:Boolean; // registration report will be available within the Report screen
			
		/* on this date all available rooms (not picked up rooms) go back into the “normal” availability
		 * and fall out of that special group reservation
		 */
		public var sCutOfDate:String;
		/*that is just the date on which the group/travel agent/company have to decide definitely if they
		 * want to book the rooms and have to send back the signed
		 */
		public var sOptionDate:String;
			
		/*Guests could apply their room inquiry to that keyword, this facilitate the booking for the guest
		 * and the reservation handling for the associate.
		 */
		public var sKeyword:String;
			  
		/**
		 * Array of date. Store quantity and room type in day.  
		 * '2010-03-01' => array( 1 => 10,2 => 20),
		 */
		public var aRoomBlocked:Array; // ReservationRoomBlockedVO
			  
		public var sArrivalDate:String;
		public var sDepartureDate:String;
			
		public var oMapReservation:ReservationVO;
	}
}