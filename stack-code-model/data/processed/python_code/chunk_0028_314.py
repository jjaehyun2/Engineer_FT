/*
** Source code Copyright 2006, Andrew Rapo
** May be used in non-commercial and commercial applications
** as long as the author is credited
*/

package org.rapo.games.astro.managers  {
	
	import flash.display.MovieClip;
	import flash.display.Stage;
	import flash.events.KeyboardEvent;
	import flash.ui.Keyboard;
	//import flash.utils.Proxy;
	//import flash.utils.flash_proxy;
	
	public class InputManager {
		
		public static var stage:Stage;
		public static var QUIT:Number = 0;
		public static var ROTATE_LEFT:Number = 1;
		public static var ROTATE_RIGHT:Number = 2;
		public static var FORWARD:Number =3;
		public static var BACK:Number = 4;
		public static var SHOOT:Number = 5;
		public static var SUPER_SHOOT:Number = 6;
		public static var USE_POWERUP:Number = 7;
		public static var SHIELD:Number = 8;
		public static var XTRA:Number = 9;
		public static var NUM_STATES:Number = 10;
		public static var keyMap:Array = new Array(NUM_STATES);
		public static var inputState:Array = new Array(NUM_STATES);
		
		public static var keyMapInitialized:Boolean = initKeymap();
		public static var keysDown:Object;
		
		public static function init(game_stage:Stage):void
		{
			stage = game_stage;
			keysDown = new Object();
			stage.addEventListener(KeyboardEvent.KEY_DOWN, keyDown);
			stage.addEventListener(KeyboardEvent.KEY_UP, keyUp);
		}
		
		public static function isDown(keyCode:uint):Boolean
		{
			return Boolean(keysDown[keyCode]);
		}
		
		public static function keyDown(event:KeyboardEvent):void
		{
			keysDown[event.keyCode] = true;
		}
		
		public static function keyUp(event:KeyboardEvent):void
		{
			delete keysDown[event.keyCode];
		}
		
		public static function initKeymap():Boolean {
			
			keyMap[QUIT]			= 81; //Q
			keyMap[ROTATE_LEFT]		= Keyboard.LEFT;
			keyMap[ROTATE_RIGHT]	= Keyboard.RIGHT;
			keyMap[FORWARD]			= Keyboard.UP;
			keyMap[BACK]			= Keyboard.DOWN;
			keyMap[SHOOT]			= Keyboard.SPACE;
			keyMap[SUPER_SHOOT]		= 88; //X
			keyMap[USE_POWERUP]		= Keyboard.SHIFT;
			keyMap[SHIELD]			= 83; //S
			keyMap[XTRA]			= 88; //X
			
			inputState[QUIT]			= false;
			inputState[ROTATE_LEFT]		= false;
			inputState[ROTATE_RIGHT]	= false;
			inputState[FORWARD] 		= false;
			inputState[BACK] 			= false;
			inputState[SHOOT]			= false;
			inputState[SUPER_SHOOT]		= false;
			inputState[USE_POWERUP]		= false;
			inputState[SHIELD]			= false;
			inputState[XTRA]			= false;
	
			return true;
		}
			
		public static function processInput():void{
			
			if (!keyMapInitialized) keyMapInitialized = initKeymap();
			processKeyboardInput();
		}
		
		public static function processKeyboardInput():void {
			
			inputState[QUIT] 			= isDown(keyMap[QUIT]);
			inputState[ROTATE_LEFT]		= isDown(keyMap[ROTATE_LEFT]);
			inputState[ROTATE_RIGHT]	= isDown(keyMap[ROTATE_RIGHT]);
			inputState[FORWARD]			= isDown(keyMap[FORWARD]);
			inputState[BACK]			= isDown(keyMap[BACK]);
			inputState[SHOOT]			= isDown(keyMap[SHOOT]);
			inputState[SUPER_SHOOT]		= isDown(keyMap[SUPER_SHOOT]);
			inputState[USE_POWERUP]		= isDown(keyMap[USE_POWERUP]);
			inputState[SHIELD]			= isDown(keyMap[SHIELD]);
			inputState[XTRA]			= isDown(keyMap[XTRA]);
		}
		
		public static function checkInputState(keyMapIndex):Boolean {
			
			return inputState[keyMapIndex];
		}
	
	/*
		Key.BACKSPACE  The key code value for the Backspace key. 8
		Key.CAPSLOCK  The key code value for the Caps Lock key. 20
		Key.CONTROL  The key code value for the Control key. 17
		Key.DELETEKEY  The key code value for the Delete key. 46
		Key.DOWN  The key code value for the Down Arrow key. 40
		Key.END  The key code value for the End key. 35
		Key.ENTER  The key code value for the Enter key. 13
		Key.ESCAPE  The key code value for the Escape key. 27
		Key.HOME  The key code value for the Home key. 36
		Key.INSERT  The key code value for the Insert key. 45
		Key.LEFT  The key code value for the Left Arrow key. 37
		Key.PGDN  The key code value for the Page Down key. 34
		Key.PGUP  The key code value for the Page Up key. 33
		Key.RIGHT  The key code value for the Right Arrow key. 39
		Key.SHIFT  The key code value for the Shift key. 16
		Key.SPACE  The key code value for the Spacebar. 32
		Key.TAB  The key code value for the Tab key. 9
		Key.UP  The key code value for the Up Arrow key. 38
	*/
	
	}
}