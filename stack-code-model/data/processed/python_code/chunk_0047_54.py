/**
 * AdGroupStatsServiceService.as
 * This file was auto-generated from WSDL by the Apache Axis2 generator modified by Adobe
 * Any change made to this file will be overwritten when the code is re-generated.
 */
 /**
  * Usage example: to use this service from within your Flex application you have two choices:
  * Use it via Actionscript only
  * Use it via MXML tags
  * Actionscript sample code:
  * Step 1: create an instance of the service; pass it the LCDS destination string if any
  * var myService:AdGroupStatsService= new AdGroupStatsService();
  * Step 2: for the desired operation add a result handler (a function that you have already defined previously)  
  * myService.addgetAdGroupStatsEventListener(myResultHandlingFunction);
  * Step 3: Call the operation as a method on the service. Pass the right values as arguments:
  * myService.getAdGroupStats(myAdGroupIds,myType,mygetAdGroupStats);
  *
  * MXML sample code:
  * First you need to map the package where the files were generated to a namespace, usually on the <mx:Application> tag, 
  * like this: xmlns:srv="com.macys.marketing.sema.*"
  * Define the service and within its tags set the request wrapper for the desired operation
  * <srv:AdGroupStatsService id="myService">
  *   <srv:getAdGroupStats_request_var>
  *		<srv:GetAdGroupStats_request AdGroupIds=myValue,Type=myValue,getAdGroupStats=myValue/>
  *   </srv:getAdGroupStats_request_var>
  * </srv:AdGroupStatsService>
  * Then call the operation for which you have set the request wrapper value above, like this:
  * <mx:Button id="myButton" label="Call operation" click="myService.getAdGroupStats_send()" />
  */
 package com.macys.marketing.sema{
	import mx.rpc.AsyncToken;
	import flash.events.EventDispatcher;
	import mx.rpc.events.ResultEvent;
	import mx.rpc.events.FaultEvent;
	import flash.utils.ByteArray;
	import mx.rpc.soap.types.*;

    /**
     * Dispatches when a call to the operation getAdGroupStats completes with success
     * and returns some data
     * @eventType GetAdGroupStatsResultEvent
     */
    [Event(name="GetAdGroupStats_result", type="com.macys.marketing.sema.GetAdGroupStatsResultEvent")]
    
	/**
	 * Dispatches when the operation that has been called fails. The fault event is common for all operations
	 * of the WSDL
	 * @eventType mx.rpc.events.FaultEvent
	 */
    [Event(name="fault", type="mx.rpc.events.FaultEvent")]

	public class AdGroupStatsService extends EventDispatcher implements IAdGroupStatsService
	{
    	private var _baseService:BaseAdGroupStatsService;
        
        /**
         * Constructor for the facade; sets the destination and create a baseService instance
         * @param The LCDS destination (if any) associated with the imported WSDL
         */  
        public function AdGroupStatsService(destination:String=null,rootURL:String=null)
        {
        	_baseService = new BaseAdGroupStatsService(destination,rootURL);
        }
        
		//stub functions for the getAdGroupStats operation
          

        /**
         * @see IAdGroupStatsService#getAdGroupStats()
         */
        public function getAdGroupStats(getAdGroupStats:GetAdGroupStats):AsyncToken
        {
         	var _internal_token:AsyncToken = _baseService.getAdGroupStats(getAdGroupStats);
            _internal_token.addEventListener("result",_getAdGroupStats_populate_results);
            _internal_token.addEventListener("fault",throwFault); 
            return _internal_token;
		}
        /**
		 * @see IAdGroupStatsService#getAdGroupStats_send()
		 */    
        public function getAdGroupStats_send():AsyncToken
        {
        	return getAdGroupStats(_getAdGroupStats_request.getAdGroupStats);
        }
              
		/**
		 * Internal representation of the request wrapper for the operation
		 * @private
		 */
		private var _getAdGroupStats_request:GetAdGroupStats_request;
		/**
		 * @see IAdGroupStatsService#getAdGroupStats_request_var
		 */
		[Bindable]
		public function get getAdGroupStats_request_var():GetAdGroupStats_request
		{
			return _getAdGroupStats_request;
		}
		
		/**
		 * @private
		 */
		public function set getAdGroupStats_request_var(request:GetAdGroupStats_request):void
		{
			_getAdGroupStats_request = request;
		}
		
	  		/**
		 * Internal variable to store the operation's lastResult
		 * @private
		 */
        private var _getAdGroupStats_lastResult:GetAdGroupStatsResponse;
		[Bindable]
		/**
		 * @see IAdGroupStatsService#getAdGroupStats_lastResult
		 */	  
		public function get getAdGroupStats_lastResult():GetAdGroupStatsResponse
		{
			return _getAdGroupStats_lastResult;
		}
		/**
		 * @private
		 */
		public function set getAdGroupStats_lastResult(lastResult:GetAdGroupStatsResponse):void
		{
			_getAdGroupStats_lastResult = lastResult;
		}
		
		/**
		 * @see IAdGroupStatsService#addgetAdGroupStats()
		 */
		public function addgetAdGroupStatsEventListener(listener:Function):void
		{
			addEventListener(GetAdGroupStatsResultEvent.GetAdGroupStats_RESULT,listener);
		}
			
		/**
		 * @private
		 */
        private function _getAdGroupStats_populate_results(event:ResultEvent):void
        {
        var e:GetAdGroupStatsResultEvent = new GetAdGroupStatsResultEvent();
		            e.result = event.result as GetAdGroupStatsResponse;
		                       e.headers = event.headers;
		             getAdGroupStats_lastResult = e.result;
		             dispatchEvent(e);
	        		
		}
		
		//service-wide functions
		/**
		 * @see IAdGroupStatsService#getWebService()
		 */
		public function getWebService():BaseAdGroupStatsService
		{
			return _baseService;
		}
		
		/**
		 * Set the event listener for the fault event which can be triggered by each of the operations defined by the facade
		 */
		public function addAdGroupStatsServiceFaultEventListener(listener:Function):void
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