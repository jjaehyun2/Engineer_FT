package services.business.backend
{
	import services.cairngorm.BaseDelegate;
	import services.events.backend.GetRoomListEvent;
	import framework.module.CommonModule;
	import services.Services;
	
	import mx.rpc.IResponder;
	import mx.rpc.events.ResultEvent;
	
	/**
	* The GetRoomListDelegate class is 
	*
	* @author Anton Kirzyk / Ramada
	*
	* @version $Revision 1.0 $ $Date: 2009-07-18 11:52:03 +0300 (Сб, 18 июл 2009) $
	*
	*/
	public class GetRoomListDelegate extends BaseDelegate
	{
		public function GetRoomListDelegate(responder:IResponder)
		{
			super(responder);
		}
		
		public function getRoomList(event:GetRoomListEvent):void
		{
			service.getRemoteObject(Services.SERVICE_HOUSEKEEPING).getOperation("getRoomList").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_HOUSEKEEPING).getOperation("getRoomList").send(CommonModule.userOptions,event.hotelStageId,event.sDate);

		}
		
	}
}