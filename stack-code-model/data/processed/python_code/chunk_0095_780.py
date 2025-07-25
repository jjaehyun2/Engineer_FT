/**
 * User: Mateusz Skafiriak :: mateusz.skafiriak@gmail.com
 * Date: 24.01.13
 * Time: 21:29
 */
package pl.onthemoon.starEngine.input {

import flash.utils.Dictionary;

import starling.core.Starling;
import starling.events.KeyboardEvent;

public class KeyboardController extends Controller {

	//--------------------------------------------------------------------------
	//   PROPERTIES
	//--------------------------------------------------------------------------

	protected var _controlMap:Dictionary;
	protected var _press:Vector.<int> = new Vector.<int>();
	protected var _push:Vector.<Boolean> = new Vector.<Boolean>(256);
	protected var _release:Vector.<int> = new Vector.<int>();
	protected var _pressNum:int;
	protected var _releaseNum:int;

	//--------------------------------------------------------------------------
	//   CONSTRUCTOR
	//--------------------------------------------------------------------------

	public function KeyboardController() {
		_controlMap = new Dictionary();
	}

	//--------------------------------------------------------------------------
	//   METHODS - public
	//--------------------------------------------------------------------------

	override public function connect():void {
		if (_isConnected)
			return;

		Starling.current.stage.addEventListener(KeyboardEvent.KEY_DOWN, onKeyDown);
		Starling.current.stage.addEventListener(KeyboardEvent.KEY_UP, onKeyUp);

		super.connect();
	}

	override public function disconnect():void {
		if (!_isConnected)
			return;

		Starling.current.stage.removeEventListener(KeyboardEvent.KEY_DOWN, onKeyDown);
		Starling.current.stage.removeEventListener(KeyboardEvent.KEY_UP, onKeyUp);

		super.disconnect();
	}

	//--------------------------------------------------------------------------
	//--------------------------------------------------------------------------

	public function defineActionIdMapping(actionId:String, keys:Array = null):void {
		_controlMap[actionId] = keys;
	}

	//--------------------------------------------------------------------------
	//--------------------------------------------------------------------------

	public function isPressed(actionId:String):Boolean {
		if (!_isConnected || !_controlMap[actionId])
			return false;

		var keys:Array = _controlMap[actionId];
		var i:int = keys.length;
		while (i--) {
			if (_press.indexOf(keys[i]) >= 0)
				return true;
		}

		return false;
	}

	public function isPushed(actionId:String):Boolean {
		if (!_isConnected || !_controlMap[actionId])
			return false;

		var keys:Array = _controlMap[actionId];
		var i:int = keys.length;
		while (i--) {
			if (_push[keys[i]])
				return true;
		}

		return false;
	}

	public function isReleased(actionId:String):Boolean {
		if (!_isConnected)
			return false;

		var keys:Array = _controlMap[actionId];
		var i:int = keys.length;
		while (i--) {
			if (_release.indexOf(keys[i]) >= 0)
				return true;
		}

		return false;
	}

	//--------------------------------------------------------------------------
	//   METHODS - protected
	//--------------------------------------------------------------------------

	protected function onKeyDown(e:KeyboardEvent):void {
		var keyCode:uint = e.keyCode;
		if (keyCode < 0 || keyCode > 255) return;
		if (!_push[keyCode]) {
			_push[keyCode] = true;
			_press[_pressNum++] = keyCode;
		}
	}

	protected function onKeyUp(e:KeyboardEvent):void {
		var keyCode:uint = e.keyCode;
		if (keyCode < 0 || keyCode > 255) return;
		if (_push[keyCode]) {
			_push[keyCode] = false;
			_release[_releaseNum++] = keyCode;
		}
	}

	//--------------------------------------------------------------------------
	//   METHODS - internal
	//--------------------------------------------------------------------------

	override internal function clear():void {
		super.clear();

		_pressNum = 0;
		_releaseNum = 0;
		_press.length = 0;
		_release.length = 0;
	}

	//--------------------------------------------------------------------------
	//--------------------------------------------------------------------------
	//--------------------------------------------------------------------------

	/*public static const BACKSPACE:uint = 8;
	public static const TAB:uint = 9;
	public static const ENTER:uint = 13;
	public static const SHIFT:uint = 16;
	public static const CTRL:uint = 17;
	public static const CAPS_LOCK:uint = 20;
	public static const ESCAPE:uint = 27;
	public static const SPACE:uint = 32;

	public static const A:uint = 65;
	public static const B:uint = 66;
	public static const C:uint = 67;
	public static const D:uint = 68;
	public static const E:uint = 69;
	public static const F:uint = 70;
	public static const G:uint = 71;
	public static const H:uint = 72;
	public static const I:uint = 73;
	public static const J:uint = 74;
	public static const K:uint = 75;
	public static const L:uint = 76;
	public static const M:uint = 77;
	public static const N:uint = 78;
	public static const O:uint = 79;
	public static const P:uint = 80;
	public static const Q:uint = 81;
	public static const R:uint = 82;
	public static const S:uint = 83;
	public static const T:uint = 84;
	public static const U:uint = 85;
	public static const V:uint = 86;
	public static const W:uint = 87;
	public static const X:uint = 88;
	public static const Y:uint = 89;
	public static const Z:uint = 90;

	public static const NUMBER_0:uint = 48;
	public static const NUMBER_1:uint = 49;
	public static const NUMBER_2:uint = 50;
	public static const NUMBER_3:uint = 51;
	public static const NUMBER_4:uint = 52;
	public static const NUMBER_5:uint = 53;
	public static const NUMBER_6:uint = 54;
	public static const NUMBER_7:uint = 55;
	public static const NUMBER_8:uint = 56;
	public static const NUMBER_9:uint = 57;

	public static const LEFT:uint = 37;
	public static const UP:uint = 38;
	public static const RIGHT:uint = 39;
	public static const DOWN:uint = 40;

	public static const INSERT:uint = 45;
	public static const DELETE:uint = 46;
	public static const PAGE_UP:uint = 33;
	public static const PAGE_DOWN:uint = 34;
	public static const END:uint = 35;
	public static const HOME:uint = 36;

	public static const BREAK:uint = 19;
	public static const NUM_LOCK:uint = 144;
	public static const SCROLL_LOCK:uint = 145;

	public static const NUMPAD_0:uint = 96;
	public static const NUMPAD_1:uint = 97;
	public static const NUMPAD_2:uint = 98;
	public static const NUMPAD_3:uint = 99;
	public static const NUMPAD_4:uint = 100;
	public static const NUMPAD_5:uint = 101;
	public static const NUMPAD_6:uint = 102;
	public static const NUMPAD_7:uint = 103;
	public static const NUMPAD_8:uint = 104;
	public static const NUMPAD_9:uint = 105;

	public static const NUMPAD_MULTIPLY:uint = 105;
	public static const NUMPAD_ADD:uint = 107;
	public static const NUMPAD_ENTER:uint = 13;
	public static const NUMPAD_SUBSTRACT:uint = 109;
	public static const NUMPAD_DECIMAL:uint = 110;
	public static const NUMPAD_DIVIDE:uint = 111;

	public static const F1:uint = 112;
	public static const F2:uint = 113;
	public static const F3:uint = 114;
	public static const F4:uint = 115;
	public static const F5:uint = 116;
	public static const F6:uint = 117;
	public static const F7:uint = 118;
	public static const F8:uint = 119;
	public static const F9:uint = 120;
	public static const F10:uint = 121;
	public static const F11:uint = 122;
	public static const F12:uint = 123;
	public static const F13:uint = 124;
	public static const F14:uint = 125;
	public static const F15:uint = 126;

	public static const COMMAND:uint = 15;
	public static const ALTERNATE:uint = 18;

	public static const BACKQUOTE:uint = 192;
	public static const QUOTE:uint = 222;
	public static const COMMA:uint = 188;
	public static const PERIOD:uint = 190;
	public static const SEMICOLON:uint = 186;
	public static const BACKSLASH:uint = 220;
	public static const SLASH:uint = 191;

	public static const EQUAL:uint = 187;
	public static const MINUS:uint = 189;

	public static const LEFT_BRACKET:uint = 219;
	public static const RIGHT_BRACKET:uint = 221;*/

	//--------------------------------------------------------------------------
	//--------------------------------------------------------------------------
	//--------------------------------------------------------------------------
}
}