/**
 * CampaignServiceService.as
 * This file was auto-generated from WSDL by the Apache Axis2 generator modified by Adobe
 * Any change made to this file will be overwritten when the code is re-generated.
 */
 /**
  * Usage example: to use this service from within your Flex application you have two choices:
  * Use it via Actionscript only
  * Use it via MXML tags
  * Actionscript sample code:
  * Step 1: create an instance of the service; pass it the LCDS destination string if any
  * var myService:CampaignService= new CampaignService();
  * Step 2: for the desired operation add a result handler (a function that you have already defined previously)  
  * myService.addgetCampaignListEventListener(myResultHandlingFunction);
  * Step 3: Call the operation as a method on the service. Pass the right values as arguments:
  * myService.getCampaignList(myCampaignIds,mygetCampaignList);
  *
  * MXML sample code:
  * First you need to map the package where the files were generated to a namespace, usually on the <mx:Application> tag, 
  * like this: xmlns:srv="com.macys.marketing.sema.*"
  * Define the service and within its tags set the request wrapper for the desired operation
  * <srv:CampaignService id="myService">
  *   <srv:getCampaignList_request_var>
  *		<srv:GetCampaignList_request CampaignIds=myValue,getCampaignList=myValue/>
  *   </srv:getCampaignList_request_var>
  * </srv:CampaignService>
  * Then call the operation for which you have set the request wrapper value above, like this:
  * <mx:Button id="myButton" label="Call operation" click="myService.getCampaignList_send()" />
  */
 package com.macys.marketing.sema{
	import mx.rpc.AsyncToken;
	import flash.events.EventDispatcher;
	import mx.rpc.events.ResultEvent;
	import mx.rpc.events.FaultEvent;
	import flash.utils.ByteArray;
	import mx.rpc.soap.types.*;

    /**
     * Dispatches when a call to the operation getCampaignList completes with success
     * and returns some data
     * @eventType GetCampaignListResultEvent
     */
    [Event(name="GetCampaignList_result", type="com.macys.marketing.sema.GetCampaignListResultEvent")]
    
    /**
     * Dispatches when a call to the operation putCampaigns completes with success
     * and returns some data
     * @eventType PutCampaignsResultEvent
     */
    [Event(name="PutCampaigns_result", type="com.macys.marketing.sema.PutCampaignsResultEvent")]
    
    /**
     * Dispatches when a call to the operation getAllCampaigns completes with success
     * and returns some data
     * @eventType GetAllCampaignsResultEvent
     */
    [Event(name="GetAllCampaigns_result", type="com.macys.marketing.sema.GetAllCampaignsResultEvent")]
    
	/**
	 * Dispatches when the operation that has been called fails. The fault event is common for all operations
	 * of the WSDL
	 * @eventType mx.rpc.events.FaultEvent
	 */
    [Event(name="fault", type="mx.rpc.events.FaultEvent")]

	public class CampaignService extends EventDispatcher implements ICampaignService
	{
    	private var _baseService:BaseCampaignService;
        
        /**
         * Constructor for the facade; sets the destination and create a baseService instance
         * @param The LCDS destination (if any) associated with the imported WSDL
         */  
        public function CampaignService(destination:String=null,rootURL:String=null)
        {
        	_baseService = new BaseCampaignService(destination,rootURL);
        }
        
		//stub functions for the getCampaignList operation
          

        /**
         * @see ICampaignService#getCampaignList()
         */
        public function getCampaignList(getCampaignList:GetCampaignList):AsyncToken
        {
         	var _internal_token:AsyncToken = _baseService.getCampaignList(getCampaignList);
            _internal_token.addEventListener("result",_getCampaignList_populate_results);
            _internal_token.addEventListener("fault",throwFault); 
            return _internal_token;
		}
        /**
		 * @see ICampaignService#getCampaignList_send()
		 */    
        public function getCampaignList_send():AsyncToken
        {
        	return getCampaignList(_getCampaignList_request.getCampaignList);
        }
              
		/**
		 * Internal representation of the request wrapper for the operation
		 * @private
		 */
		private var _getCampaignList_request:GetCampaignList_request;
		/**
		 * @see ICampaignService#getCampaignList_request_var
		 */
		[Bindable]
		public function get getCampaignList_request_var():GetCampaignList_request
		{
			return _getCampaignList_request;
		}
		
		/**
		 * @private
		 */
		public function set getCampaignList_request_var(request:GetCampaignList_request):void
		{
			_getCampaignList_request = request;
		}
		
	  		/**
		 * Internal variable to store the operation's lastResult
		 * @private
		 */
        private var _getCampaignList_lastResult:GetCampaignListResponse;
		[Bindable]
		/**
		 * @see ICampaignService#getCampaignList_lastResult
		 */	  
		public function get getCampaignList_lastResult():GetCampaignListResponse
		{
			return _getCampaignList_lastResult;
		}
		/**
		 * @private
		 */
		public function set getCampaignList_lastResult(lastResult:GetCampaignListResponse):void
		{
			_getCampaignList_lastResult = lastResult;
		}
		
		/**
		 * @see ICampaignService#addgetCampaignList()
		 */
		public function addgetCampaignListEventListener(listener:Function):void
		{
			addEventListener(GetCampaignListResultEvent.GetCampaignList_RESULT,listener);
		}
			
		/**
		 * @private
		 */
        private function _getCampaignList_populate_results(event:ResultEvent):void
        {
        var e:GetCampaignListResultEvent = new GetCampaignListResultEvent();
		            e.result = event.result as GetCampaignListResponse;
		                       e.headers = event.headers;
		             getCampaignList_lastResult = e.result;
		             dispatchEvent(e);
	        		
		}
		
		//stub functions for the putCampaigns operation
          

        /**
         * @see ICampaignService#putCampaigns()
         */
        public function putCampaigns(putCampaigns:PutCampaigns):AsyncToken
        {
         	var _internal_token:AsyncToken = _baseService.putCampaigns(_putCampaigns_header.userName17,putCampaigns);
            _internal_token.addEventListener("result",_putCampaigns_populate_results);
            _internal_token.addEventListener("fault",throwFault); 
            return _internal_token;
		}
        /**
		 * @see ICampaignService#putCampaigns_send()
		 */    
        public function putCampaigns_send():AsyncToken
        {
        	return putCampaigns(_putCampaigns_request.putCampaigns);
        }
              
		/**
		 * Internal representation of the request wrapper for the operation
		 * @private
		 */
		private var _putCampaigns_request:PutCampaigns_request;
		/**
		 * @see ICampaignService#putCampaigns_request_var
		 */
		[Bindable]
		public function get putCampaigns_request_var():PutCampaigns_request
		{
			return _putCampaigns_request;
		}
		
		/**
		 * @private
		 */
		public function set putCampaigns_request_var(request:PutCampaigns_request):void
		{
			_putCampaigns_request = request;
		}
					  
		/**
		 * Internal representation of the header wrapper
		 * @private
		 */
		private var _putCampaigns_header:Object;
		[Bindable]
		/**
		 * @see ICampaignService#putCampaigns_header
		 */
		public function get putCampaigns_header():Object
		{
			return _putCampaigns_header;
		}
		public function set putCampaigns_header(header:Object):void
		{
			_putCampaigns_header = header;
		}
		/**
		 * Add values for the various parts of the header
         * @param 
         userName17
		 */ 
		public function addputCampaigns_header(userName17:com.macys.marketing.sema.UserName):void
		{
			_putCampaigns_header = new Object;
            _putCampaigns_header.userName17 = userName17;
              		
		}
	  		/**
		 * Internal variable to store the operation's lastResult
		 * @private
		 */
        private var _putCampaigns_lastResult:PutCampaignsResponse;
		[Bindable]
		/**
		 * @see ICampaignService#putCampaigns_lastResult
		 */	  
		public function get putCampaigns_lastResult():PutCampaignsResponse
		{
			return _putCampaigns_lastResult;
		}
		/**
		 * @private
		 */
		public function set putCampaigns_lastResult(lastResult:PutCampaignsResponse):void
		{
			_putCampaigns_lastResult = lastResult;
		}
		
		/**
		 * @see ICampaignService#addputCampaigns()
		 */
		public function addputCampaignsEventListener(listener:Function):void
		{
			addEventListener(PutCampaignsResultEvent.PutCampaigns_RESULT,listener);
		}
			
		/**
		 * @private
		 */
        private function _putCampaigns_populate_results(event:ResultEvent):void
        {
        var e:PutCampaignsResultEvent = new PutCampaignsResultEvent();
		            e.result = event.result as PutCampaignsResponse;
		                       e.headers = event.headers;
		             putCampaigns_lastResult = e.result;
		             dispatchEvent(e);
	        		
		}
		
		//stub functions for the getAllCampaigns operation
          

        /**
         * @see ICampaignService#getAllCampaigns()
         */
        public function getAllCampaigns(getAllCampaigns:GetAllCampaigns):AsyncToken
        {
         	var _internal_token:AsyncToken = _baseService.getAllCampaigns(getAllCampaigns);
            _internal_token.addEventListener("result",_getAllCampaigns_populate_results);
            _internal_token.addEventListener("fault",throwFault); 
            return _internal_token;
		}
        /**
		 * @see ICampaignService#getAllCampaigns_send()
		 */    
        public function getAllCampaigns_send():AsyncToken
        {
        	return getAllCampaigns(_getAllCampaigns_request.getAllCampaigns);
        }
              
		/**
		 * Internal representation of the request wrapper for the operation
		 * @private
		 */
		private var _getAllCampaigns_request:GetAllCampaigns_request;
		/**
		 * @see ICampaignService#getAllCampaigns_request_var
		 */
		[Bindable]
		public function get getAllCampaigns_request_var():GetAllCampaigns_request
		{
			return _getAllCampaigns_request;
		}
		
		/**
		 * @private
		 */
		public function set getAllCampaigns_request_var(request:GetAllCampaigns_request):void
		{
			_getAllCampaigns_request = request;
		}
		
	  		/**
		 * Internal variable to store the operation's lastResult
		 * @private
		 */
        private var _getAllCampaigns_lastResult:GetAllCampaignsResponse;
		[Bindable]
		/**
		 * @see ICampaignService#getAllCampaigns_lastResult
		 */	  
		public function get getAllCampaigns_lastResult():GetAllCampaignsResponse
		{
			return _getAllCampaigns_lastResult;
		}
		/**
		 * @private
		 */
		public function set getAllCampaigns_lastResult(lastResult:GetAllCampaignsResponse):void
		{
			_getAllCampaigns_lastResult = lastResult;
		}
		
		/**
		 * @see ICampaignService#addgetAllCampaigns()
		 */
		public function addgetAllCampaignsEventListener(listener:Function):void
		{
			addEventListener(GetAllCampaignsResultEvent.GetAllCampaigns_RESULT,listener);
		}
			
		/**
		 * @private
		 */
        private function _getAllCampaigns_populate_results(event:ResultEvent):void
        {
        var e:GetAllCampaignsResultEvent = new GetAllCampaignsResultEvent();
		            e.result = event.result as GetAllCampaignsResponse;
		                       e.headers = event.headers;
		             getAllCampaigns_lastResult = e.result;
		             dispatchEvent(e);
	        		
		}
		
		//service-wide functions
		/**
		 * @see ICampaignService#getWebService()
		 */
		public function getWebService():BaseCampaignService
		{
			return _baseService;
		}
		
		/**
		 * Set the event listener for the fault event which can be triggered by each of the operations defined by the facade
		 */
		public function addCampaignServiceFaultEventListener(listener:Function):void
		{
			addEventListener("fault",listener);
		}
		
		/**
		 * Internal function to re-dispatch the fault event passed on by the base service implementation
		 * @private
		 */
		 
		 private function throwFault(event:FaultEvent):void
		 {
		 	dispatchEvent(event);
		 }
    }
}