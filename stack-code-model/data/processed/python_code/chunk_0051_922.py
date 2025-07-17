package services.business.backend
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.cairngorm.BaseDelegate;
	import framework.module.CommonModule;
	import services.Services;
	
	import mx.rpc.IResponder;
	import mx.rpc.events.ResultEvent;
	
	/**
	* The GetStatusListDelegate class is 
	*
	* @author Anton Kirzyk / Ramada
	*
	* @version $Revision 1.0 $ $Date: 2009-07-18 11:52:03 +0300 (Сб, 18 июл 2009) $
	*
	*/
	public class GetStatusListDelegate extends BaseDelegate
	{
		public function GetStatusListDelegate(responder:IResponder)
		{
			super(responder);
		}
		
		public function getStatusList(event:CairngormEvent):void
		{
			service.getRemoteObject(Services.SERVICE_HOUSEKEEPING).getOperation("getStatusList").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_HOUSEKEEPING).getOperation("getStatusList").send(CommonModule.userOptions);

		}
		
	}
}