package services.business.cashShift
{
	import services.cairngorm.BaseDelegate;
	import services.events.cashShift.CloseShiftEvent;
	import services.events.cashShift.GetDayShiftListEvent;
	import services.events.cashShift.GetLastOpenShiftEvent;
	import services.events.cashShift.GetShiftPaymentListEvent;
	import services.events.cashShift.OpenNextShiftEvent;
	import services.events.cashShift.ReopenShiftEvent;
	import services.events.cashShift.StartNewBusinessDayEvent;
	import framework.module.CommonModule;
	import services.Services;
	
	import mx.rpc.IResponder;
	import mx.rpc.events.ResultEvent;

	/**
	* The PackageDelegate class is
	*
	* @author Anton Kirzyk / Ramada
	* @update Viktor Potapov / Ramada
	* @version $Revision 1.2 $ $Date: 2009-07-18 11:52:03 +0300 (Сб, 18 июл 2009) $
	*
	*/
	public class CashShiftDelegate extends BaseDelegate
	{
		public function CashShiftDelegate(responder:IResponder)
		{
			super(responder);
		}

		public function getLastOpenShift(event:GetLastOpenShiftEvent):void
		{
			service.getRemoteObject(Services.SERVICE_BUSINESS_DAY).getOperation("getLastOpenShift").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_BUSINESS_DAY).getOperation("getLastOpenShift").send(CommonModule.userOptions,event.hotelId);
		}

		public function closeShift(event:CloseShiftEvent ):void
		{
			service.getRemoteObject(Services.SERVICE_BUSINESS_DAY).getOperation("closeShift").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_BUSINESS_DAY).getOperation("closeShift").send(CommonModule.userOptions,event.hotelId,event.iShiftNumber);
		}

		public function openNextShift(event:OpenNextShiftEvent):void
		{
			service.getRemoteObject(Services.SERVICE_BUSINESS_DAY).getOperation("openNextShift").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_BUSINESS_DAY).getOperation("openNextShift").send(CommonModule.userOptions,event.hotelId);
		}
		
		public function reopenShift(event:ReopenShiftEvent):void
		{
			service.getRemoteObject(Services.SERVICE_BUSINESS_DAY).getOperation("reopenShift").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_BUSINESS_DAY).getOperation("reopenShift").send(CommonModule.userOptions,event.hotelId, event.shiftNumber);
		}
		
		public function getDayShiftList(event:GetDayShiftListEvent):void
		{
			service.getRemoteObject(Services.SERVICE_BUSINESS_DAY).getOperation("getDayShiftList").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_BUSINESS_DAY).getOperation("getDayShiftList").send(CommonModule.userOptions, event.hotelId,event.sDate);
		}
		
		public function getShiftPaymentList(event:GetShiftPaymentListEvent):void
		{
			service.getRemoteObject(Services.SERVICE_BUSINESS_DAY).getOperation("getShiftPaymentList").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_BUSINESS_DAY).getOperation("getShiftPaymentList").send(CommonModule.userOptions, event.hotelId, event.sDate, event.iShiftNumber);
		}
		
		public function startNewBusinessDay(event:StartNewBusinessDayEvent):void
		{
			service.getRemoteObject(Services.SERVICE_BUSINESS_DAY).getOperation("startNewBusinessDay").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_BUSINESS_DAY).getOperation("startNewBusinessDay").send(CommonModule.userOptions, event.hotelId);
		}

	}
}