package services.events.checkOut
{
	import services.cairngorm.BaseEvent;

	public class DetachItemToAccountEvent extends BaseEvent
	{
		// ===================================================================== //
		//                        VARIABLES AND CONSTANTS                        //
		// ===================================================================== //
		/**
		 *  This property is id of attaching item.
		 */
		private var _itemId:Number;
		
		// ===================================================================== //
		//                      COMMON METHODS AND HANDLERS                      //
		// ===================================================================== //
		/**
		 *  DetachItemToAccountEvent. Constructor.
		 *
		 *  @param type:String — The type of the event, accessible as BaseEvent
		 */
		public function DetachItemToAccountEvent(type:String)
		{
			super(type);
		}
		
		// ===================================================================== //
		//                       GETTER AND SETTER HANDLERS                      //
		// ===================================================================== //
		/**
		 *  Id of attaching items.
		 */
		public function get itemId():Number
		{
			return _itemId;
		}
		/**
		 *  @private
		 */
		public function set itemId(value:Number):void
		{
			_itemId = value;
		}
	}
}