/*
Copyright (c) 2007, Yahoo! Inc. All rights reserved.
Code licensed under the BSD License:
http://developer.yahoo.net/yui/license.txt
version: 2.2.0
*/
package com.yahoo.webapis.maps {
	
	import com.yahoo.webapis.maps.utils.ExternalInterfaceBuffer;
	import com.yahoo.webapis.maps.events.MapEvent;
	import flash.display.Loader;
	import flash.external.ExternalInterface;
	import flash.geom.Rectangle;
	import mx.controls.SWFLoader;
	import mx.core.mx_internal;
	import flash.events.Event;
	import flash.events.EventDispatcher;
	import flash.utils.getTimer;
	
	//use namespace mx_internal;
	
	/**
	 * UIComponent designed specifically to load Yahoo Maps swfs into flex 2/as3 environments.
	 * This class extends mx.controls.SWFLoader.
	 * 
	 * @langversion ActionScript 3.0
	 * @playerversion Flash 9
	 * @author Scott Morgan 02/25/2007
	 * 
	 * @see mx.controls.SWFLoader
	*/
	public class YahooMapService extends SWFLoader {
		
		/**
		 * @private
		 * Access to ExternalInterfaceBuffer class which proxies methods passed to the AS2 map
		 * 
		 * @see com.yahoo.webapis.utils.ExternalInterfaceBuffer
		 */
		private var EIBuffer:ExternalInterfaceBuffer;//
		/** 
		 * Your Yahoo API App ID. If you don't have one get one here:
		 * for communication purposes.
		 */
		private var _apiId:String;		
		public function set apiId(id:String):void {
			_apiId = id;
		}
		public function get apiId():String {
			return _apiId;
		}
		
		/** 
		 * The id of the YahooMapService.swf proxy that will be used
		 * for communication purposes.
		 */
		private var _UUID:int;
		public function set UUID(id:int):void {
			_UUID = id;
			//keep for when LocalConnection communication is set up.
			//EIBuffer = ExternalInterfaceBuffer.getInstance('local', id);
			EIBuffer = ExternalInterfaceBuffer.getInstance();
		}
		public function get UUID():int {
			return _UUID;
		}
		
		/**
		 * The name of the application that is loading in the YahooMapService.swf
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
		
		/**
		 * The filename and path of the map swf that will be loaded into the
		 * Flex or AS3 application.
		 */
		private var _mapURL:String;
		public function set mapURL(map:String):void {
			_mapURL = map;
		}
		public function get mapURL():String {
			return _mapURL;
		}
		
		function YahooMapService():void {
			super();
		}
	
		/**
		 * @internal
		 * Override the swfLoader commitProperties method, it is the last method called 
		 * when the swfLoader component is fully instantiated. Once it is loaded call 
		 * the draw() method to get things started.
		 */
		override protected function commitProperties():void { 
			super.commitProperties();
			this.draw();
		}
		
		/**
		 * @private
		 * Method that kicks off everything and sets up listeners to notify us when the 
		 * map is loaded or if there was an error loading it. Meta data is passed through 
		 * to the loaded swf via the querystring. This data is used for communication between
		 * the two virtual machines.
		 */
		private function draw():void {
			// Add event listeners to know when the map is ready
			ExternalInterface.addCallback("onLoadError" + UUID, onLoadError );
			ExternalInterface.addCallback("onLoadInit" + UUID, onLoadInit );
			
			// Pull in the YahooMap swf from the server using the YahooMapService swf proxy
			this.source = mapURL + "?&swfDomId=" + swfDomId + "&id=" + UUID + "&url=" + escape( mapURL );
		}
		
		/**
		 * @private
		 * Event triggered when the map is loaded and ready to go.
		 */
		private function onLoadInit(ev:Object):void {
			//set up map id
			EIBuffer.addCall({method:swfDomId + '.setApiId' + UUID, data:_apiId})
			EIBuffer.addCall({method:swfDomId + ".setMapSize" + UUID, data:{w:super.width,h:super.height}});
			dispatchEvent(new MapEvent('onMapLoad', ev));
		}
		
		/**
		 * @private
		 * Event triggered when there is an error loading the map swf.
		 */
		private function onLoadError(errorCode:String, httpStatus:String):void {
			dispatchEvent(new MapEvent('onMapError', errorCode));
		}
		
	} 
}