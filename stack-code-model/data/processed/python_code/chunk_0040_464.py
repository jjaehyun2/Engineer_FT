/**
 * PortfolioGroupServiceService.as
 * This file was auto-generated from WSDL by the Apache Axis2 generator modified by Adobe
 * Any change made to this file will be overwritten when the code is re-generated.
 */
 /**
  * Usage example: to use this service from within your Flex application you have two choices:
  * Use it via Actionscript only
  * Use it via MXML tags
  * Actionscript sample code:
  * Step 1: create an instance of the service; pass it the LCDS destination string if any
  * var myService:PortfolioGroupService= new PortfolioGroupService();
  * Step 2: for the desired operation add a result handler (a function that you have already defined previously)  
  * myService.addputPortfolioGroupsEventListener(myResultHandlingFunction);
  * Step 3: Call the operation as a method on the service. Pass the right values as arguments:
  * myService.putPortfolioGroups(myPortfolioGroups,myputPortfolioGroups);
  *
  * MXML sample code:
  * First you need to map the package where the files were generated to a namespace, usually on the <mx:Application> tag, 
  * like this: xmlns:srv="com.macys.marketing.sema.*"
  * Define the service and within its tags set the request wrapper for the desired operation
  * <srv:PortfolioGroupService id="myService">
  *   <srv:putPortfolioGroups_request_var>
  *		<srv:PutPortfolioGroups_request PortfolioGroups=myValue,putPortfolioGroups=myValue/>
  *   </srv:putPortfolioGroups_request_var>
  * </srv:PortfolioGroupService>
  * Then call the operation for which you have set the request wrapper value above, like this:
  * <mx:Button id="myButton" label="Call operation" click="myService.putPortfolioGroups_send()" />
  */
 package com.macys.marketing.sema{
	import mx.rpc.AsyncToken;
	import flash.events.EventDispatcher;
	import mx.rpc.events.ResultEvent;
	import mx.rpc.events.FaultEvent;
	import flash.utils.ByteArray;
	import mx.rpc.soap.types.*;

    /**
     * Dispatches when a call to the operation putPortfolioGroups completes with success
     * and returns some data
     * @eventType PutPortfolioGroupsResultEvent
     */
    [Event(name="PutPortfolioGroups_result", type="com.macys.marketing.sema.PutPortfolioGroupsResultEvent")]
    
    /**
     * Dispatches when a call to the operation getPortfolioGroupList completes with success
     * and returns some data
     * @eventType GetPortfolioGroupListResultEvent
     */
    [Event(name="GetPortfolioGroupList_result", type="com.macys.marketing.sema.GetPortfolioGroupListResultEvent")]
    
    /**
     * Dispatches when a call to the operation getAllPortfolioGroups completes with success
     * and returns some data
     * @eventType GetAllPortfolioGroupsResultEvent
     */
    [Event(name="GetAllPortfolioGroups_result", type="com.macys.marketing.sema.GetAllPortfolioGroupsResultEvent")]
    
	/**
	 * Dispatches when the operation that has been called fails. The fault event is common for all operations
	 * of the WSDL
	 * @eventType mx.rpc.events.FaultEvent
	 */
    [Event(name="fault", type="mx.rpc.events.FaultEvent")]

	public class PortfolioGroupService extends EventDispatcher implements IPortfolioGroupService
	{
    	private var _baseService:BasePortfolioGroupService;
        
        /**
         * Constructor for the facade; sets the destination and create a baseService instance
         * @param The LCDS destination (if any) associated with the imported WSDL
         */  
        public function PortfolioGroupService(destination:String=null,rootURL:String=null)
        {
        	_baseService = new BasePortfolioGroupService(destination,rootURL);
        }
        
		//stub functions for the putPortfolioGroups operation
          

        /**
         * @see IPortfolioGroupService#putPortfolioGroups()
         */
        public function putPortfolioGroups(putPortfolioGroups:PutPortfolioGroups):AsyncToken
        {
         	var _internal_token:AsyncToken = _baseService.putPortfolioGroups(_putPortfolioGroups_header.userName15,putPortfolioGroups);
            _internal_token.addEventListener("result",_putPortfolioGroups_populate_results);
            _internal_token.addEventListener("fault",throwFault); 
            return _internal_token;
		}
        /**
		 * @see IPortfolioGroupService#putPortfolioGroups_send()
		 */    
        public function putPortfolioGroups_send():AsyncToken
        {
        	return putPortfolioGroups(_putPortfolioGroups_request.putPortfolioGroups);
        }
              
		/**
		 * Internal representation of the request wrapper for the operation
		 * @private
		 */
		private var _putPortfolioGroups_request:PutPortfolioGroups_request;
		/**
		 * @see IPortfolioGroupService#putPortfolioGroups_request_var
		 */
		[Bindable]
		public function get putPortfolioGroups_request_var():PutPortfolioGroups_request
		{
			return _putPortfolioGroups_request;
		}
		
		/**
		 * @private
		 */
		public function set putPortfolioGroups_request_var(request:PutPortfolioGroups_request):void
		{
			_putPortfolioGroups_request = request;
		}
					  
		/**
		 * Internal representation of the header wrapper
		 * @private
		 */
		private var _putPortfolioGroups_header:Object;
		[Bindable]
		/**
		 * @see IPortfolioGroupService#putPortfolioGroups_header
		 */
		public function get putPortfolioGroups_header():Object
		{
			return _putPortfolioGroups_header;
		}
		public function set putPortfolioGroups_header(header:Object):void
		{
			_putPortfolioGroups_header = header;
		}
		/**
		 * Add values for the various parts of the header
         * @param 
         userName15
		 */ 
		public function addputPortfolioGroups_header(userName15:com.macys.marketing.sema.UserName):void
		{
			_putPortfolioGroups_header = new Object;
            _putPortfolioGroups_header.userName15 = userName15;
              		
		}
	  		/**
		 * Internal variable to store the operation's lastResult
		 * @private
		 */
        private var _putPortfolioGroups_lastResult:PutPortfolioGroupsResponse;
		[Bindable]
		/**
		 * @see IPortfolioGroupService#putPortfolioGroups_lastResult
		 */	  
		public function get putPortfolioGroups_lastResult():PutPortfolioGroupsResponse
		{
			return _putPortfolioGroups_lastResult;
		}
		/**
		 * @private
		 */
		public function set putPortfolioGroups_lastResult(lastResult:PutPortfolioGroupsResponse):void
		{
			_putPortfolioGroups_lastResult = lastResult;
		}
		
		/**
		 * @see IPortfolioGroupService#addputPortfolioGroups()
		 */
		public function addputPortfolioGroupsEventListener(listener:Function):void
		{
			addEventListener(PutPortfolioGroupsResultEvent.PutPortfolioGroups_RESULT,listener);
		}
			
		/**
		 * @private
		 */
        private function _putPortfolioGroups_populate_results(event:ResultEvent):void
        {
        var e:PutPortfolioGroupsResultEvent = new PutPortfolioGroupsResultEvent();
		            e.result = event.result as PutPortfolioGroupsResponse;
		                       e.headers = event.headers;
		             putPortfolioGroups_lastResult = e.result;
		             dispatchEvent(e);
	        		
		}
		
		//stub functions for the getPortfolioGroupList operation
          

        /**
         * @see IPortfolioGroupService#getPortfolioGroupList()
         */
        public function getPortfolioGroupList(getPortfolioGroupList:GetPortfolioGroupList):AsyncToken
        {
         	var _internal_token:AsyncToken = _baseService.getPortfolioGroupList(getPortfolioGroupList);
            _internal_token.addEventListener("result",_getPortfolioGroupList_populate_results);
            _internal_token.addEventListener("fault",throwFault); 
            return _internal_token;
		}
        /**
		 * @see IPortfolioGroupService#getPortfolioGroupList_send()
		 */    
        public function getPortfolioGroupList_send():AsyncToken
        {
        	return getPortfolioGroupList(_getPortfolioGroupList_request.getPortfolioGroupList);
        }
              
		/**
		 * Internal representation of the request wrapper for the operation
		 * @private
		 */
		private var _getPortfolioGroupList_request:GetPortfolioGroupList_request;
		/**
		 * @see IPortfolioGroupService#getPortfolioGroupList_request_var
		 */
		[Bindable]
		public function get getPortfolioGroupList_request_var():GetPortfolioGroupList_request
		{
			return _getPortfolioGroupList_request;
		}
		
		/**
		 * @private
		 */
		public function set getPortfolioGroupList_request_var(request:GetPortfolioGroupList_request):void
		{
			_getPortfolioGroupList_request = request;
		}
		
	  		/**
		 * Internal variable to store the operation's lastResult
		 * @private
		 */
        private var _getPortfolioGroupList_lastResult:GetPortfolioGroupListResponse;
		[Bindable]
		/**
		 * @see IPortfolioGroupService#getPortfolioGroupList_lastResult
		 */	  
		public function get getPortfolioGroupList_lastResult():GetPortfolioGroupListResponse
		{
			return _getPortfolioGroupList_lastResult;
		}
		/**
		 * @private
		 */
		public function set getPortfolioGroupList_lastResult(lastResult:GetPortfolioGroupListResponse):void
		{
			_getPortfolioGroupList_lastResult = lastResult;
		}
		
		/**
		 * @see IPortfolioGroupService#addgetPortfolioGroupList()
		 */
		public function addgetPortfolioGroupListEventListener(listener:Function):void
		{
			addEventListener(GetPortfolioGroupListResultEvent.GetPortfolioGroupList_RESULT,listener);
		}
			
		/**
		 * @private
		 */
        private function _getPortfolioGroupList_populate_results(event:ResultEvent):void
        {
        var e:GetPortfolioGroupListResultEvent = new GetPortfolioGroupListResultEvent();
		            e.result = event.result as GetPortfolioGroupListResponse;
		                       e.headers = event.headers;
		             getPortfolioGroupList_lastResult = e.result;
		             dispatchEvent(e);
	        		
		}
		
		//stub functions for the getAllPortfolioGroups operation
          

        /**
         * @see IPortfolioGroupService#getAllPortfolioGroups()
         */
        public function getAllPortfolioGroups(getAllPortfolioGroups:GetAllPortfolioGroups):AsyncToken
        {
         	var _internal_token:AsyncToken = _baseService.getAllPortfolioGroups(getAllPortfolioGroups);
            _internal_token.addEventListener("result",_getAllPortfolioGroups_populate_results);
            _internal_token.addEventListener("fault",throwFault); 
            return _internal_token;
		}
        /**
		 * @see IPortfolioGroupService#getAllPortfolioGroups_send()
		 */    
        public function getAllPortfolioGroups_send():AsyncToken
        {
        	return getAllPortfolioGroups(_getAllPortfolioGroups_request.getAllPortfolioGroups);
        }
              
		/**
		 * Internal representation of the request wrapper for the operation
		 * @private
		 */
		private var _getAllPortfolioGroups_request:GetAllPortfolioGroups_request;
		/**
		 * @see IPortfolioGroupService#getAllPortfolioGroups_request_var
		 */
		[Bindable]
		public function get getAllPortfolioGroups_request_var():GetAllPortfolioGroups_request
		{
			return _getAllPortfolioGroups_request;
		}
		
		/**
		 * @private
		 */
		public function set getAllPortfolioGroups_request_var(request:GetAllPortfolioGroups_request):void
		{
			_getAllPortfolioGroups_request = request;
		}
		
	  		/**
		 * Internal variable to store the operation's lastResult
		 * @private
		 */
        private var _getAllPortfolioGroups_lastResult:GetAllPortfolioGroupsResponse;
		[Bindable]
		/**
		 * @see IPortfolioGroupService#getAllPortfolioGroups_lastResult
		 */	  
		public function get getAllPortfolioGroups_lastResult():GetAllPortfolioGroupsResponse
		{
			return _getAllPortfolioGroups_lastResult;
		}
		/**
		 * @private
		 */
		public function set getAllPortfolioGroups_lastResult(lastResult:GetAllPortfolioGroupsResponse):void
		{
			_getAllPortfolioGroups_lastResult = lastResult;
		}
		
		/**
		 * @see IPortfolioGroupService#addgetAllPortfolioGroups()
		 */
		public function addgetAllPortfolioGroupsEventListener(listener:Function):void
		{
			addEventListener(GetAllPortfolioGroupsResultEvent.GetAllPortfolioGroups_RESULT,listener);
		}
			
		/**
		 * @private
		 */
        private function _getAllPortfolioGroups_populate_results(event:ResultEvent):void
        {
        var e:GetAllPortfolioGroupsResultEvent = new GetAllPortfolioGroupsResultEvent();
		            e.result = event.result as GetAllPortfolioGroupsResponse;
		                       e.headers = event.headers;
		             getAllPortfolioGroups_lastResult = e.result;
		             dispatchEvent(e);
	        		
		}
		
		//service-wide functions
		/**
		 * @see IPortfolioGroupService#getWebService()
		 */
		public function getWebService():BasePortfolioGroupService
		{
			return _baseService;
		}
		
		/**
		 * Set the event listener for the fault event which can be triggered by each of the operations defined by the facade
		 */
		public function addPortfolioGroupServiceFaultEventListener(listener:Function):void
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