package com.illuzor.spinner.events {
	
	import starling.events.Event;

	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class ScreenEvent extends Event {
		
		private var _data:Object;
		private var _screenType:uint;
		
		public static const CHANGE_SCREEN:String = "changeScreen";
		public static const SHOW_SUBSCREEN:String = "showSubscreen";
		public static const SCREEN_HIDED:String = "screenHided";
		
		public function ScreenEvent(type:String, screenType:uint = 0, data:Object = null) { 
			super(type, true);
			this._screenType = screenType;
			this._data = data;
		} 
		
		public function get screenType():uint {
			return _screenType;
		}
		
		override public function get data():Object {
			return _data;
		}
		
	}
}