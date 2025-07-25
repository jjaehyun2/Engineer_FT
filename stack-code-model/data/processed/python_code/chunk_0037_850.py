/*
Copyright (c) 2007, Yahoo! Inc. All rights reserved.
Code licensed under the BSD License:
http://developer.yahoo.net/yui/license.txt
version: 2.2.0
*/
package com.yahoo.webapis.upcoming
{
	import flash.net.URLRequest;
	import flash.net.URLRequestMethod;
	import flash.net.URLLoader;
	import flash.net.URLVariables;

	import flash.events.Event;
	import flash.events.EventDispatcher;
	import com.yahoo.webapis.upcoming.events.*;
	
	/**
	* Yahoo! Upcoming.org API State Class. This class is used to hold information
	* about states in which Upcoming events take place (for US locations only)
	* 
	* @langversion ActionScript 3.0
	* @playerversion Flash 9
	* @author Allen Rabinovich 02/25/07
	*/
	public class State extends EventDispatcher
	{
		/**
		* Defines the parent UpcomingService for this state (used to access the token and API key)
		*/
		public var parent_service:UpcomingService;
		/**
		* The state's Upcoming.org ID number
		*/		
		public var id:Number;
		/**
		* The state's name
		*/
		public var name:String;
		/**
		* The state's Upcoming.org code
		*/
		public var code:String;
		/**
 		 * State class constructor
 		 * 
 		 * @param _parent_service An UpcomingService with an instantiated token and API key.
 		 * @param _id State's Upcoming.org identification number
 		 * @param _name State's name
 		 * @param _code State's code
 		 */
 		public function State(_parent_service:UpcomingService, _id:Number, _name:String, _code:String) {
 			parent_service = _parent_service;
 			id = _id;
 			name = _name;
 			code = _code;
 		}
 		
 		/**
 		 * This method updates the data fields in the specific instance of State
 		 * by the ID number. If the <code>id</code> property is already filled in,
 		 * then no argument needs to be passed. Otherwise, pass the state's
 		 * Upcoming.org identification number.
 		 * <p>When the update completes, the State class will dispatch an
 		 * <code>UpcomingResultEvent.STATE_GET_INFO</code> event.</p>
 		 * @param _id The state's Upcoming.org identification number, if
 		 * none is filled in.
 		 * 
 		 */ 		
 		public function update(_id:Number = NaN):void {
			if (!isNaN(_id)) {
				id = _id;
			}
			sendQuery("state.getInfo", ("state_id=" + id), UpcomingResultEvent.STATE_GET_INFO, 'GET');
		}
		
		/**
		 * This method is used to send the appropriate REST query and parse
		 * the resulting XML.
		 * @private
		 * @param method Upcoming.org API method that should be called.
		 * @param params Parameters to pass in the REST query.
		 * @param dispatchType Event to dispatch when results are received.
		 * @param methodType Whether to POST or to GET the API request.
		 * 
		 */		
		private function sendQuery(method:String, params:String, dispatchType:String, methodType:String = 'POST') : void {
		
			var sendQuery:String;
			sendQuery = (parent_service.api_URL);
			var queryParams:String;
		
			if(params != null) {
				queryParams = ("api_key=" + parent_service.api_id + "&method=" + method + "&"+params);
			} else {
				queryParams = ("api_key=" + parent_service.api_id + "&method=" + method);
			}
			
			var queryXML:XML;
 			var request:URLRequest = new URLRequest(sendQuery);
 			var variables:URLVariables;
 			if (methodType.toLowerCase() == 'post') {
	 			if(params != null) {
	 				variables = new URLVariables(queryParams);
	            	request.method = URLRequestMethod.POST;
	            	request.data = variables;
	    		}
  			}
  			else if (methodType.toLowerCase() == 'get') {
  				if (params != null) {
  					variables = new URLVariables(queryParams);
	            	request.method = URLRequestMethod.GET;
	            	request.data = variables;
  				}
  			}
  			
			var queryLoader:URLLoader = new URLLoader(request);
			queryLoader.addEventListener("complete", xmlLoaded);
			queryLoader.addEventListener("ioError", xmlError);	
			
			// XML loading result method
			function xmlLoaded(evtObj:Object):void {
				
				var data:Object = new Object();
				var resultNode:XML;
				var resultObject:Object = new Object();
				
				queryXML = new XML(queryLoader.data);
								
				switch(dispatchType) {
					case UpcomingResultEvent.STATE_GET_INFO:
						for each (resultNode in queryXML.children()) {
							id = resultNode.@id;
							name = resultNode.@name;
							code = resultNode.@code;
							data = this;
						}
						dispatchEvent(new UpcomingResultEvent(UpcomingResultEvent.STATE_GET_INFO, this));
						break;
				}
			}
				
			
			function xmlError (evtObj:Object):void {
	        	var error:UpcomingErrorEvent = new UpcomingErrorEvent(UpcomingErrorEvent.XML_LOADING, evtObj);
				dispatchEvent(error);
	        }
	        
		}	
	}
}