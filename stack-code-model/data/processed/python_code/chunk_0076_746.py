package com.illuzor.engine3d.events {
	
	import flash.events.Event;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	
	public class MenuEvent extends Event {
		
		static public const SHOW_INFO:String = "showInfo";
		static public const SHOW_MODELS_MENU:String = "showModelMenu";
		static public const SELECT_MODEL:String = "selectModel";
		
		public function MenuEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false) { 
			super(type, bubbles, cancelable);
		} 
		
		public override function clone():Event { 
			return new MenuEvent(type, bubbles, cancelable);
		} 
		
		public override function toString():String { 
			return formatToString("MenuEvent", "type", "bubbles", "cancelable", "eventPhase"); 
		}	
	}
}