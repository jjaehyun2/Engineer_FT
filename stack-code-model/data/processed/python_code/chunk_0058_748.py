package com.profusiongames.events 
{
	import starling.events.Event;
	
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class WindowEvent extends Event 
	{
		public static var NAVIGATION:String = "window_navigation";
		private var _windowData:String = "";
		public function WindowEvent(type:String, windowData:String = "") 
		{
			_windowData = windowData;
			super(type);
		}
		
		public function get windowData():String 
		{
			return _windowData;
		}
		
		
	}

}