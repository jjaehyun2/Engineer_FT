package services.business.common
{
	import services.cairngorm.BaseDelegate;
	import services.events.common.GetMarketCodesEvent;
	import framework.module.CommonModule;
	import services.Services;
	
	import mx.rpc.IResponder;
	import mx.rpc.events.ResultEvent;
	
	public class GetMarketCodesDelegate extends BaseDelegate
	{
		public function GetMarketCodesDelegate(responder:IResponder)
		{
			super(responder);
		}
		
		public function getMarketCodes(evt:GetMarketCodesEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_COMMON).getOperation("getMarketCodeList");
			
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(CommonModule.userOptions);
		}
	}
}