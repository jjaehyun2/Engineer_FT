package services.vo.frontend
{
	[RemoteClass(alias="MapReservationSummary")]
	public class ReservationSummaryVO
	{
		/**
		 * Reservation status - complete or not complete
		 * @var boolean
		 */ 
		public var bStatus:Boolean;

		/**
		 * Confirmation code for reservation
		 * Example "1111-I-222222"
		 * @var String
		 */
		public var sConfirmationCode:String;
		/**
		 * Now only array Block codes. In future may by more information
		 * Example: ([0] =>"1111-I-222222",[1] => "3333-I-777777")
		 * @var array
		 */
		public var aOrderSummary:Array = new Array(); // array order summary information

	}
}