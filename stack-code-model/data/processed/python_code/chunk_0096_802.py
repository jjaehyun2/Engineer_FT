package services.events.security
{
	import services.cairngorm.BaseEvent;
	import services.vo.frontend.RoleVO;

	public class SaveRoleEvent extends BaseEvent
	{
		public static const NAME:String = "securitySaveRoleEvent";
		
		public var role:RoleVO; 
		
		public function SaveRoleEvent(bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(NAME, bubbles, cancelable);
		}
	}
}