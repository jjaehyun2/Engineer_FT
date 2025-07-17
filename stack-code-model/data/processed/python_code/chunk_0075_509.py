package com.illuzor.thegame.events {
	import flash.events.Event;
	
	/**
	 * ...
	 * @author illuzor // illuzor.com // illuzor@gmail.com
	 */
	public class LibEvent extends Event {
		
		public static const LIB_LOADED:String = "libLoaded";
		
		public function LibEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false) { 
			super(type, bubbles, cancelable);
			
		} 
		
		public override function clone():Event { 
			return new LibEvent(type, bubbles, cancelable);
		} 
		
		public override function toString():String { 
			return formatToString("LibEvent", "type", "bubbles", "cancelable", "eventPhase"); 
		}
		
	}
}