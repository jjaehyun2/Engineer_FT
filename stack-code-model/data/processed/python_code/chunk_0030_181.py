package services.events.backend
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.vo.backend.LocationVO;

	public class AddLocationEvent extends CairngormEvent
	{
		/**
		 *  This property contain new adding location.
		 *  
		 *  @see services.vo.backend.LocationVO
		 */
		public var location:LocationVO;
		/**
		 *  This property contain call back function for executing some functions
		 *  if user get result's handler after call remote function from the server.
		 */
		public var callBack:Function;
		
		public function AddLocationEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
		}
		
	}
}