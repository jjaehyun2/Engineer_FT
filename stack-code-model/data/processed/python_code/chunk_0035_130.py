package services.business.security
{
	import services.cairngorm.BaseDelegate;
	import services.events.security.AddSystemUserEvent;
	import services.events.security.DeleteRoleEvent;
	import services.events.security.DeleteUserHotelRoleEvent;
	import services.events.security.GetUserListInHotelEvent;
	import services.events.security.SaveRoleEvent;
	import services.events.security.SetStatusSystemUserEvent;
	import services.events.security.SetUserHotelRoleEvent;
	import framework.module.CommonModule;
	import services.Services;
	import services.vo.GlobalStorage;
	
	import mx.rpc.IResponder;
	import mx.rpc.events.ResultEvent;


	/**
	* The SecurityDelegate class is 
	*
	* @author Anton Kirzyk / Ramada
	*
	* @version $Revision 1.0 $ $Date: 2009-08-31 11:52:03 +0300 (Сб, 18 июл 2009) $
	*
	*/
	public class SecurityDelegate extends BaseDelegate
	{
		public function SecurityDelegate(responder:IResponder)
		{
			super(responder);
		}
		
		public function getUserList():void
		{
			service.getRemoteObject(Services.SERVICE_LOGIN).getOperation("getUserList").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_LOGIN).getOperation("getUserList").send(CommonModule.userOptions);
		}	
			
		public function getUserListInHotel(event:GetUserListInHotelEvent):void
		{
			service.getRemoteObject(Services.SERVICE_LOGIN).getOperation("getUserListInHotel").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_LOGIN).getOperation("getUserListInHotel").send(CommonModule.userOptions,event.iHotelID);
		}	

		

		public function addSystemUser(event:AddSystemUserEvent):void
		{
			service.getRemoteObject(Services.SERVICE_LOGIN).getOperation("addSystemUser").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_LOGIN).getOperation("addSystemUser").send(CommonModule.userOptions, event.sLogin,event.iRoleId, event.iUserId);
		}
		
		public function setUserHotelRole(event:SetUserHotelRoleEvent):void
		{
			service.getRemoteObject(Services.SERVICE_LOGIN).getOperation("setUserHotelRole").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_LOGIN).getOperation("setUserHotelRole").send(CommonModule.userOptions,event.iUserId, event.iHotelId, event.iRoleId);

		}	
		
		public function setStatusSystemUser(event:SetStatusSystemUserEvent):void
		{
			service.getRemoteObject(Services.SERVICE_LOGIN).getOperation("setStatusSystemUser").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_LOGIN).getOperation("setStatusSystemUser").send(CommonModule.userOptions,event.iUserId, event.bStatus);

		}			
		// ROLES
		public function getRoles():void
		{
			service.getRemoteObject(Services.SERVICE_LOGIN).getOperation("getRoleList").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_LOGIN).getOperation("getRoleList").send(CommonModule.userOptions);
		}

		public function getSystemRoleList():void
		{
			service.getRemoteObject(Services.SERVICE_LOGIN).getOperation("getSystemRoleList").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_LOGIN).getOperation("getSystemRoleList").send(CommonModule.userOptions);
		}		
		
		public function deleteUserHotelRole(event:DeleteUserHotelRoleEvent):void
		{
			service.getRemoteObject(Services.SERVICE_LOGIN).getOperation("deleteUserHotelRole").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_LOGIN).getOperation("deleteUserHotelRole").send(CommonModule.userOptions,event.iUserId, event.iHotelId, event.iRoleId);

		}	
		
		public function saveRole(event:SaveRoleEvent):void
		{
			service.getRemoteObject(Services.SERVICE_LOGIN).getOperation("saveRole").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_LOGIN).getOperation("saveRole").send(CommonModule.userOptions, event.role);
		}
		
								
		public function deleteRole(event:DeleteRoleEvent):void
		{
			service.getRemoteObject(Services.SERVICE_LOGIN).getOperation("deleteRole").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_LOGIN).getOperation("deleteRole").send(CommonModule.userOptions, event.role);
		}
					
	}
}