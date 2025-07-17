package services.command.security
{
	import com.adobe.cairngorm.commands.ICommand;
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.security.SecurityDelegate;
	import services.events.security.SetUserHotelRoleEvent;
	import framework.model.AppModelLocator;
	import services.vo.frontend.RoleVO;
	import services.vo.frontend.UserProfileVO;
	import services.vo.frontend.UserVO;
	
	import mx.controls.Alert;
	import mx.rpc.IResponder;

	/**
	* The SetUserHotelRoleCommand class is 
	*
	* @author Anton Kirzyk / Ramada
	*
	* @version $Revision 1.0 $ $Date: 2009-07-18 11:52:03 +0300 (Сб, 18 июл 2009) $
	*
	*/
	public class SetUserHotelRoleCommand implements ICommand, IResponder
	{
		private var model:AppModelLocator = AppModelLocator.getInstance();

		private var userID:int;
		private var user:UserProfileVO;
		private var userRole:RoleVO;
		private var isAddUser:Boolean;
		
		public function execute(event:CairngormEvent):void
		{
			var delegate:SecurityDelegate = new SecurityDelegate( this );
			userID = (event as SetUserHotelRoleEvent).iUserId;
			isAddUser = (event as SetUserHotelRoleEvent).isAddUser;	
			delegate.setUserHotelRole(event as SetUserHotelRoleEvent);
		}
		
		public function result(data:Object):void
		{
			if(isAddUser)
			{
				model.securityModule.userListInHotel.addItem(data as UserVO);				
				model.securityModule.userListInHotel.refresh();
				
			}
			else
			{			
				for each(var user:UserVO in model.securityModule.userListInHotel)
				{
					if(user.oUser.lId == userID)
					{
						user.oHotelRole = (data as UserVO).oHotelRole;
						break;
					}
				}
			}
			model.appEnabled--;	
		}
		
		public function fault(info:Object):void
		{			
			Alert.show("Error");			 
			model.appEnabled--;
		}
		
	}
}