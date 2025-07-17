/*
Copyright (c) 2007, Yahoo! Inc. All rights reserved.
Code licensed under the BSD License:
http://developer.yahoo.net/yui/license.txt
version: 2.2.0
*/
package com.yahoo.webapis.weather.events
{
	import flash.events.Event;
	
	/**
	* Error Event class in response to data events from the Yahoo! Weather API.
	* 
	* @langversion ActionScript 3.0
	* @playerversion Flash 9
	* @author Allen Rabinovich 02/10/07
	*/
	public class WeatherErrorEvent extends Event
	{
			/**
		* The type of event dispatched when XML data could not be loaded from the server.
		*/	
		public static const XML_LOADING:String = "XMLLoading";
	/**
		* The type of event dispatched when the specified location is invalid.
		*/	
		public static const INVALID_LOCATION:String = "LocInvalid";
		
		/**
		 * True if the event is the result of a successful call,
		 * False if the call failed
		 */
		public var success:Boolean;
		
		private var _data:Object;
		
		/**
		 * Constructs a new WeatherErrorEvent
		 */
		public function WeatherErrorEvent(type:String, inData:Object)
		{
			_data = inData;
									   	
			super( type, bubbles, cancelable );
		}
		
		
		/**
		 * Data
		 */
		public function get data():Object
		{
			return _data;
		}
		
		public function set data( value:Object ):void
		{
			_data = value;
		}
		
	}
	
}