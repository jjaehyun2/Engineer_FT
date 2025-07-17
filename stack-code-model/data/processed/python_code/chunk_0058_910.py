package services.business.rates.bar
{
	import services.cairngorm.BaseDelegate;
	import services.events.rates.bar.GetBARsByDateEvent;
	import services.events.rates.bar.GetBarItemsInfoEvent;
	import services.events.rates.bar.GetHotelBarPriceEvent;
	import services.events.rates.bar.SaveBarItemsDataEvent;
	import framework.module.CommonModule;
	import services.Services;
	
	import mx.rpc.IResponder;
	import mx.rpc.events.ResultEvent;

	/**
	* The BARDelegate class is
	*
	* @author Viktor Potapov / Ramada
	*
	* @version $Revision 2.0 $ $Date: 2009-10-26 15:15:19 +0200 (Mon, 26 Oct 2009) $
	*
	*/
	public class BARDelegate extends BaseDelegate
	{
		public function BARDelegate(responder:IResponder)
		{
			super(responder);
		}


		public function getBarItemsInfo(evt:GetBarItemsInfoEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_HOTEL_BAR).getOperation("getBARsByMonth");
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(CommonModule.userOptions, model.ratesModule.barModule.barGetter);
		}

		public function saveBarItemsData(evt:SaveBarItemsDataEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_HOTEL_BAR).getOperation("saveHotelBARs")
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(CommonModule.userOptions, evt.barDate, evt.hotelDateInterval);
		}

		public function getHotelBarPrice(event:GetHotelBarPriceEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_HOTEL_BAR).getOperation("getHotelBarPrice");
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(CommonModule.userOptions, event.iHotelId, event.iRoomQualityId, event.sStartDate, event.sEndDate);
		}
		
		public function getBARsByDate(event:GetBARsByDateEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_HOTEL_BAR).getOperation("getBARsByDate");
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(CommonModule.userOptions, event.iHotelId, event.sStartDate);
		}

	}
}