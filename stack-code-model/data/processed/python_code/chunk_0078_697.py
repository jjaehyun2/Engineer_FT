package services.events.security
{
	import services.cairngorm.BaseEvent;
	
	/**
	* The SetUserHotelRoleEvent class is 
	*
	* @author  Anton Kirzyk / Ramada
	*
	* @version $Revision 1.0 $ $Date: 2009-07-18 11:52:03 +0300 (Сб, 18 июл 2009) $
	*
	*/
	public class SetUserHotelRoleEvent extends BaseEvent
	{
		public static const NAME:String = "securitySetUserHotelRoleEvent";
		
		public var iUserId:int;
		public var iHotelId:int;
		public var iRoleId:int;
		public var isAddUser:Boolean;
		
		public function SetUserHotelRoleEvent(bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(NAME, bubbles, cancelable);
		}
		
	}
}