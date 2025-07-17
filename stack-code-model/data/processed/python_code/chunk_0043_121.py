package services.events.checkOut
{
	import services.cairngorm.BaseEvent;

	public class GetCheckoutStateFromInHouseEvent extends BaseEvent
	{
		// ----------------------------------------------------------- //
		//                          VARIABLES                          //
		// ----------------------------------------------------------- //
		/**
		 *  This property is id of room.
		 *  
		 *  @default []
		 */
		private var _roomId:Number = 0;
		/**
		 *  This property is id of hotel.
		 *  
		 *  @default 0
		 */
		private var _hotelId:Number = 0;
		/**
		 *  This property is date of check out by guest.
		 */
		private var _someDate:String = "";
		
		// ----------------------------------------------------------- //
		//                    METHODS AND FUNCTIONS                    //
		// ----------------------------------------------------------- //
		/**
		 *  GetCheckoutStateFromInHouseEvent. Constructor.
		 *  
		 *  @param type:String is the type of the event, accessible
		 *         as Event.type.
		 */
		public function GetCheckoutStateFromInHouseEvent(type:String)
		{
			super(type);
		}
		
		// ----------------------------------------------------------- //
		//                      GETTER AND SETTER                      //
		// ----------------------------------------------------------- //
		/**
		 *  Id of room
		 */
		public function get roomId():Number
		{
			return _roomId;
		}
		/**
		 *  @private
		 */
		public function set roomId(value:Number):void
		{
			_roomId = value;
		}
		
		/**
		 *  Id of hotel.
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
		 *  The date of check out by guest.
		 */
		public function get someDate():String
		{
			return _someDate;
		}
		/**
		 *  @private
		 */
		public function set someDate(value:String):void
		{
			_someDate = value;
		}
	}
}