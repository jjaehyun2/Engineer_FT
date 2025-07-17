package services.business.frontend
{
	import com.adobe.cairngorm.business.ServiceLocator;
	
	import services.events.frontend.AddIndividualProfileEvent;
	import services.Services;
	import services.vo.GlobalSettings;
	import services.vo.GlobalStorage;
	
	import mx.rpc.IResponder;
	import mx.rpc.events.ResultEvent;
	
	public class AddIndividualProfileDelegate
	{
		private var responder:IResponder;
		private var service:ServiceLocator = ServiceLocator.getInstance();
		
		public function AddIndividualProfileDelegate( _responder:IResponder )
		{
			responder = _responder;
		}
		 
		public function addProfiles(evt:AddIndividualProfileEvent):void
		{			
			service.getRemoteObject(Services.SERVICE_PERSONAL).getOperation("SaveGuestsProfiles").addEventListener(ResultEvent.RESULT, handleSaveProfilesResult);
			service.getRemoteObject(Services.SERVICE_PERSONAL).getOperation("SaveGuestsProfiles").send(GlobalStorage.userOptions, evt.profileList);
		}
		
		private function handleSaveProfilesResult(evt:ResultEvent):void
		{
			if(evt.result == null || evt.result == false) this.responder.fault({});
			else this.responder.result(evt.result);
			
			service.getRemoteObject(Services.SERVICE_PERSONAL).getOperation("SaveGuestsProfiles").removeEventListener(ResultEvent.RESULT, handleSaveProfilesResult);
		}

	}
}