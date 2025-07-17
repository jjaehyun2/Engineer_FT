package services.business.backend
{
	import services.cairngorm.BaseDelegate;
	import services.events.backend.GetPageOfStartEvent;
	import framework.module.CommonModule;
	import services.Services;
	
	import mx.rpc.IResponder;
	import mx.rpc.events.ResultEvent;

	public class GetPageOfStartDelegate extends BaseDelegate
	{
		
		public function GetPageOfStartDelegate(responder:IResponder)
		{
			super(responder);
		}
		
		public function GetPageOfStart(evt:GetPageOfStartEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_COMMON).getOperation("getCommonDictionaries");
			
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(CommonModule.userOptions);
		}
	}
}