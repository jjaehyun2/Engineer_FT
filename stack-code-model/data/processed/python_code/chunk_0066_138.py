package com.illuzor.circles.events {
	
	import starling.events.Event;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class ScreenEvent extends Event {

		public static const CHANGE_SCREEN:String = "changeScreen";
		public static const GOTO_MAIN:String = "gotoMain";
		
		private var _screenType:uint;
		private var _gameType:String;
		
		public function ScreenEvent(type:String, screenType:uint, gameType:String = "") { 
			super(type, true);
			this._gameType = gameType;
			this._screenType = screenType;
		} 
		
		public function get screenType():uint {
			return _screenType;
		}
		
		public function get gameType():String {
			return _gameType;
		}
		
	}
}