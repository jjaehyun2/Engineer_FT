/**
 * GetAllCampaignsResultEvent.as
 * This file was auto-generated from WSDL
 * Any change made to this file will be overwritten when the code is re-generated.
*/
package com.macys.marketing.sema
{
    import mx.utils.ObjectProxy;
    import flash.events.Event;
    import flash.utils.ByteArray;
    import mx.rpc.soap.types.*;
    /**
     * Typed event handler for the result of the operation
     */
    
    public class GetAllCampaignsResultEvent extends Event
    {
        /**
         * The event type value
         */
        public static var GetAllCampaigns_RESULT:String="GetAllCampaigns_result";
        /**
         * Constructor for the new event type
         */
        public function GetAllCampaignsResultEvent()
        {
            super(GetAllCampaigns_RESULT,false,false);
        }
        
        private var _headers:Object;
        private var _result:GetAllCampaignsResponse;
         public function get result():GetAllCampaignsResponse
        {
            return _result;
        }
        
        public function set result(value:GetAllCampaignsResponse):void
        {
            _result = value;
        }

        public function get headers():Object
	    {
            return _headers;
	    }
			
	    public function set headers(value:Object):void
	    {
            _headers = value;
	    }
    }
}