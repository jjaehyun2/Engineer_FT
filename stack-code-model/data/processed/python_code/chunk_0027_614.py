package services.events.items.management
{
	import services.events.PageBaseEvent;
	
	public class GetHotelTransactionsEvent extends PageBaseEvent
	{
		// ----------------------------------------------------------- //
		//                          VARIABLES                          //
		// ----------------------------------------------------------- //
		/**
		 *  This property contain id of the hotel.
		 */
		private var _hotelId:Number;
		/**
		 *  This property contain id of the sub group of the hotel.
		 */
		private var _groupId:Number;
		
		// ----------------------------------------------------------- //
		//                    METHODS AND FUNCTIONS                    //
		// ----------------------------------------------------------- //
		/**
		 *  GetHotelTransactionsEvent. Constructor.
		 *  
		 *  @param type:String is the type of the event, accessible
		 *         as Event.type.
		 */
		public function GetHotelTransactionsEvent(type:String)
		{
			super(type);
		}
		
		// ----------------------------------------------------------- //
		//                      GETTER AND SETTER                      //
		// ----------------------------------------------------------- //
		/**
		 *  Id of the hotel.
		 */
		public function get hotelId():Number
		{
			return _hotelId;
		}
		/**
		 *  @private
		 */
		public function set hotelId(value:Number):void
		{
			_hotelId = value;
		}
		
		/**
		 *  Id of the sub group of the hotel.
		 */
		public function get groupId():Number
		{
			return _groupId;
		}
		/**
		 *  @private
		 */
		public function set groupId(value:Number):void
		{
			_groupId = value;
		}
	}
}