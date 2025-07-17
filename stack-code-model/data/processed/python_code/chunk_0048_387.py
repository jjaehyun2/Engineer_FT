package services.business.miscellaneous.countries
{
	import services.cairngorm.BaseDelegate;
	import services.events.miscellaneous.countries.AddCountryEvent;
	import services.events.miscellaneous.countries.AddRegionEvent;
	import services.events.miscellaneous.countries.DeleteCountryEvent;
	import services.events.miscellaneous.countries.DeleteRegionEvent;
	import services.events.miscellaneous.countries.GetCountryEvent;
	import services.events.miscellaneous.countries.GetRegionEvent;
	import framework.module.CommonModule;
	import services.Services;
	import services.vo.GlobalStorage;
	
	import mx.rpc.IResponder;
	import mx.rpc.events.ResultEvent;


	/**
	* The CountryDelegate class is
	*
	* @author Viktor Potapov / Ramada
	*
	* @version $Revision 1.0 $ $Date: 2009-10-05 11:28:29 +0300 (Mon, 05 Oct 2009) $
	*
	*/
	public class CountryDelegate extends BaseDelegate
	{
		public static const SAVE_COUNTRY:String = "SaveCountry";
		public static const SAVE_REGION:String = "SaveRegion";
		public static const DELETE_COUNTRY:String = "DeleteCountry";
		public static const DELETE_REGION:String = "DeleteRegion";
		public static const GET_COUNTRIES_LIST:String = "GetCountriesList";
		public static const GET_REGION_LIST:String = "GetRegionsList";

		
		/**
		 *  CountryDelegate. Constructor.
		 *  
		 *  @param responder:IResponder - contact provider for any service.
		 */
		public function CountryDelegate(responder:IResponder)
		{
			super(responder);
		}
		/**
		 *  Remote call to add country.
		 *  
		 *  @param event:AddCountryEvent
		 */
		public function addCountry(event:AddCountryEvent):void
		{
			service.getRemoteObject(Services.SERVICE_HELPER).getOperation(SAVE_COUNTRY).addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_HELPER).getOperation(SAVE_COUNTRY).send(CommonModule.userOptions, event.country);
		}
		/**
		 *  Remote call to add region.
		 *  
		 *  @param event:AddRegionEvent
		 */
		public function addRegion(event:AddRegionEvent):void
		{
			service.getRemoteObject(Services.SERVICE_HELPER).getOperation(SAVE_REGION).addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_HELPER).getOperation(SAVE_REGION).send(CommonModule.userOptions, event.region);
		}
		/**
		 *  Remote call to delete country.
		 *  
		 *  @param event:DeleteCountryEvent
		 */
		public function deleteCountry(event:DeleteCountryEvent):void
		{
			service.getRemoteObject(Services.SERVICE_HELPER).getOperation(DELETE_COUNTRY).addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_HELPER).getOperation(DELETE_COUNTRY).send(CommonModule.userOptions, event.country);
		}
		/**
		 *  Remote call to delete region.
		 *  
		 *  @param event:DeleteRegionEvent
		 */
		public function deleteRegion(event:DeleteRegionEvent):void
		{
			service.getRemoteObject(Services.SERVICE_HELPER).getOperation(DELETE_REGION).addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_HELPER).getOperation(DELETE_REGION).send(CommonModule.userOptions, event.region);
		}
		
		/**
		 *  Remote call to get Country.
		 *  
		 *  @param event:GetCountryEvent
		 */
		public function getCountry(event:GetCountryEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_HELPER).getOperation(GET_COUNTRIES_LIST);			
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(CommonModule.userOptions);
		}
		
		/**
		 *  Remote call to get region.
		 *  
		 *  @param event:GetRegionEvent
		 */
		public function getRegion(event:GetRegionEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_HELPER).getOperation(GET_REGION_LIST);			
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(CommonModule.userOptions, event.countryId);
		}
		
	}
}