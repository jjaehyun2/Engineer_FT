/**
 * GetAdKeyWordStatsResultEvent.as
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
    
    public class GetAdKeyWordStatsResultEvent extends Event
    {
        /**
         * The event type value
         */
        public static var GetAdKeyWordStats_RESULT:String="GetAdKeyWordStats_result";
        /**
         * Constructor for the new event type
         */
        public function GetAdKeyWordStatsResultEvent()
        {
            super(GetAdKeyWordStats_RESULT,false,false);
        }
        
        private var _headers:Object;
        private var _result:GetAdKeyWordStatsResponse;
         public function get result():GetAdKeyWordStatsResponse
        {
            return _result;
        }
        
        public function set result(value:GetAdKeyWordStatsResponse):void
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