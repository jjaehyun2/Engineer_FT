package com.illuzor.otherside.events {
	
	import starling.events.Event;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class WeaponEvent extends Event {
		
		private var _weaponType:uint;
		private var _x:int;
		private var _y:int;
		
		public static const SHOOT:String = "shoot";
		
		public function WeaponEvent(type:String, weaponType:uint, x:int, y:int) { 
			super(type);
			_y = y;
			_x = x;
			_weaponType = weaponType;
		} 
		
		public function get weaponType():uint {
			return _weaponType;
		}
		
		public function get x():int {
			return _x;
		}
		
		public function get y():int {
			return _y;
		}
		
	}
}