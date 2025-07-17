package services.business.backend
{
	import services.cairngorm.BaseDelegate;
	import services.events.hotels.SetHotelRoomStatusEvent;
	import framework.module.CommonModule;
	import services.Services;
	
	import mx.rpc.IResponder;
	import mx.rpc.events.ResultEvent;
	
	/**
	* The SetHotelRoomStatusDelegate class is 
	*
	* @author Anton Kirzyk / Ramada
	*
	* @version $Revision 1.0 $ $Date: 2009-07-18 11:52:03 +0300 (Сб, 18 июл 2009) $
	*
	*/
	public class SetHotelRoomStatusDelegate extends BaseDelegate
	{
		public function SetHotelRoomStatusDelegate(responder:IResponder)
		{
			super(responder);
		}
		
		public function setHotelRoomStatus(event:SetHotelRoomStatusEvent):void
		{
			service.getRemoteObject(Services.SERVICE_HOUSEKEEPING).getOperation("setStatus").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_HOUSEKEEPING).getOperation("setStatus").send(CommonModule.userOptions,event.iRoomId,event.oHotelRoomStatus,event.sDate);
		}
		
	}
}