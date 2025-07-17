package com.illuzor.circles.tools {
	
	import flash.display.Stage;
	import flash.events.KeyboardEvent;
	import flash.ui.Keyboard;

	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class KeyboardManager {
		
		private static var stage:Stage;
		private static var func:Function;
		
		public static function init(stage:Stage):void {
			KeyboardManager.stage = stage;
			stage.addEventListener(KeyboardEvent.KEY_DOWN, onKeyDown);
		}
		
		private static function onKeyDown(e:KeyboardEvent):void {
			if (e.keyCode == Keyboard.BACK || e.keyCode == Keyboard.BACKSPACE) {
				if (func) {
					e.preventDefault();
					func();
				}
			}
		}
		
		public static function setFunction(func:Function):void {
			KeyboardManager.func = func;
		}
		
		public static function removeFunc():void {
			func = null;
		}
		
	}
}