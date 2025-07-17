package com.illuzor.otherside.events {
	
	import starling.events.Event;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class WeaponEvent extends Event {
		public static const SHOOT:String = "shootEvent";
		
		private var _weaponType:String;
		
		public function WeaponEvent(type:String, weaponType:String) { 
			super(type);
			_weaponType = weaponType;
		} 
		
		public function get weaponType():String {
			return _weaponType;
		}
	}
	
}