package services.business.reservation
{
	import services.cairngorm.BaseDelegate;
	import services.events.reservation.GetPackagesRatesForReservationEvent;
	import framework.module.CommonModule;
	import services.Services;
	
	import mx.rpc.IResponder;
	import mx.rpc.events.ResultEvent;
	
	public class GetPackagesRatesForReservationDelegate extends BaseDelegate
	{
		public function GetPackagesRatesForReservationDelegate(_responder:IResponder)
		{
			super(_responder);
		}
		
		public function getPackagesRatesForReservation(event:GetPackagesRatesForReservationEvent):void {
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("getPackagesForRsv").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("getPackagesForRsv").send(CommonModule.userOptions,event.packageRequest);
		}

	}
}