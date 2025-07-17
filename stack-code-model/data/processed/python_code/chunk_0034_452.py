package services.events.checkOut
{
	import services.cairngorm.BaseEvent;

	public class AddNewItemsEvent extends BaseEvent
	{
		/**
		 *  This property is id of hotel from where leave guest.
		 *  
		 *  #default 0
		 */
		private var _hotelId:Number = 0;
		/**
		 *  This property is id of payment line.
		 *  
		 *  #default 0
		 */
		private var _paymentLineId:Number = 0;
		/**
		 *  This property is list of adding item used by guest.
		 *  
		 *  #default []
		 */
		private var _addedItems:Array = [];
		/**
		 *  This property is id of cashier shift.
		 *  
		 *  @default 0
		 */
		private var _cashierShiftId:Number = 0;

		
		public function AddNewItemsEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
		}
		
		/**
		 *  Id of hotel from where leave guest.
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
		 *  Id of payment line.
		 */
		public function get paymentLineId():Number
		{
			return _paymentLineId;
		}
		/**
		 *  @private
		 */
		public function set paymentLineId(value:Number):void
		{
			_paymentLineId = value;
		}
		
		/**
		 *  List of adding item used by guest.
		 */
		public function get addedItems():Array
		{
			return _addedItems;
		}
		/**
		 *  @private
		 */
		public function set addedItems(value:Array):void
		{
			_addedItems = value;
		}
		
		/**
		 *  Id of cashier shift.
		 */
		public function get cashierShiftId():Number
		{
			return _cashierShiftId;
		}
		/**
		 *  @private
		 */
		public function set cashierShiftId(value:Number):void
		{
			_cashierShiftId = value;
		}
		

	}
}