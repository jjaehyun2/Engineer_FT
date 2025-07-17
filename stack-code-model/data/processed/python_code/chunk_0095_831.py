package services.business.checkIn
{
	import services.cairngorm.BaseDelegate;
	import services.events.checkIn.SaveCheckInDataEvent;
	import framework.module.CommonModule;
	import services.Services;
	
	import mx.rpc.IResponder;
	import mx.rpc.events.ResultEvent;
	
	public class SaveCheckInDataDelegate extends BaseDelegate
	{		 
		public function SaveCheckInDataDelegate( _responder:IResponder )
		{
			super( _responder);
		}
		 
		public function saveCheckInData(evt:SaveCheckInDataEvent):void
		{
			service. getRemoteObject(Services.SERVICE_CHECK_IN).getOperation("executeCheckIn").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_CHECK_IN).getOperation("executeCheckIn").send(CommonModule.userOptions, 
																									   model.hotelsModule.hotelTotalInfo.iHotelId,																									   
																									   evt.orderId,
																									   evt.roomId,
																									   evt.profileId,
																									   evt.isYieldMode);
		}
		
	}
}