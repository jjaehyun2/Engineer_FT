package com.illuzor.otherside.editor.events {
	
	import flash.events.Event;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class ScreenEvent extends Event {
		
		private var _screenType:String;
		private var _levelData:Object;
		
		public static const SCHANGE_SCREEN:String = "changeScreen";
		
		public function ScreenEvent(type:String, screenType:String, levelData:Object = null) { 
			super(type, true);
			_levelData = levelData;
			_screenType = screenType;
		} 
		
		public function get screenType():String {
			return _screenType;
		}
		
		public function get levelData():Object {
			return _levelData;
		}
		
	}
}