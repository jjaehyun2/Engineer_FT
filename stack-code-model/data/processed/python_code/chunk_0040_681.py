package services.business.frontend
{
	import services.cairngorm.BaseDelegate;
	import services.events.frontend.GetCheckInDataEvent;
	import framework.module.CommonModule;
	import services.Services;
	import services.vo.GlobalSettings;
	
	import mx.controls.DateField;
	import mx.rpc.IResponder;
	import mx.rpc.events.ResultEvent;
	
	public class GetCheckInDataDelegate extends BaseDelegate
	{		
		public function GetCheckInDataDelegate( responder:IResponder )
		{
			super(responder);
		}
		
		public function getCheckInData(evt:GetCheckInDataEvent):void
		{
			var str:String = DateField.dateToString( new Date(evt.checkDate), GlobalSettings.DATE_SERVER_FORMAT );
			//var str:String ="2009-08-19";
			
			service.getRemoteObject(Services.SERVICE_CHECK_IN).getOperation("executeIndex").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_CHECK_IN).getOperation("executeIndex").send(CommonModule.userOptions, 
																								     model.hotelsModule.hotelTotalInfo.iHotelId, 
																							   		 str,
																								     evt.checkStageId,
																								     evt.checkYieldMode);
		}
	}
}