/**
 * AdCopyStatsServiceService.as
 * This file was auto-generated from WSDL by the Apache Axis2 generator modified by Adobe
 * Any change made to this file will be overwritten when the code is re-generated.
 */
 /**
  * Usage example: to use this service from within your Flex application you have two choices:
  * Use it via Actionscript only
  * Use it via MXML tags
  * Actionscript sample code:
  * Step 1: create an instance of the service; pass it the LCDS destination string if any
  * var myService:AdCopyStatsService= new AdCopyStatsService();
  * Step 2: for the desired operation add a result handler (a function that you have already defined previously)  
  * myService.addgetAdCopyStatsEventListener(myResultHandlingFunction);
  * Step 3: Call the operation as a method on the service. Pass the right values as arguments:
  * myService.getAdCopyStats(mygetAdCopyStats,myAdCopyIds,myType);
  *
  * MXML sample code:
  * First you need to map the package where the files were generated to a namespace, usually on the <mx:Application> tag, 
  * like this: xmlns:srv="com.macys.marketing.sema.*"
  * Define the service and within its tags set the request wrapper for the desired operation
  * <srv:AdCopyStatsService id="myService">
  *   <srv:getAdCopyStats_request_var>
  *		<srv:GetAdCopyStats_request getAdCopyStats=myValue,AdCopyIds=myValue,Type=myValue/>
  *   </srv:getAdCopyStats_request_var>
  * </srv:AdCopyStatsService>
  * Then call the operation for which you have set the request wrapper value above, like this:
  * <mx:Button id="myButton" label="Call operation" click="myService.getAdCopyStats_send()" />
  */
 package com.macys.marketing.sema{
	import mx.rpc.AsyncToken;
	import flash.events.EventDispatcher;
	import mx.rpc.events.ResultEvent;
	import mx.rpc.events.FaultEvent;
	import flash.utils.ByteArray;
	import mx.rpc.soap.types.*;

    /**
     * Dispatches when a call to the operation getAdCopyStats completes with success
     * and returns some data
     * @eventType GetAdCopyStatsResultEvent
     */
    [Event(name="GetAdCopyStats_result", type="com.macys.marketing.sema.GetAdCopyStatsResultEvent")]
    
	/**
	 * Dispatches when the operation that has been called fails. The fault event is common for all operations
	 * of the WSDL
	 * @eventType mx.rpc.events.FaultEvent
	 */
    [Event(name="fault", type="mx.rpc.events.FaultEvent")]

	public class AdCopyStatsService extends EventDispatcher implements IAdCopyStatsService
	{
    	private var _baseService:BaseAdCopyStatsService;
        
        /**
         * Constructor for the facade; sets the destination and create a baseService instance
         * @param The LCDS destination (if any) associated with the imported WSDL
         */  
        public function AdCopyStatsService(destination:String=null,rootURL:String=null)
        {
        	_baseService = new BaseAdCopyStatsService(destination,rootURL);
        }
        
		//stub functions for the getAdCopyStats operation
          

        /**
         * @see IAdCopyStatsService#getAdCopyStats()
         */
        public function getAdCopyStats(getAdCopyStats:GetAdCopyStats):AsyncToken
        {
         	var _internal_token:AsyncToken = _baseService.getAdCopyStats(getAdCopyStats);
            _internal_token.addEventListener("result",_getAdCopyStats_populate_results);
            _internal_token.addEventListener("fault",throwFault); 
            return _internal_token;
		}
        /**
		 * @see IAdCopyStatsService#getAdCopyStats_send()
		 */    
        public function getAdCopyStats_send():AsyncToken
        {
        	return getAdCopyStats(_getAdCopyStats_request.getAdCopyStats);
        }
              
		/**
		 * Internal representation of the request wrapper for the operation
		 * @private
		 */
		private var _getAdCopyStats_request:GetAdCopyStats_request;
		/**
		 * @see IAdCopyStatsService#getAdCopyStats_request_var
		 */
		[Bindable]
		public function get getAdCopyStats_request_var():GetAdCopyStats_request
		{
			return _getAdCopyStats_request;
		}
		
		/**
		 * @private
		 */
		public function set getAdCopyStats_request_var(request:GetAdCopyStats_request):void
		{
			_getAdCopyStats_request = request;
		}
		
	  		/**
		 * Internal variable to store the operation's lastResult
		 * @private
		 */
        private var _getAdCopyStats_lastResult:GetAdCopyStatsResponse;
		[Bindable]
		/**
		 * @see IAdCopyStatsService#getAdCopyStats_lastResult
		 */	  
		public function get getAdCopyStats_lastResult():GetAdCopyStatsResponse
		{
			return _getAdCopyStats_lastResult;
		}
		/**
		 * @private
		 */
		public function set getAdCopyStats_lastResult(lastResult:GetAdCopyStatsResponse):void
		{
			_getAdCopyStats_lastResult = lastResult;
		}
		
		/**
		 * @see IAdCopyStatsService#addgetAdCopyStats()
		 */
		public function addgetAdCopyStatsEventListener(listener:Function):void
		{
			addEventListener(GetAdCopyStatsResultEvent.GetAdCopyStats_RESULT,listener);
		}
			
		/**
		 * @private
		 */
        private function _getAdCopyStats_populate_results(event:ResultEvent):void
        {
        var e:GetAdCopyStatsResultEvent = new GetAdCopyStatsResultEvent();
		            e.result = event.result as GetAdCopyStatsResponse;
		                       e.headers = event.headers;
		             getAdCopyStats_lastResult = e.result;
		             dispatchEvent(e);
	        		
		}
		
		//service-wide functions
		/**
		 * @see IAdCopyStatsService#getWebService()
		 */
		public function getWebService():BaseAdCopyStatsService
		{
			return _baseService;
		}
		
		/**
		 * Set the event listener for the fault event which can be triggered by each of the operations defined by the facade
		 */
		public function addAdCopyStatsServiceFaultEventListener(listener:Function):void
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