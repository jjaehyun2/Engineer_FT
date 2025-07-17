package services.business.reports
{
	import services.cairngorm.BaseDelegate;
	import services.events.reports.GetItemTreeEvent;
	import services.events.reports.GetReportEvent;
	import framework.module.CommonModule;
	import services.Services;
	
	import mx.rpc.IResponder;
	import mx.rpc.events.ResultEvent;
	
	public class GetReportDelegate extends BaseDelegate
	{
		public function GetReportDelegate(responder:IResponder )
		{
			super(responder);
		}
		
		public function getArrivalReport(evt:GetReportEvent):void
		{
			service.getRemoteObject(Services.SERVICE_REPORTS).getOperation("executeCreate").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_REPORTS).getOperation("executeCreate").send(CommonModule.userOptions, evt.report);
		}
		
		public function getItemTree(evt:GetItemTreeEvent):void
		{
			service.getRemoteObject(Services.SERVICE_COMMON).getOperation("getItemTree").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_COMMON).getOperation("getItemTree").send(CommonModule.userOptions, model.hotelsModule.hotelTotalInfo.iHotelId);
		}
		

	}
}