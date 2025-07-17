package services.business.common
{
	import services.cairngorm.BaseDelegate;
	import services.events.common.GetVipTotalListEvent;
	import services.Services;
	import services.vo.GlobalStorage;
	
	import mx.rpc.IResponder;
	import mx.rpc.events.ResultEvent;
	
	public class GetVipTotalListDelegate extends BaseDelegate
	{
		/**
		 *  GetVipTotalListDelegate. Constructor.
		 *  
		 *  @param _responder:IResponder - contact provider for any service
		 */
		public function GetVipTotalListDelegate(_responder:IResponder)
		{
			super(_responder);
		}
		/**
		 *  Remote call for get list of total VIPs.
		 *  
		 *  @param evt:GetVipTotalListEvent
		 */
		public function getVIPTotalList(evt:GetVipTotalListEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_PROFILE).getOperation("GetVipTotalList");
			
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(GlobalStorage.userOptions);
		}
	}
}