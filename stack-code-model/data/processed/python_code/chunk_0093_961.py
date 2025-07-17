package services.vo.inHouse
{
	[RemoteClass(alias="MapInHouseSearch")]
	public class InHouseSearchVO
	{
		/**
		 *  This property is pattern for search by number of room.
		 *  
		 *  @default ""
		 */
		public var sRoomNumber:String = "";
		/**
		 *  This property is pattern for search by last name of
		 *  guest.
		 *  
		 *  @default ""
		 */
		public var sLastName:String = "";
		/**
		 *  This property is pattern for search by first name of
		 *  guest.
		 *  
		 *  @default ""
		 */
		public var sFirstName:String = "";
		/**
		 *  This property is pattern for search by company name of
		 *  guest.
		 *  
		 *  @default ""
		 */
		public var sCompany:String = "";
		/**
		 *  This property is pattern for search by city of guest.
		 *  
		 *  @default ""
		 */
		public var sCity:String = "";
		/**
		 *  This property is pattern for search by zip code of
		 *  guest.
		 *  
		 *  @default ""
		 */
		public var sZipCode:String = "";
		/**
		 *  This property is pattern for search by arrival date.
		 *  
		 *  @default ""
		 */
		public var dArrivalDate:String = "";
		/**
		 *  This property is pattern for search by departure date.
		 *  
		 *  @default ""
		 */
		public var dDepartureDate:String = "";
		/**
		 *  Thus property is current in house day.
		 */
		public var dInHouseDate:String = ""
	}
}