package services.events.backend
{
	import com.adobe.cairngorm.control.CairngormEvent;
	/**
	 *  AddHotelSubGroupsEvent.
	 *  <p>This event need to add new sub groups into exist main group for each
	 *  hotel, which existed in the system. 
	 *  
	 *  @see com.adobe.cairngorm.control.CairngormEvent
	 */
	public class AddHotelSubGroupsEvent extends CairngormEvent
	{
		/**
		 *  This property contain new adding sub groups or editing item of
		 *  sub group.
		 */
		public var subGroups:Array = [];
		/**
		 *  This property contain index (position in the list) where needs
		 *  to add new sub group or edited item of sub group.
		 */
		public var subGroupIndex:int;
		/**
		 *  This property contain id of main group for which will be added
		 *  new sub groups.
		 */
		public var groupId:int;
		/**
		 *  This property contain index ot the item in owner's group.
		 */
		public var groupIndex:int;
		/**
		 *  This property contain call back function for executing some functions
		 *  if user get result's handler after call remote function from the server.
		 */
		public var callBack:Function;
		/**
		 *  AddHotelSubGroupsEvent. Constructor.
		 */
		public function AddHotelSubGroupsEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
		}
	}
}