package com.illuzor.leaptest.away3d.events {
	import flash.events.Event;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	public class RotatorEvent extends Event {
		
		public static const ROTATOR_ENDS:String = "rotEnds";
		
		public function RotatorEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false) { 
			super(type, bubbles, cancelable);
		} 
		
		public override function clone():Event { 
			return new RotatorEvent(type, bubbles, cancelable);
		} 
		
		public override function toString():String { 
			return formatToString("RotatorEvent", "type", "bubbles", "cancelable", "eventPhase"); 
		}
		
	}
	
}