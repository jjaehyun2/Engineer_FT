/*
Copyright (c) 2007, Yahoo! Inc. All rights reserved.
Code licensed under the BSD License:
http://developer.yahoo.net/yui/license.txt
version: 2.2.0
*/
package com.yahoo.webapis.maps.methodgroups {
	import flash.events.EventDispatcher;
	import flash.events.Event;	
	import flash.external.ExternalInterface;
	import com.yahoo.webapis.maps.events.MapEvent;
	import com.yahoo.webapis.maps.utils.ExternalInterfaceBuffer;
	
	/**
	 * This class currently only contains the getters and setters for
	 * map instance specific data (UUID and swfDomId). I have abstracted
	 * this class for future funtionality and to allow for easy inclusions of
	 * global functionality that spans across all method groups.
	 * 
	 * @langversion ActionScript 3.0
	 * @playerversion Flash 9
	 * @author Scott Morgan 02/25/2007
	*/
	public class AbstractMethod extends EventDispatcher {
		
		/** 
		 * The id of the YahooMapLoader.swf proxy that will be used
		 * for communication purposes.
		 */
		private var _UUID:int;
		
		public function set UUID(id:int):void {
			_UUID = id;
		}
		
		public function get UUID():int {
			return _UUID;
		}
		
		/**
		 * The name of the application that is loading in the YahooMapLoader.swf
		 * file.  This name must correspond to the "id" attribute in the object tag
		 * and the "name" attribute in the embed tag when the Flex client is embedded
		 * into the html page.
		 */
		private var _swfDomId:String;
		
		public function set swfDomId(id:String):void {
			_swfDomId = id;
		}
		
		public function get swfDomId():String {
			return _swfDomId;
		}
		
		private var EIBuffer:ExternalInterfaceBuffer = ExternalInterfaceBuffer.getInstance();
		
		public function AbstractMethod(id:int, domId:String):void {
			UUID = id;
			swfDomId = domId;
		}
		
		
		
		
		
	}
	
}