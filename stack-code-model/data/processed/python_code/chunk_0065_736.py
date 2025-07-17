/*
Copyright (c) 2007, Yahoo! Inc. All rights reserved.
Code licensed under the BSD License:
http://developer.yahoo.net/yui/license.txt
version: 2.2.0
*/
package com.yahoo.webapis.maps.methodgroups {
	
	import com.yahoo.webapis.maps.methodgroups.AbstractMethod;
	import com.yahoo.webapis.maps.YahooMapService;
	import com.yahoo.webapis.maps.utils.ExternalInterfaceBuffer;
	import flash.external.ExternalInterface;
	import flash.events.Event;
	
	/**
	 * This class communicates with the AS2 methods found in the 
	 * com.yahoo.maps.Overlays package. This class extends
	 * the AbstractMethod class which not only is waiting for some 
	 * "totally cool" new functionality but also contains the current 
	 * instances UUID and swfDomId.
	 * 
	 * @langversion ActionScript 3.0
	 * @playerversion Flash 9
	 * @author Scott Morgan 02/25/2007
	 * 
	 * @see com.yahoo.maps.api.flash.AbstractMethod
	 * @see com.yahoo.maps.api.flash.YahooMap
	 * @see com.yahoo.maps.PanTool
	*/
	public class PanTool extends AbstractMethod {

		/**
		 * @private
		 * Access to the singleton ExternalInterfaceBuffer where all cross-AVM
		 * communication occurs.
		 * 
		 * @see com.yahoo.webapis.maps.utils.ExternalInterfaceBuffer
		 */
		private var EIBuffer:ExternalInterfaceBuffer = ExternalInterfaceBuffer.getInstance();
		
		/**
		 * Constructor
		 * 
		 * @param service YahooMapService class that stores instance config data
		 */
		public function PanTool(service:YahooMapService):void {
			super(service.UUID, service.swfDomId);
			
		}
	
		/**
		 * The PanTool allows the user to drag the map around for panning. It also 
		 * allows the user to double click on a position on the map and pan to 
		 * that location.
		 * 
		 * @param bool - A boolean value that determines if the panning will be
		 * enabled (true) or not (false).
		 */ 
		public function setPanTool(bool:Boolean = true):void {
			EIBuffer.addCall({method:super.swfDomId + ".setPanTool" + super.UUID, data:bool});
		}
		
	}
}