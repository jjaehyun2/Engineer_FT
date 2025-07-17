package com.adrienheisch.spacewar.utils
{
	import com.adrienheisch.spacewar.Main;
	import flash.display.Stage;
	import flash.events.KeyboardEvent;
	
	/**
	 * ...
	 * @author Adrien Heisch
	 */
	public class KeyboardManager
	{
		
		protected static var stage:Stage;
		
		public static var keys:Vector.<uint> = new Vector.<uint>();
		
		public static function init():void
		{
			stage = Main.instance.stage;
			
			stage.addEventListener(KeyboardEvent.KEY_DOWN, registerKey);
			stage.addEventListener(KeyboardEvent.KEY_UP, unregisterKey);
		}
		
		protected static function registerKey(pEvent:KeyboardEvent):void
		{
			if (keys.indexOf(pEvent.keyCode) < 0) keys.push(pEvent.keyCode);
		}
		
		protected static function unregisterKey(pEvent:KeyboardEvent):void
		{
			keys.splice(keys.indexOf(pEvent.keyCode), 1);
		}
	
	}

}