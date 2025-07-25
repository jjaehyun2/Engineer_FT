/*
 * Copyright 2017 FreshPlanet
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.freshplanet.ane.AirMoPub {
	
	import flash.events.EventDispatcher;
	import flash.events.StatusEvent;
	import flash.external.ExtensionContext;
	
	/**
	 *
	 */
	public class MoPubRewardVideo extends EventDispatcher {
		
		// --------------------------------------------------------------------------------------//
		//																						 //
		// 									   PUBLIC API										 //
		// 																						 //
		// --------------------------------------------------------------------------------------//
		
		// todo : move to generic ad class
		public static var DID_LOAD:String         = "didLoad";
		public static var DID_FAIL_TO_LOAD:String = "didFailToLoad";
		
		public static var WILL_APPEAR:String    = "willAppear";
		public static var DID_APPEAR:String     = "didAppear";
		public static var WILL_DISAPPEAR:String = "willDisappear";
		public static var DID_DISAPPEAR:String  = "didDisappear";
		
		public static var DID_EXPIRE:String = "didExpire";
		
		public static var DID_RECEIVE_TAP:String = "didReceiveTapEvent";
		
		public static var DID_COMPLETE:String = "didComplete";
		
		public static var DID_FAIL_TO_PLAY:String = "didFailToPlay";
		
		/**
		 *
		 */
		public function get id():String {
			return _id;
		}
		
		/**
		 *
		 */
		public function load():void {
			
			var ret:Object = _context.call("reward_load");
			if (ret is Error)
				throw ret;
		}
		
		/**
		 *
		 */
		public function show():void {
			
			var ret:Object = _context.call("reward_show");
			if (ret is Error)
				throw ret;
		}
		
		/**
		 *
		 */
		public function get isReady():Boolean {
			
			var ret:Object = _context.call("reward_has");
			
			if (ret is Error)
				throw ret;
			
			return ret as Boolean;
		}
		
		/**
		 *
		 */
		public function get data():Object {
			
			var ret:Object = _context.call("reward_data");
			
			if (ret is Error)
				throw ret;
			
			var dataString:String = ret as String;
			var json:Object       = null;
			
			try {
				json = JSON.parse(dataString);
			}
			catch (e:Error) {
			
			}
			
			return json;
		}
		
		// --------------------------------------------------------------------------------------//
		//																						 //
		// 									 	PRIVATE API										 //
		// 																						 //
		// --------------------------------------------------------------------------------------//
		
		private var _context:ExtensionContext;
		private var _id:String;
		
		public function MoPubRewardVideo(context:ExtensionContext, id:String) {
			
			super();
			
			_context = context;
			_id      = id;
			
			_context.addEventListener(StatusEvent.STATUS, _handleStatusEvent);
		}
		
		private function _handleStatusEvent(event:StatusEvent):void {
			this.dispatchEvent(new MoPubEvent(event.code, event.level));
		}
	}
}