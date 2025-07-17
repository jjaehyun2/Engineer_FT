/**
 * Service.as
 * This file was auto-generated from WSDL by the Apache Axis2 generator modified by Adobe
 * Any change made to this file will be overwritten when the code is re-generated.
 */
package com.macys.marketing.sema{
	import mx.rpc.AsyncToken;
	import flash.utils.ByteArray;
	import mx.rpc.soap.types.*;
               
    public interface IAccountService
    {
    	//Stub functions for the getAllAccounts operation
    	/**
    	 * Call the operation on the server passing in the arguments defined in the WSDL file
    	 * @param getAllAccounts
    	 * @return An AsyncToken
    	 */
    	function getAllAccounts(getAllAccounts:GetAllAccounts):AsyncToken;
        /**
         * Method to call the operation on the server without passing the arguments inline.
         * You must however set the _request property for the operation before calling this method
         * Should use it in MXML context mostly
         * @return An AsyncToken
         */
        function getAllAccounts_send():AsyncToken;
        
        /**
         * The getAllAccounts operation lastResult property
         */
        function get getAllAccounts_lastResult():GetAllAccountsResponse;
		/**
		 * @private
		 */
        function set getAllAccounts_lastResult(lastResult:GetAllAccountsResponse):void;
       /**
        * Add a listener for the getAllAccounts operation successful result event
        * @param The listener function
        */
       function addgetAllAccountsEventListener(listener:Function):void;
       
       
        /**
         * The getAllAccounts operation request wrapper
         */
        function get getAllAccounts_request_var():GetAllAccounts_request;
        
        /**
         * @private
         */
        function set getAllAccounts_request_var(request:GetAllAccounts_request):void;
                   
        /**
         * Get access to the underlying web service that the stub uses to communicate with the server
         * @return The base service that the facade implements
         */
        function getWebService():BaseAccountService;
	}
}