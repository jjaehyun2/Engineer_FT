package services.events.security
{
	import services.controller.AppController;
	import services.cairngorm.BaseEvent;
	import services.vo.frontend.RoleVO;

	public class DeleteRoleEvent extends BaseEvent
	{
		public static const NAME:String = "securityDeleteRoleEvent";
		public var role:RoleVO; 
		
		public function DeleteRoleEvent(bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(NAME, bubbles, cancelable);
		}
		
	}
}