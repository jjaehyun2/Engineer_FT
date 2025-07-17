package services.events.backend
{
	import com.adobe.cairngorm.control.CairngormEvent;
	/**
	* The LoginInHotelEvent class is 
	*
	* @author  Anton Kirzyk / Ramada
	*
	* @version $Revision 1.0 $ $Date: 2009-07-18 11:52:03 +0300 (Сб, 18 июл 2009) $
	*
	*/
	public class LoginInHotelEvent extends CairngormEvent
	{		
		public var iHotelId:int;
		public var callBack:Function;
		
		public function LoginInHotelEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
		}
		
	}
}