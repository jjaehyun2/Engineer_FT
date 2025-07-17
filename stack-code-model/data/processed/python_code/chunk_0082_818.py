/**
 * AdKeyWordServiceService.as
 * This file was auto-generated from WSDL by the Apache Axis2 generator modified by Adobe
 * Any change made to this file will be overwritten when the code is re-generated.
 */
 /**
  * Usage example: to use this service from within your Flex application you have two choices:
  * Use it via Actionscript only
  * Use it via MXML tags
  * Actionscript sample code:
  * Step 1: create an instance of the service; pass it the LCDS destination string if any
  * var myService:AdKeyWordService= new AdKeyWordService();
  * Step 2: for the desired operation add a result handler (a function that you have already defined previously)  
  * myService.addgetAdKeywordListEventListener(myResultHandlingFunction);
  * Step 3: Call the operation as a method on the service. Pass the right values as arguments:
  * myService.getAdKeywordList(mygetAdKeywordList,myAdKeywordId);
  *
  * MXML sample code:
  * First you need to map the package where the files were generated to a namespace, usually on the <mx:Application> tag, 
  * like this: xmlns:srv="com.macys.marketing.sema.*"
  * Define the service and within its tags set the request wrapper for the desired operation
  * <srv:AdKeyWordService id="myService">
  *   <srv:getAdKeywordList_request_var>
  *		<srv:GetAdKeywordList_request getAdKeywordList=myValue,AdKeywordId=myValue/>
  *   </srv:getAdKeywordList_request_var>
  * </srv:AdKeyWordService>
  * Then call the operation for which you have set the request wrapper value above, like this:
  * <mx:Button id="myButton" label="Call operation" click="myService.getAdKeywordList_send()" />
  */
 package com.macys.marketing.sema{
	import mx.rpc.AsyncToken;
	import flash.events.EventDispatcher;
	import mx.rpc.events.ResultEvent;
	import mx.rpc.events.FaultEvent;
	import flash.utils.ByteArray;
	import mx.rpc.soap.types.*;

    /**
     * Dispatches when a call to the operation getAdKeywordList completes with success
     * and returns some data
     * @eventType GetAdKeywordListResultEvent
     */
    [Event(name="GetAdKeywordList_result", type="com.macys.marketing.sema.GetAdKeywordListResultEvent")]
    
    /**
     * Dispatches when a call to the operation getAllAdKeywords completes with success
     * and returns some data
     * @eventType GetAllAdKeywordsResultEvent
     */
    [Event(name="GetAllAdKeywords_result", type="com.macys.marketing.sema.GetAllAdKeywordsResultEvent")]
    
    /**
     * Dispatches when a call to the operation putAdKeywords completes with success
     * and returns some data
     * @eventType PutAdKeywordsResultEvent
     */
    [Event(name="PutAdKeywords_result", type="com.macys.marketing.sema.PutAdKeywordsResultEvent")]
    
	/**
	 * Dispatches when the operation that has been called fails. The fault event is common for all operations
	 * of the WSDL
	 * @eventType mx.rpc.events.FaultEvent
	 */
    [Event(name="fault", type="mx.rpc.events.FaultEvent")]

	public class AdKeyWordService extends EventDispatcher implements IAdKeyWordService
	{
    	private var _baseService:BaseAdKeyWordService;
        
        /**
         * Constructor for the facade; sets the destination and create a baseService instance
         * @param The LCDS destination (if any) associated with the imported WSDL
         */  
        public function AdKeyWordService(destination:String=null,rootURL:String=null)
        {
        	_baseService = new BaseAdKeyWordService(destination,rootURL);
        }
        
		//stub functions for the getAdKeywordList operation
          

        /**
         * @see IAdKeyWordService#getAdKeywordList()
         */
        public function getAdKeywordList(getAdKeywordList:GetAdKeywordList):AsyncToken
        {
         	var _internal_token:AsyncToken = _baseService.getAdKeywordList(getAdKeywordList);
            _internal_token.addEventListener("result",_getAdKeywordList_populate_results);
            _internal_token.addEventListener("fault",throwFault); 
            return _internal_token;
		}
        /**
		 * @see IAdKeyWordService#getAdKeywordList_send()
		 */    
        public function getAdKeywordList_send():AsyncToken
        {
        	return getAdKeywordList(_getAdKeywordList_request.getAdKeywordList);
        }
              
		/**
		 * Internal representation of the request wrapper for the operation
		 * @private
		 */
		private var _getAdKeywordList_request:GetAdKeywordList_request;
		/**
		 * @see IAdKeyWordService#getAdKeywordList_request_var
		 */
		[Bindable]
		public function get getAdKeywordList_request_var():GetAdKeywordList_request
		{
			return _getAdKeywordList_request;
		}
		
		/**
		 * @private
		 */
		public function set getAdKeywordList_request_var(request:GetAdKeywordList_request):void
		{
			_getAdKeywordList_request = request;
		}
		
	  		/**
		 * Internal variable to store the operation's lastResult
		 * @private
		 */
        private var _getAdKeywordList_lastResult:GetAdKeywordListResponse;
		[Bindable]
		/**
		 * @see IAdKeyWordService#getAdKeywordList_lastResult
		 */	  
		public function get getAdKeywordList_lastResult():GetAdKeywordListResponse
		{
			return _getAdKeywordList_lastResult;
		}
		/**
		 * @private
		 */
		public function set getAdKeywordList_lastResult(lastResult:GetAdKeywordListResponse):void
		{
			_getAdKeywordList_lastResult = lastResult;
		}
		
		/**
		 * @see IAdKeyWordService#addgetAdKeywordList()
		 */
		public function addgetAdKeywordListEventListener(listener:Function):void
		{
			addEventListener(GetAdKeywordListResultEvent.GetAdKeywordList_RESULT,listener);
		}
			
		/**
		 * @private
		 */
        private function _getAdKeywordList_populate_results(event:ResultEvent):void
        {
        var e:GetAdKeywordListResultEvent = new GetAdKeywordListResultEvent();
		            e.result = event.result as GetAdKeywordListResponse;
		                       e.headers = event.headers;
		             getAdKeywordList_lastResult = e.result;
		             dispatchEvent(e);
	        		
		}
		
		//stub functions for the getAllAdKeywords operation
          

        /**
         * @see IAdKeyWordService#getAllAdKeywords()
         */
        public function getAllAdKeywords(getAllAdKeywords:GetAllAdKeywords):AsyncToken
        {
         	var _internal_token:AsyncToken = _baseService.getAllAdKeywords(getAllAdKeywords);
            _internal_token.addEventListener("result",_getAllAdKeywords_populate_results);
            _internal_token.addEventListener("fault",throwFault); 
            return _internal_token;
		}
        /**
		 * @see IAdKeyWordService#getAllAdKeywords_send()
		 */    
        public function getAllAdKeywords_send():AsyncToken
        {
        	return getAllAdKeywords(_getAllAdKeywords_request.getAllAdKeywords);
        }
              
		/**
		 * Internal representation of the request wrapper for the operation
		 * @private
		 */
		private var _getAllAdKeywords_request:GetAllAdKeywords_request;
		/**
		 * @see IAdKeyWordService#getAllAdKeywords_request_var
		 */
		[Bindable]
		public function get getAllAdKeywords_request_var():GetAllAdKeywords_request
		{
			return _getAllAdKeywords_request;
		}
		
		/**
		 * @private
		 */
		public function set getAllAdKeywords_request_var(request:GetAllAdKeywords_request):void
		{
			_getAllAdKeywords_request = request;
		}
		
	  		/**
		 * Internal variable to store the operation's lastResult
		 * @private
		 */
        private var _getAllAdKeywords_lastResult:GetAllAdKeywordsResponse;
		[Bindable]
		/**
		 * @see IAdKeyWordService#getAllAdKeywords_lastResult
		 */	  
		public function get getAllAdKeywords_lastResult():GetAllAdKeywordsResponse
		{
			return _getAllAdKeywords_lastResult;
		}
		/**
		 * @private
		 */
		public function set getAllAdKeywords_lastResult(lastResult:GetAllAdKeywordsResponse):void
		{
			_getAllAdKeywords_lastResult = lastResult;
		}
		
		/**
		 * @see IAdKeyWordService#addgetAllAdKeywords()
		 */
		public function addgetAllAdKeywordsEventListener(listener:Function):void
		{
			addEventListener(GetAllAdKeywordsResultEvent.GetAllAdKeywords_RESULT,listener);
		}
			
		/**
		 * @private
		 */
        private function _getAllAdKeywords_populate_results(event:ResultEvent):void
        {
        var e:GetAllAdKeywordsResultEvent = new GetAllAdKeywordsResultEvent();
		            e.result = event.result as GetAllAdKeywordsResponse;
		                       e.headers = event.headers;
		             getAllAdKeywords_lastResult = e.result;
		             dispatchEvent(e);
	        		
		}
		
		//stub functions for the putAdKeywords operation
          

        /**
         * @see IAdKeyWordService#putAdKeywords()
         */
        public function putAdKeywords(putAdKeywords:PutAdKeywords):AsyncToken
        {
         	var _internal_token:AsyncToken = _baseService.putAdKeywords(_putAdKeywords_header.userName19,putAdKeywords);
            _internal_token.addEventListener("result",_putAdKeywords_populate_results);
            _internal_token.addEventListener("fault",throwFault); 
            return _internal_token;
		}
        /**
		 * @see IAdKeyWordService#putAdKeywords_send()
		 */    
        public function putAdKeywords_send():AsyncToken
        {
        	return putAdKeywords(_putAdKeywords_request.putAdKeywords);
        }
              
		/**
		 * Internal representation of the request wrapper for the operation
		 * @private
		 */
		private var _putAdKeywords_request:PutAdKeywords_request;
		/**
		 * @see IAdKeyWordService#putAdKeywords_request_var
		 */
		[Bindable]
		public function get putAdKeywords_request_var():PutAdKeywords_request
		{
			return _putAdKeywords_request;
		}
		
		/**
		 * @private
		 */
		public function set putAdKeywords_request_var(request:PutAdKeywords_request):void
		{
			_putAdKeywords_request = request;
		}
					  
		/**
		 * Internal representation of the header wrapper
		 * @private
		 */
		private var _putAdKeywords_header:Object;
		[Bindable]
		/**
		 * @see IAdKeyWordService#putAdKeywords_header
		 */
		public function get putAdKeywords_header():Object
		{
			return _putAdKeywords_header;
		}
		public function set putAdKeywords_header(header:Object):void
		{
			_putAdKeywords_header = header;
		}
		/**
		 * Add values for the various parts of the header
         * @param 
         userName19
		 */ 
		public function addputAdKeywords_header(userName19:com.macys.marketing.sema.UserName):void
		{
			_putAdKeywords_header = new Object;
            _putAdKeywords_header.userName19 = userName19;
              		
		}
	  		/**
		 * Internal variable to store the operation's lastResult
		 * @private
		 */
        private var _putAdKeywords_lastResult:PutAdKeywordsResponse;
		[Bindable]
		/**
		 * @see IAdKeyWordService#putAdKeywords_lastResult
		 */	  
		public function get putAdKeywords_lastResult():PutAdKeywordsResponse
		{
			return _putAdKeywords_lastResult;
		}
		/**
		 * @private
		 */
		public function set putAdKeywords_lastResult(lastResult:PutAdKeywordsResponse):void
		{
			_putAdKeywords_lastResult = lastResult;
		}
		
		/**
		 * @see IAdKeyWordService#addputAdKeywords()
		 */
		public function addputAdKeywordsEventListener(listener:Function):void
		{
			addEventListener(PutAdKeywordsResultEvent.PutAdKeywords_RESULT,listener);
		}
			
		/**
		 * @private
		 */
        private function _putAdKeywords_populate_results(event:ResultEvent):void
        {
        var e:PutAdKeywordsResultEvent = new PutAdKeywordsResultEvent();
		            e.result = event.result as PutAdKeywordsResponse;
		                       e.headers = event.headers;
		             putAdKeywords_lastResult = e.result;
		             dispatchEvent(e);
	        		
		}
		
		//service-wide functions
		/**
		 * @see IAdKeyWordService#getWebService()
		 */
		public function getWebService():BaseAdKeyWordService
		{
			return _baseService;
		}
		
		/**
		 * Set the event listener for the fault event which can be triggered by each of the operations defined by the facade
		 */
		public function addAdKeyWordServiceFaultEventListener(listener:Function):void
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