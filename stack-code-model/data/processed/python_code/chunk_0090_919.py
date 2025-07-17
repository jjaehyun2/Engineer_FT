package com.macys.marketing.sema.model
{
	import mx.collections.ArrayCollection;
	import mx.rpc.events.FaultEvent;
	import mx.rpc.events.ResultEvent;
	import mx.rpc.http.HTTPService;
	import mx.utils.ObjectProxy;
	
	public class UserRegistry
	{
		
		private var model : SEMAModelLocator;
		private static const userRegistryXML : String = "config/userRegistry.xml";
			
		
		
		
		public function UserRegistry(model:SEMAModelLocator) {
			if (model == null) {
				throw new Error("Model cannot be null");
			}
			this.model = model;
		}//end UserRegistry()
		 
		
		public function initializeUserRegistry():void {
			var hostnameService : HTTPService = new HTTPService();
			hostnameService.url = UserRegistry.userRegistryXML;
			hostnameService.useProxy = false;
			hostnameService.addEventListener(ResultEvent.RESULT, handleResult);
			hostnameService.addEventListener(FaultEvent.FAULT, handleFault);
			hostnameService.send();
		}//end initializeUserRegistry()
		
		
		private function handleResult(event : ResultEvent):void {	
			var configRoot : ObjectProxy = event.result as ObjectProxy;
			
			if (configRoot.UserRegistry.Users.User is ArrayCollection){
				var users : ArrayCollection = configRoot.UserRegistry.Users.User;
				for each (var i:Object in users) {
					var user : SemaUser = new SemaUser(i.UserName);
					user.firstName = i.FirstName;
					user.lastName = i.LastName;
					user.password = i.Password;
					user.role = i.Role;
					
					model.userRegistry[user.userName] = user;
				}
			}//end if
			
			//.... is there a more clever way to do this?
			model.loginRequired = configRoot.UserRegistry.LoginFunctionality.enabled;
			if (configRoot.UserRegistry.LoginFunctionality.enabled) {
				model.enableAppOrLogin = 0;
			} else {
				model.enableAppOrLogin = 1;
			};
		    
		}//end handleResult()
		
	
		private function handleFault(event: FaultEvent) :void {
			trace("Problem occured initializing user registry",event);
		}//end handleFault()
		
		
	}
}