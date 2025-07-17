package com.illuzor.thegame.editor.events {
	
	import flash.events.Event;
	
	/**
	 * ...
	 * @author illuzor // illuzor.com // illuzor@gmail.com
	 */
	
	public class EditorEvent extends Event {
		
		public static const PLAY_LEVEL:String = "playLevel";
		public static const MAIN_MENU:String = "mainMenu";
		
		public function EditorEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false) { 
			super(type, bubbles, cancelable);
		} 
		
		public override function clone():Event { 
			return new EditorEvent(type, bubbles, cancelable);
		} 
		
		public override function toString():String { 
			return formatToString("EditorEvent", "type", "bubbles", "cancelable", "eventPhase"); 
		}
		
	}
}