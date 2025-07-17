/**
 * AdCopyServiceService.as
 * This file was auto-generated from WSDL by the Apache Axis2 generator modified by Adobe
 * Any change made to this file will be overwritten when the code is re-generated.
 */
 /**
  * Usage example: to use this service from within your Flex application you have two choices:
  * Use it via Actionscript only
  * Use it via MXML tags
  * Actionscript sample code:
  * Step 1: create an instance of the service; pass it the LCDS destination string if any
  * var myService:AdCopyService= new AdCopyService();
  * Step 2: for the desired operation add a result handler (a function that you have already defined previously)  
  * myService.addgetAllAdCopyEventListener(myResultHandlingFunction);
  * Step 3: Call the operation as a method on the service. Pass the right values as arguments:
  * myService.getAllAdCopy(mygetAllAdCopy,myGroupId);
  *
  * MXML sample code:
  * First you need to map the package where the files were generated to a namespace, usually on the <mx:Application> tag, 
  * like this: xmlns:srv="com.macys.marketing.sema.*"
  * Define the service and within its tags set the request wrapper for the desired operation
  * <srv:AdCopyService id="myService">
  *   <srv:getAllAdCopy_request_var>
  *		<srv:GetAllAdCopy_request getAllAdCopy=myValue,GroupId=myValue/>
  *   </srv:getAllAdCopy_request_var>
  * </srv:AdCopyService>
  * Then call the operation for which you have set the request wrapper value above, like this:
  * <mx:Button id="myButton" label="Call operation" click="myService.getAllAdCopy_send()" />
  */
 package com.macys.marketing.sema{
	import mx.rpc.AsyncToken;
	import flash.events.EventDispatcher;
	import mx.rpc.events.ResultEvent;
	import mx.rpc.events.FaultEvent;
	import flash.utils.ByteArray;
	import mx.rpc.soap.types.*;

    /**
     * Dispatches when a call to the operation getAllAdCopy completes with success
     * and returns some data
     * @eventType GetAllAdCopyResultEvent
     */
    [Event(name="GetAllAdCopy_result", type="com.macys.marketing.sema.GetAllAdCopyResultEvent")]
    
    /**
     * Dispatches when a call to the operation getAdCopyList completes with success
     * and returns some data
     * @eventType GetAdCopyListResultEvent
     */
    [Event(name="GetAdCopyList_result", type="com.macys.marketing.sema.GetAdCopyListResultEvent")]
    
    /**
     * Dispatches when a call to the operation putAdCopyList completes with success
     * and returns some data
     * @eventType PutAdCopyListResultEvent
     */
    [Event(name="PutAdCopyList_result", type="com.macys.marketing.sema.PutAdCopyListResultEvent")]
    
	/**
	 * Dispatches when the operation that has been called fails. The fault event is common for all operations
	 * of the WSDL
	 * @eventType mx.rpc.events.FaultEvent
	 */
    [Event(name="fault", type="mx.rpc.events.FaultEvent")]

	public class AdCopyService extends EventDispatcher implements IAdCopyService
	{
    	private var _baseService:BaseAdCopyService;
        
        /**
         * Constructor for the facade; sets the destination and create a baseService instance
         * @param The LCDS destination (if any) associated with the imported WSDL
         */  
        public function AdCopyService(destination:String=null,rootURL:String=null)
        {
        	_baseService = new BaseAdCopyService(destination,rootURL);
        }
        
		//stub functions for the getAllAdCopy operation
          

        /**
         * @see IAdCopyService#getAllAdCopy()
         */
        public function getAllAdCopy(getAllAdCopy:GetAllAdCopy):AsyncToken
        {
         	var _internal_token:AsyncToken = _baseService.getAllAdCopy(getAllAdCopy);
            _internal_token.addEventListener("result",_getAllAdCopy_populate_results);
            _internal_token.addEventListener("fault",throwFault); 
            return _internal_token;
		}
        /**
		 * @see IAdCopyService#getAllAdCopy_send()
		 */    
        public function getAllAdCopy_send():AsyncToken
        {
        	return getAllAdCopy(_getAllAdCopy_request.getAllAdCopy);
        }
              
		/**
		 * Internal representation of the request wrapper for the operation
		 * @private
		 */
		private var _getAllAdCopy_request:GetAllAdCopy_request;
		/**
		 * @see IAdCopyService#getAllAdCopy_request_var
		 */
		[Bindable]
		public function get getAllAdCopy_request_var():GetAllAdCopy_request
		{
			return _getAllAdCopy_request;
		}
		
		/**
		 * @private
		 */
		public function set getAllAdCopy_request_var(request:GetAllAdCopy_request):void
		{
			_getAllAdCopy_request = request;
		}
		
	  		/**
		 * Internal variable to store the operation's lastResult
		 * @private
		 */
        private var _getAllAdCopy_lastResult:GetAllAdCopyResponse;
		[Bindable]
		/**
		 * @see IAdCopyService#getAllAdCopy_lastResult
		 */	  
		public function get getAllAdCopy_lastResult():GetAllAdCopyResponse
		{
			return _getAllAdCopy_lastResult;
		}
		/**
		 * @private
		 */
		public function set getAllAdCopy_lastResult(lastResult:GetAllAdCopyResponse):void
		{
			_getAllAdCopy_lastResult = lastResult;
		}
		
		/**
		 * @see IAdCopyService#addgetAllAdCopy()
		 */
		public function addgetAllAdCopyEventListener(listener:Function):void
		{
			addEventListener(GetAllAdCopyResultEvent.GetAllAdCopy_RESULT,listener);
		}
			
		/**
		 * @private
		 */
        private function _getAllAdCopy_populate_results(event:ResultEvent):void
        {
        var e:GetAllAdCopyResultEvent = new GetAllAdCopyResultEvent();
		            e.result = event.result as GetAllAdCopyResponse;
		                       e.headers = event.headers;
		             getAllAdCopy_lastResult = e.result;
		             dispatchEvent(e);
	        		
		}
		
		//stub functions for the getAdCopyList operation
          

        /**
         * @see IAdCopyService#getAdCopyList()
         */
        public function getAdCopyList(getAdCopyList:GetAdCopyList):AsyncToken
        {
         	var _internal_token:AsyncToken = _baseService.getAdCopyList(getAdCopyList);
            _internal_token.addEventListener("result",_getAdCopyList_populate_results);
            _internal_token.addEventListener("fault",throwFault); 
            return _internal_token;
		}
        /**
		 * @see IAdCopyService#getAdCopyList_send()
		 */    
        public function getAdCopyList_send():AsyncToken
        {
        	return getAdCopyList(_getAdCopyList_request.getAdCopyList);
        }
              
		/**
		 * Internal representation of the request wrapper for the operation
		 * @private
		 */
		private var _getAdCopyList_request:GetAdCopyList_request;
		/**
		 * @see IAdCopyService#getAdCopyList_request_var
		 */
		[Bindable]
		public function get getAdCopyList_request_var():GetAdCopyList_request
		{
			return _getAdCopyList_request;
		}
		
		/**
		 * @private
		 */
		public function set getAdCopyList_request_var(request:GetAdCopyList_request):void
		{
			_getAdCopyList_request = request;
		}
		
	  		/**
		 * Internal variable to store the operation's lastResult
		 * @private
		 */
        private var _getAdCopyList_lastResult:GetAdCopyListResponse;
		[Bindable]
		/**
		 * @see IAdCopyService#getAdCopyList_lastResult
		 */	  
		public function get getAdCopyList_lastResult():GetAdCopyListResponse
		{
			return _getAdCopyList_lastResult;
		}
		/**
		 * @private
		 */
		public function set getAdCopyList_lastResult(lastResult:GetAdCopyListResponse):void
		{
			_getAdCopyList_lastResult = lastResult;
		}
		
		/**
		 * @see IAdCopyService#addgetAdCopyList()
		 */
		public function addgetAdCopyListEventListener(listener:Function):void
		{
			addEventListener(GetAdCopyListResultEvent.GetAdCopyList_RESULT,listener);
		}
			
		/**
		 * @private
		 */
        private function _getAdCopyList_populate_results(event:ResultEvent):void
        {
        var e:GetAdCopyListResultEvent = new GetAdCopyListResultEvent();
		            e.result = event.result as GetAdCopyListResponse;
		                       e.headers = event.headers;
		             getAdCopyList_lastResult = e.result;
		             dispatchEvent(e);
	        		
		}
		
		//stub functions for the putAdCopyList operation
          

        /**
         * @see IAdCopyService#putAdCopyList()
         */
        public function putAdCopyList(putAdCopyList:PutAdCopyList):AsyncToken
        {
         	var _internal_token:AsyncToken = _baseService.putAdCopyList(_putAdCopyList_header.userName19,putAdCopyList);
            _internal_token.addEventListener("result",_putAdCopyList_populate_results);
            _internal_token.addEventListener("fault",throwFault); 
            return _internal_token;
		}
        /**
		 * @see IAdCopyService#putAdCopyList_send()
		 */    
        public function putAdCopyList_send():AsyncToken
        {
        	return putAdCopyList(_putAdCopyList_request.putAdCopyList);
        }
              
		/**
		 * Internal representation of the request wrapper for the operation
		 * @private
		 */
		private var _putAdCopyList_request:PutAdCopyList_request;
		/**
		 * @see IAdCopyService#putAdCopyList_request_var
		 */
		[Bindable]
		public function get putAdCopyList_request_var():PutAdCopyList_request
		{
			return _putAdCopyList_request;
		}
		
		/**
		 * @private
		 */
		public function set putAdCopyList_request_var(request:PutAdCopyList_request):void
		{
			_putAdCopyList_request = request;
		}
					  
		/**
		 * Internal representation of the header wrapper
		 * @private
		 */
		private var _putAdCopyList_header:Object;
		[Bindable]
		/**
		 * @see IAdCopyService#putAdCopyList_header
		 */
		public function get putAdCopyList_header():Object
		{
			return _putAdCopyList_header;
		}
		public function set putAdCopyList_header(header:Object):void
		{
			_putAdCopyList_header = header;
		}
		/**
		 * Add values for the various parts of the header
         * @param 
         userName19
		 */ 
		public function addputAdCopyList_header(userName19:com.macys.marketing.sema.UserName):void
		{
			_putAdCopyList_header = new Object;
            _putAdCopyList_header.userName19 = userName19;
              		
		}
	  		/**
		 * Internal variable to store the operation's lastResult
		 * @private
		 */
        private var _putAdCopyList_lastResult:PutAdCopyListResponse;
		[Bindable]
		/**
		 * @see IAdCopyService#putAdCopyList_lastResult
		 */	  
		public function get putAdCopyList_lastResult():PutAdCopyListResponse
		{
			return _putAdCopyList_lastResult;
		}
		/**
		 * @private
		 */
		public function set putAdCopyList_lastResult(lastResult:PutAdCopyListResponse):void
		{
			_putAdCopyList_lastResult = lastResult;
		}
		
		/**
		 * @see IAdCopyService#addputAdCopyList()
		 */
		public function addputAdCopyListEventListener(listener:Function):void
		{
			addEventListener(PutAdCopyListResultEvent.PutAdCopyList_RESULT,listener);
		}
			
		/**
		 * @private
		 */
        private function _putAdCopyList_populate_results(event:ResultEvent):void
        {
        var e:PutAdCopyListResultEvent = new PutAdCopyListResultEvent();
		            e.result = event.result as PutAdCopyListResponse;
		                       e.headers = event.headers;
		             putAdCopyList_lastResult = e.result;
		             dispatchEvent(e);
	        		
		}
		
		//service-wide functions
		/**
		 * @see IAdCopyService#getWebService()
		 */
		public function getWebService():BaseAdCopyService
		{
			return _baseService;
		}
		
		/**
		 * Set the event listener for the fault event which can be triggered by each of the operations defined by the facade
		 */
		public function addAdCopyServiceFaultEventListener(listener:Function):void
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