package services.events.checkOut
{
	import services.cairngorm.BaseEvent;

	public class GetItemsRoutingEvent extends BaseEvent
	{
		// ===================================================================== //
		//                        VARIABLES AND CONSTANTS                        //
		// ===================================================================== //
		/**
		 *  This property is id of hotel.
		 */
		private var _hotelId:Number;
		/**
		 *  This property is list with profile's id.
		 */
		private var _profileIds:Array;
		
		// ===================================================================== //
		//                      COMMON METHODS AND HANDLERS                      //
		// ===================================================================== //
		/**
		 *  GetItemsRoutingEvent. Constructor.
		 *
		 *  @param type:String — The type of the event, accessible as BaseEvent
		 */
		public function GetItemsRoutingEvent(type:String)
		{
			super(type);
		}
		
		// ===================================================================== //
		//                       GETTER AND SETTER HANDLERS                      //
		// ===================================================================== //
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
		 *  The list with profile's id.
		 */
		public function get profileIds():Array
		{
			return _profileIds;
		}
		/**
		 *  @private
		 */
		public function set profileIds(value:Array):void
		{
			_profileIds = value;
		}
	}
}