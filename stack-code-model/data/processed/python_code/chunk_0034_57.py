/*
 *	Temple Library for ActionScript 3.0
 *	Copyright © MediaMonks B.V.
 *	All rights reserved.
 *	
 *	Redistribution and use in source and binary forms, with or without
 *	modification, are permitted provided that the following conditions are met:
 *	1. Redistributions of source code must retain the above copyright
 *	   notice, this list of conditions and the following disclaimer.
 *	2. Redistributions in binary form must reproduce the above copyright
 *	   notice, this list of conditions and the following disclaimer in the
 *	   documentation and/or other materials provided with the distribution.
 *	3. All advertising materials mentioning features or use of this software
 *	   must display the following acknowledgement:
 *	   This product includes software developed by MediaMonks B.V.
 *	4. Neither the name of MediaMonks B.V. nor the
 *	   names of its contributors may be used to endorse or promote products
 *	   derived from this software without specific prior written permission.
 *	
 *	THIS SOFTWARE IS PROVIDED BY MEDIAMONKS B.V. ''AS IS'' AND ANY
 *	EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 *	WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 *	DISCLAIMED. IN NO EVENT SHALL MEDIAMONKS B.V. BE LIABLE FOR ANY
 *	DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 *	(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 *	LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 *	ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 *	(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 *	SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *	
 *	
 *	Note: This license does not apply to 3rd party classes inside the Temple
 *	repository with their own license!
 */

package temple.utils.keys 
{
	import flash.ui.Keyboard;

	/**
	 * Class contains the keycodes for keys.
	 * 
	 * @author Bas
	 */
	public final class KeyCode 
	{
		// Flash standard Keycodes
		public static const TAB:uint = Keyboard.TAB;
		public static const CAPS_LOCK:uint = Keyboard.CAPS_LOCK;
		public static const SHIFT:uint = Keyboard.SHIFT;
		public static const CONTROL:uint = Keyboard.CONTROL;
		public static const SPACE:uint = Keyboard.SPACE;
		public static const DOWN:uint = Keyboard.DOWN;
		public static const UP:uint = Keyboard.UP;
		public static const LEFT:uint = Keyboard.LEFT;
		public static const RIGHT:uint = Keyboard.RIGHT;
		public static const ESCAPE:uint = Keyboard.ESCAPE;
		public static const F1:uint = Keyboard.F1;
		public static const F2:uint = Keyboard.F2;
		public static const F3:uint = Keyboard.F3;
		public static const F4:uint = Keyboard.F4;
		public static const F5:uint = Keyboard.F5;
		public static const F6:uint = Keyboard.F6;
		public static const F7:uint = Keyboard.F7;
		public static const F8:uint = Keyboard.F8;
		public static const F9:uint = Keyboard.F9;
		public static const F10:uint = Keyboard.F10;
		public static const F11:uint = Keyboard.F11;
		public static const F12:uint = Keyboard.F12;
		public static const F13:uint = Keyboard.F13;
		public static const F14:uint = Keyboard.F14;
		public static const F15:uint = Keyboard.F15;
		public static const INSERT:uint = Keyboard.INSERT;
		public static const HOME:uint = Keyboard.HOME;
		public static const PAGE_UP:uint = Keyboard.PAGE_UP;
		public static const PAGE_DOWN:uint = Keyboard.PAGE_DOWN;
		public static const DELETE:uint = Keyboard.DELETE;
		public static const END:uint = Keyboard.END;
		public static const ENTER:uint = Keyboard.ENTER;
		public static const BACKSPACE:uint = Keyboard.BACKSPACE;
		public static const NUMPAD_0:uint = Keyboard.NUMPAD_0;
		public static const NUMPAD_1:uint = Keyboard.NUMPAD_1;
		public static const NUMPAD_2:uint = Keyboard.NUMPAD_2;
		public static const NUMPAD_3:uint = Keyboard.NUMPAD_3;
		public static const NUMPAD_4:uint = Keyboard.NUMPAD_4;
		public static const NUMPAD_5:uint = Keyboard.NUMPAD_5;
		public static const NUMPAD_6:uint = Keyboard.NUMPAD_6;
		public static const NUMPAD_7:uint = Keyboard.NUMPAD_7;
		public static const NUMPAD_8:uint = Keyboard.NUMPAD_8;
		public static const NUMPAD_9:uint = Keyboard.NUMPAD_9;
		public static const NUMPAD_DIVIDE:uint = Keyboard.NUMPAD_DIVIDE;
		public static const NUMPAD_ADD:uint = Keyboard.NUMPAD_ADD;
		public static const NUMPAD_ENTER:uint = Keyboard.NUMPAD_ENTER;
		public static const NUMPAD_DECIMAL:uint = Keyboard.NUMPAD_DECIMAL;
		public static const NUMPAD_SUBTRACT:uint = Keyboard.NUMPAD_SUBTRACT;
		public static const NUMPAD_MULTIPLY:uint = Keyboard.NUMPAD_MULTIPLY;

		public static const SEMICOLON:uint = 186;
		public static const EQUAL:uint = 187;
		public static const COMMA:uint = 188;
		public static const MINUS:uint = 189;
		public static const PERIOD:uint = 190;
		public static const SLASH:uint = 191;
		public static const BACKQUOTE:uint = 192;
		public static const LEFTBRACKET:uint = 219;
		public static const BACKSLASH:uint = 220;
		public static const RIGHTBRACKET:uint = 221;
		public static const QUOTE:uint = 222;
		public static const ALTERNATE:uint = 18;
		public static const COMMAND:uint = 15;
		public static const NUMPAD:uint = 21;

		// Custom added
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

		public static const NUM_0:uint = 48;		
		public static const NUM_1:uint = 49;
		public static const NUM_2:uint = 50;
		public static const NUM_3:uint = 51;
		public static const NUM_4:uint = 52;
		public static const NUM_5:uint = 53;
		public static const NUM_6:uint = 54;
		public static const NUM_7:uint = 55;
		public static const NUM_8:uint = 56;
		public static const NUM_9:uint = 57;
		
		public static const SUBSTRACT:uint = 189;
		public static const ADD:uint = 187;
	}
}