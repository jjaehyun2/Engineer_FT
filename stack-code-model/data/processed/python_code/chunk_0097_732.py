package services.events.profiles.individual
{
	import com.adobe.cairngorm.control.CairngormEvent;
	/**
	 *  The event to get count of profiles by hotel.
	 *  
	 *  @author Artemyev Dmitriy
	 *  @date 08.06.2009
	 *  
	 *  @see com.adobe.cairngorm.control.CairngormEvent
	 */
	public class GetProfilesCounterEvent extends CairngormEvent
	{
		/**
		 *  This property contain id of hotel.
		 */
		public var hotelId:Number;
		/**
		 *  This property contain call back function for
		 *  executing some functions if user get result's
		 *  handler after call remote function from the
		 *  server.
		 */
		public var callBack:Function;
		/**
		 *  GetCityEvent. Constructor.
		 */
		public function GetProfilesCounterEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
		}
	}
}