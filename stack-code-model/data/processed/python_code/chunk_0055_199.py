package services.events.items.management
{
	import services.events.PageBaseEvent;
	
	public class GetVatPeriodsEvent extends PageBaseEvent
	//getVatPeriods($oUserOptions, $bBasicList, $iItemId)
	{
		// ----------------------------------------------------------- //
		//                          VARIABLES                          //
		// ----------------------------------------------------------- //
		/**
		 *  Basic list or not.
		 */
		private var _bBasicList:Boolean;
		/**
		 *  This property contain id of item of the hotel.
		 */
		private var _iItemId:Number;
		
		// ----------------------------------------------------------- //
		//                    METHODS AND FUNCTIONS                    //
		// ----------------------------------------------------------- //
		/**
		 *  GetHotelTransactionsEvent. Constructor.
		 *  
		 *  @param type:String is the type of the event, accessible
		 *         as Event.type.
		 */
		public function GetVatPeriodsEvent(type:String)
		{
			super(type);
		}
		
		// ----------------------------------------------------------- //
		//                      GETTER AND SETTER                      //
		// ----------------------------------------------------------- //
		/**
		 *  It is basic list or not.
		 */
		public function get bBasicList():Boolean
		{
			return _bBasicList;
		}
		/**
		 *  @private
		 */
		public function set bBasicList(value:Boolean):void
		{
			_bBasicList = value;
		}
		
		/**
		 *  Id of the item of the hotel.
		 */
		public function get iItemId():Number
		{
			return _iItemId;
		}
		/**
		 *  @private
		 */
		public function set iItemId(value:Number):void
		{
			_iItemId = value;
		}
	}
}