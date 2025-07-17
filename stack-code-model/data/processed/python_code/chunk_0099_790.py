package com.illuzor.leaptest.away3d.events {
	import flash.events.Event;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	public class SceneEvent extends Event {
		
		private var _direction:int;
		
		public static const SWYPE:String = "swypeGuest";
		public static const TWO_FINGERS:String = "twoFingers";
		public static const ONE_FINGER:String = "threeFingers";
		public static const OTHER_FINGER:String = "otherFingers";
		
		public function SceneEvent(type:String, direction:int, bubbles:Boolean = false, cancelable:Boolean = false) { 
			_direction = direction;
			super(type, bubbles, cancelable);
		} 
		
		public override function clone():Event { 
			return new SceneEvent(type, _direction, bubbles, cancelable);
		} 
		
		public override function toString():String { 
			return formatToString("SceneEvent", "type", "bubbles", "cancelable", "eventPhase"); 
		}
		
		public function get direction():int {
			return _direction;
		}
		
	}
	
}