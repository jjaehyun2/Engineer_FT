package com.illuzor.otherside.editor.events {
	
	import flash.events.Event;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class ComponentEvent extends Event {
		
		public static const CHANGE_VALUE:String = "changeValue";
		
		private var _eventData:Object;
		
		public function ComponentEvent(type:String, eventData:Object) { 
			super(type, true);
			_eventData = eventData;
		} 
		
		public function get eventData():Object {
			return _eventData;
		}
		
	}
}