package services.business.frontend
{
	import services.cairngorm.BaseDelegate;
	import services.events.frontend.GetAddressByZipEvent;
	import framework.module.CommonModule;
	import services.Services;
	
	import mx.rpc.IResponder;
	import mx.rpc.events.ResultEvent;
	/**
	 *  Delegate to find addreses by zip code.
	 *  
	 *  @author Artemyev Dmitriy
	 *  @date 05.06.2009
	 */
	public class GetAddressByZipDelegate extends BaseDelegate
	{
		/**
		 *  GetAddressByZipDelegate. Constructor.
		 *  
		 *  @param responder:IResponder - contact provider for any service
		 */
		public function GetAddressByZipDelegate(responder:IResponder)
		{
			super(responder);
		}
		/**
		 *  Remote call for find all addreses by neccessary zip code.
		 *  
		 *  @param evt:GetAddressByZipEvent
		 */
		public function findAddressByZip(evt:GetAddressByZipEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_HELPER).getOperation("FindAddressByZip");
			
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(CommonModule.userOptions, evt.zipCode);
		}
	}
}