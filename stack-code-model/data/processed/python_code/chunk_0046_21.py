package com.illuzor.spinner.events {
	
	import starling.events.Event;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class ControlManagerEvent extends Event {
		
		public static const ROTATE_CW:String = "rotateCW";
		public static const ROTATE_CCW:String = "rotateCCW";
		
		public function ControlManagerEvent(type:String) { 
			super(type);
		} 
		
	}
}