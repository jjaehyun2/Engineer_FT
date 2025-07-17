package services.business.frontend
{
	import services.cairngorm.BaseDelegate;
	import services.events.frontend.GetCityEvent;
	import framework.module.CommonModule;
	import services.Services;
	
	import mx.rpc.IResponder;
	import mx.rpc.events.ResultEvent;
	/**
	 *  Delegate to get list of cities.
	 *  
	 *  @author Artemyev Dmitriy
	 *  @date 08.06.2009
	 */
	public class GetCityDelegate extends BaseDelegate
	{
		/**
		 *  GetCityDelegate. Constructor.
		 *  
		 *  @param _responder:IResponder - contact provider for any service
		 */
		public function GetCityDelegate(_responder:IResponder)
		{
			super(_responder);
		}
		/**
		 *  Remote call for get list of all countries.
		 *  
		 *  @param evt:GetCountryEvent
		 */
		public function getCities(evt:GetCityEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_HELPER).getOperation("GetCitiesList");
			
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(CommonModule.userOptions, evt.regionId);
		}
	}
}