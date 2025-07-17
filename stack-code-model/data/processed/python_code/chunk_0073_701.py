package services.events.security
{
	import services.cairngorm.BaseEvent;

	public class GetRolesEvent extends BaseEvent
	{
		public static const NAME:String = "securityGetRolesEvent";
		
		
		public function GetRolesEvent(bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(NAME, bubbles, cancelable);
		}
		
	}
}