package services.events.items.itemGroups
{
	import services.cairngorm.BaseEvent;

	public class GetHotelItemsGroupsEvent extends BaseEvent
	{
		// ----------------------------------------------------------- //
		//                          VARIABLES                          //
		// ----------------------------------------------------------- //
		/**
		 *  This property contain id of hotel.
		 */
		private var _hotelId:Number;
		
		// ----------------------------------------------------------- //
		//                    METHODS AND FUNCTIONS                    //
		// ----------------------------------------------------------- //
		/**
		 *  GetHotelItemsGroupsEvent. Constructor.
		 *  
		 *  @param type:String is the type of the event, accessible
		 *         as Event.type.
		 */
		public function GetHotelItemsGroupsEvent(type:String)
		{
			super(type);
		}
		
		// ----------------------------------------------------------- //
		//                      GETTER AND SETTER                      //
		// ----------------------------------------------------------- //
		/**
		 *  Id of hotel, for whom have to get main and sub groups.
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
	}
}