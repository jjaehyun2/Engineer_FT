/**
 * Extended Adam Atomic's "Keyboard" to support listening to mouse down and up.
 * Useful to call justPressed("MOUSE");
 * - Ethan Kennerly
 */
package org.flixel.system.input {
	import flash.display.DisplayObject;
	import flash.display.Stage;
	import flash.events.KeyboardEvent;
	import flash.events.MouseEvent;

	/**
	 * Keeps track of what keys are pressed and how with handy booleans or strings.
	 * 
	 * @author Adam Atomic
	 */
	public class KeyMouse extends Input {
		public var ESCAPE : Boolean;
		public var F1 : Boolean;
		public var F2 : Boolean;
		public var F3 : Boolean;
		public var F4 : Boolean;
		public var F5 : Boolean;
		public var F6 : Boolean;
		public var F7 : Boolean;
		public var F8 : Boolean;
		public var F9 : Boolean;
		public var F10 : Boolean;
		public var F11 : Boolean;
		public var F12 : Boolean;
		public var ONE : Boolean;
		public var TWO : Boolean;
		public var THREE : Boolean;
		public var FOUR : Boolean;
		public var FIVE : Boolean;
		public var SIX : Boolean;
		public var SEVEN : Boolean;
		public var EIGHT : Boolean;
		public var NINE : Boolean;
		public var ZERO : Boolean;
		public var NUMPADONE : Boolean;
		public var NUMPADTWO : Boolean;
		public var NUMPADTHREE : Boolean;
		public var NUMPADFOUR : Boolean;
		public var NUMPADFIVE : Boolean;
		public var NUMPADSIX : Boolean;
		public var NUMPADSEVEN : Boolean;
		public var NUMPADEIGHT : Boolean;
		public var NUMPADNINE : Boolean;
		public var NUMPADZERO : Boolean;
		public var PAGEUP : Boolean;
		public var PAGEDOWN : Boolean;
		public var HOME : Boolean;
		public var END : Boolean;
		public var INSERT : Boolean;
		public var MINUS : Boolean;
		public var NUMPADMINUS : Boolean;
		public var PLUS : Boolean;
		public var NUMPADPLUS : Boolean;
		public var DELETE : Boolean;
		public var BACKSPACE : Boolean;
		public var TAB : Boolean;
		public var Q : Boolean;
		public var W : Boolean;
		public var E : Boolean;
		public var R : Boolean;
		public var T : Boolean;
		public var Y : Boolean;
		public var U : Boolean;
		public var I : Boolean;
		public var O : Boolean;
		public var P : Boolean;
		public var LBRACKET : Boolean;
		public var RBRACKET : Boolean;
		public var BACKSLASH : Boolean;
		public var CAPSLOCK : Boolean;
		public var A : Boolean;
		public var S : Boolean;
		public var D : Boolean;
		public var F : Boolean;
		public var G : Boolean;
		public var H : Boolean;
		public var J : Boolean;
		public var K : Boolean;
		public var L : Boolean;
		public var SEMICOLON : Boolean;
		public var QUOTE : Boolean;
		public var ENTER : Boolean;
		public var SHIFT : Boolean;
		public var Z : Boolean;
		public var X : Boolean;
		public var C : Boolean;
		public var V : Boolean;
		public var B : Boolean;
		public var N : Boolean;
		public var M : Boolean;
		public var COMMA : Boolean;
		public var PERIOD : Boolean;
		public var NUMPADPERIOD : Boolean;
		public var SLASH : Boolean;
		public var NUMPADSLASH : Boolean;
		public var CONTROL : Boolean;
		public var ALT : Boolean;
		public var SPACE : Boolean;
		public var UP : Boolean;
		public var DOWN : Boolean;
		public var LEFT : Boolean;
		public var RIGHT : Boolean;
		public var MOUSE : Boolean;
		public var MOUSE_CODE : uint = 255;
		public var target:DisplayObject;
		private var stage:Stage;

		public function KeyMouse() {
			var i : uint;

			// LETTERS
			i = 65;
			while (i <= 90)
				addKey(String.fromCharCode(i), i++);

			// NUMBERS
			i = 48;
			addKey("ZERO", i++);
			addKey("ONE", i++);
			addKey("TWO", i++);
			addKey("THREE", i++);
			addKey("FOUR", i++);
			addKey("FIVE", i++);
			addKey("SIX", i++);
			addKey("SEVEN", i++);
			addKey("EIGHT", i++);
			addKey("NINE", i++);
			i = 96;
			addKey("NUMPADZERO", i++);
			addKey("NUMPADONE", i++);
			addKey("NUMPADTWO", i++);
			addKey("NUMPADTHREE", i++);
			addKey("NUMPADFOUR", i++);
			addKey("NUMPADFIVE", i++);
			addKey("NUMPADSIX", i++);
			addKey("NUMPADSEVEN", i++);
			addKey("NUMPADEIGHT", i++);
			addKey("NUMPADNINE", i++);
			addKey("PAGEUP", 33);
			addKey("PAGEDOWN", 34);
			addKey("HOME", 36);
			addKey("END", 35);
			addKey("INSERT", 45);

			// FUNCTION KEYS
			i = 1;
			while (i <= 12)
				addKey("F" + i, 111 + (i++));

			// SPECIAL KEYS + PUNCTUATION
			addKey("ESCAPE", 27);
			addKey("MINUS", 189);
			addKey("NUMPADMINUS", 109);
			addKey("PLUS", 187);
			addKey("NUMPADPLUS", 107);
			addKey("DELETE", 46);
			addKey("BACKSPACE", 8);
			addKey("LBRACKET", 219);
			addKey("RBRACKET", 221);
			addKey("BACKSLASH", 220);
			addKey("CAPSLOCK", 20);
			addKey("SEMICOLON", 186);
			addKey("QUOTE", 222);
			addKey("ENTER", 13);
			addKey("SHIFT", 16);
			addKey("COMMA", 188);
			addKey("PERIOD", 190);
			addKey("NUMPADPERIOD", 110);
			addKey("SLASH", 191);
			addKey("NUMPADSLASH", 191);
			addKey("CONTROL", 17);
			addKey("ALT", 18);
			addKey("SPACE", 32);
			addKey("UP", 38);
			addKey("DOWN", 40);
			addKey("LEFT", 37);
			addKey("RIGHT", 39);
			addKey("TAB", 9);
			addKey("MOUSE", MOUSE_CODE);
		}

		/**
		 * Event handler so FlxGame can toggle keys.
		 * 
		 * @param	FlashEvent	A <code>KeyboardEvent</code> object.
		 */
		public function handleKeyDown(FlashEvent : KeyboardEvent) : void {
			handleDown(FlashEvent.keyCode);
        }

		private function handleDown(keyCode:uint) : void {
			var object : Object = _map[keyCode];
			if (object == null) return;
			if (object.current > 0) object.current = 1;
			else object.current = 2;
			this[object.name] = true;
		}

		/**
		 * Event handler so FlxGame can toggle keys.
		 * 
		 * @param	FlashEvent	A <code>KeyboardEvent</code> object.
		 */
		public function handleKeyUp(FlashEvent : KeyboardEvent) : void {
			handleUp(FlashEvent.keyCode);
        }

		private function handleUp(keyCode:uint) : void {
			var object : Object = _map[keyCode];
			if (object == null) return;
			if (object.current > 0) object.current = -1;
			else object.current = 0;
			this[object.name] = false;
		}

		/**
		 * Event handler so FlxGame can update the mouse.
		 * 
		 * @param	FlashEvent	A <code>MouseEvent</code> object.
		 */
		public function handleMouseDown(FlashEvent : MouseEvent) : void {
            target = FlashEvent.target as DisplayObject;
            handleDown(MOUSE_CODE);
		}

		/**
		 * Event handler so FlxGame can update the mouse.
		 * 
		 * @param	FlashEvent	A <code>MouseEvent</code> object.
		 */
		public function handleMouseUp(FlashEvent : MouseEvent) : void {
            target = FlashEvent.target as DisplayObject;
            handleUp(MOUSE_CODE);
		}

		public function listen(stage:Stage) : void {
            this.stage = stage;
            stage.addEventListener(KeyboardEvent.KEY_DOWN, handleKeyDown, false, 0, true);
            stage.addEventListener(KeyboardEvent.KEY_UP, handleKeyUp, false, 0, true);
            stage.addEventListener(MouseEvent.MOUSE_DOWN, handleMouseDown, false, 0, true);
            stage.addEventListener(MouseEvent.MOUSE_UP, handleMouseUp, false, 0, true);
        }

        /**
         * Remove focus to allow keyboard input after a mouse click.
         * Not compatible with text fields.
         */
		override public function update() : void {
            if (stage.focus && stage.focus != stage && !stage.focus.stage) {
                stage.focus = null;
            }
            super.update();
        }
	}
}