/**
 * Service.as
 * This file was auto-generated from WSDL by the Apache Axis2 generator modified by Adobe
 * Any change made to this file will be overwritten when the code is re-generated.
 */
package com.macys.marketing.sema{
	import mx.rpc.AsyncToken;
	import flash.utils.ByteArray;
	import mx.rpc.soap.types.*;
               
    public interface IPortfolioGroupService
    {
    	//Stub functions for the putPortfolioGroups operation
    	/**
    	 * Call the operation on the server passing in the arguments defined in the WSDL file
    	 * @param PortfolioGroups
    	 * @param putPortfolioGroups
    	 * @return An AsyncToken
    	 */
    	function putPortfolioGroups(putPortfolioGroups:PutPortfolioGroups):AsyncToken;
        /**
         * Method to call the operation on the server without passing the arguments inline.
         * You must however set the _request property for the operation before calling this method
         * Should use it in MXML context mostly
         * @return An AsyncToken
         */
        function putPortfolioGroups_send():AsyncToken;
        
        /**
         * The putPortfolioGroups operation lastResult property
         */
        function get putPortfolioGroups_lastResult():PutPortfolioGroupsResponse;
		/**
		 * @private
		 */
        function set putPortfolioGroups_lastResult(lastResult:PutPortfolioGroupsResponse):void;
       /**
        * Add a listener for the putPortfolioGroups operation successful result event
        * @param The listener function
        */
       function addputPortfolioGroupsEventListener(listener:Function):void;
       
       
        /**
         * The putPortfolioGroups operation request wrapper
         */
        function get putPortfolioGroups_request_var():PutPortfolioGroups_request;
        
        /**
         * @private
         */
        function set putPortfolioGroups_request_var(request:PutPortfolioGroups_request):void;
                   
    	//Stub functions for the getPortfolioGroupList operation
    	/**
    	 * Call the operation on the server passing in the arguments defined in the WSDL file
    	 * @param getPortfolioGroupList
    	 * @param PortfolioGroupIds
    	 * @return An AsyncToken
    	 */
    	function getPortfolioGroupList(getPortfolioGroupList:GetPortfolioGroupList):AsyncToken;
        /**
         * Method to call the operation on the server without passing the arguments inline.
         * You must however set the _request property for the operation before calling this method
         * Should use it in MXML context mostly
         * @return An AsyncToken
         */
        function getPortfolioGroupList_send():AsyncToken;
        
        /**
         * The getPortfolioGroupList operation lastResult property
         */
        function get getPortfolioGroupList_lastResult():GetPortfolioGroupListResponse;
		/**
		 * @private
		 */
        function set getPortfolioGroupList_lastResult(lastResult:GetPortfolioGroupListResponse):void;
       /**
        * Add a listener for the getPortfolioGroupList operation successful result event
        * @param The listener function
        */
       function addgetPortfolioGroupListEventListener(listener:Function):void;
       
       
        /**
         * The getPortfolioGroupList operation request wrapper
         */
        function get getPortfolioGroupList_request_var():GetPortfolioGroupList_request;
        
        /**
         * @private
         */
        function set getPortfolioGroupList_request_var(request:GetPortfolioGroupList_request):void;
                   
    	//Stub functions for the getAllPortfolioGroups operation
    	/**
    	 * Call the operation on the server passing in the arguments defined in the WSDL file
    	 * @param getAllPortfolioGroups
    	 * @return An AsyncToken
    	 */
    	function getAllPortfolioGroups(getAllPortfolioGroups:GetAllPortfolioGroups):AsyncToken;
        /**
         * Method to call the operation on the server without passing the arguments inline.
         * You must however set the _request property for the operation before calling this method
         * Should use it in MXML context mostly
         * @return An AsyncToken
         */
        function getAllPortfolioGroups_send():AsyncToken;
        
        /**
         * The getAllPortfolioGroups operation lastResult property
         */
        function get getAllPortfolioGroups_lastResult():GetAllPortfolioGroupsResponse;
		/**
		 * @private
		 */
        function set getAllPortfolioGroups_lastResult(lastResult:GetAllPortfolioGroupsResponse):void;
       /**
        * Add a listener for the getAllPortfolioGroups operation successful result event
        * @param The listener function
        */
       function addgetAllPortfolioGroupsEventListener(listener:Function):void;
       
       
        /**
         * The getAllPortfolioGroups operation request wrapper
         */
        function get getAllPortfolioGroups_request_var():GetAllPortfolioGroups_request;
        
        /**
         * @private
         */
        function set getAllPortfolioGroups_request_var(request:GetAllPortfolioGroups_request):void;
                   
        /**
         * Get access to the underlying web service that the stub uses to communicate with the server
         * @return The base service that the facade implements
         */
        function getWebService():BasePortfolioGroupService;
	}
}