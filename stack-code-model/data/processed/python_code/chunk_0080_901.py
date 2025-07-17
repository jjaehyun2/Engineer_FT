package com.macys.marketing.sema.business
{
	import mx.rpc.soap.WebService;
	import com.macys.marketing.sema.model.SEMAModelLocator;

	public class SEMAWebService extends WebService
	{
		
		private var model : SEMAModelLocator = SEMAModelLocator.getInstance();

		public function SEMAWebService(serviceName:String)
		{
			super();
			
			this.wsdl = model.serviceRegistry[serviceName] + "?wsdl";
			this.endpointURI = model.serviceRegistry[serviceName];
			this.addSimpleHeader("userName", "http://schemas.macys.com/definitions/ad/v1", "userName", model.semaUser.userName);
			
			this.requestTimeout = 30; // seconds
 
	        this.loadWSDL();
			
		}
		
	}
}