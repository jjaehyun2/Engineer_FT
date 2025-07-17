/**
 * <p>Original Author: toddanderson</p>
 * <p>Class File: TextInput.as</p>
 * <p>Version: 0.4</p>
 *
 * <p>Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:</p>
 *
 * <p>The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.</p>
 *
 * <p>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.</p>
 *
 * <p>Licensed under The MIT License</p>
 * <p>Redistributions of files must retain the above copyright notice.</p>
 */
package com.custardbelly.as3flobile.controls.textinput
{
	import com.custardbelly.as3flobile.controls.core.AS3FlobileComponent;
	import com.custardbelly.as3flobile.enum.BasicStateEnum;
	import com.custardbelly.as3flobile.skin.TextInputSkin;
	
	import flash.display.Graphics;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.FocusEvent;
	import flash.events.MouseEvent;
	import flash.text.TextField;
	import flash.text.TextFieldAutoSize;
	import flash.text.TextFieldType;
	
	import org.osflash.signals.Signal;
	
	/**
	 * TextInput is a control to allow for input of text on single and multiple lines. 
	 * @author toddanderson
	 */
	public class TextInput extends AS3FlobileComponent
	{
		protected var _input:TextField;
		protected var _clearButton:Sprite;
		
		protected var _currentState:int;
		
		protected var _displayAsPassword:Boolean;
		protected var _defaultText:String = "";
		protected var _text:String = "";
		
		protected var _textChange:Signal;
		
		/**
		 * Constructor.
		 */
		public function TextInput() { super(); }
		
		/**
		 * @inherit
		 */
		override protected function initialize():void
		{	
			super.initialize();
			
			_width = 180;
			_height = 40;
			
			updatePadding( 4, 4, 4, 4 );
			
			_skin = new TextInputSkin();
			_skin.target = this;
			
			_textChange = new Signal( String );
		}
		
		/**
		 * @inherit
		 */
		override protected function createChildren():void
		{
			super.createChildren();
			
			_input = new TextField();
			_input.type = TextFieldType.INPUT;
			_input.autoSize = TextFieldAutoSize.NONE;
			_input.multiline = false;
			_input.wordWrap = false;
			addChild( _input );
			
			_clearButton = new Sprite();
			_clearButton.mouseChildren = false;
		}
		
		/**
		 * @inherit
		 */
		override protected function addDisplayHandlers():void
		{
			_input.addEventListener( FocusEvent.FOCUS_IN, handleFocusIn, false, 0, true );
			_input.addEventListener( FocusEvent.FOCUS_OUT, handleFocusOut, false, 0, true );
			
			addEventListener( MouseEvent.MOUSE_DOWN, handleClear, false, 0, true );
		}
		
		/**
		 * @inherit
		 */
		override protected function removeDisplayHandlers():void
		{
			_input.removeEventListener( FocusEvent.FOCUS_IN, handleFocusIn, false );
			_input.removeEventListener( FocusEvent.FOCUS_OUT, handleFocusOut, false );
			
			removeEventListener( MouseEvent.MOUSE_DOWN, handleClear, false );
		}
		
		/**
		 * @private
		 * 
		 * Invalidates textual content displayed in control. If the textual content is deemed invalid, default text is displayed. 
		 * @param value String
		 */
		protected function invalidateText( value:String ):void
		{
			if( _input.text == value ) return;
			
			_input.text = ( value.length > 0 ) ? value : _defaultText;
			_input.displayAsPassword = ( _input.text == _defaultText ) ? false : _displayAsPassword;
			updateDisplay();
			
			_textChange.dispatch( value );
		}
		
		/**
		 * @private
		 * 
		 * Invalidates the availability of multiline input. 
		 * @param value Boolean
		 */
		protected function invalidateMultiline( value:Boolean ):void
		{
			if( _input.multiline == value ) return;
			
			_input.multiline = value;
			_input.wordWrap = value;
			updateDisplay();
		}
		
		/**
		 * @private 
		 * 
		 * Invalidates the default text displayed in the control when textual content is deemed not valid.
		 */
		protected function invalidateDefaultText():void
		{
			if( _input.text.length == 0 )
			{
				_input.text = _defaultText;
				updateDisplay();
			}
		}
		
		/**
		 * @private 
		 * 
		 * Adds the clear button to the display list.
		 */
		protected function addClearButton():void
		{
			if( !contains( _clearButton ) )
				addChild( _clearButton );
		}
		
		/**
		 * @private 
		 * 
		 * Removes the clear button from the display list.
		 */
		protected function removeClearButton():void
		{
			if( contains( _clearButton ) )
				removeChild( _clearButton );
		}
		
		/**
		 * @private
		 * 
		 * Sets the current state of the control. 
		 * @param state int
		 */
		protected function setCurrentState( state:int ):void
		{
			if( _currentState == state ) return;
			
			_currentState = state;
			skinState = _currentState;
			
			if( _currentState == BasicStateEnum.FOCUSED )
				addClearButton();
			else
				removeClearButton();
		}
		
		/**
		 * @private
		 * 
		 * Event handler for input field having gained focus. 
		 * @param evt Event
		 */
		protected function handleFocusIn( evt:Event ):void
		{
			if( _input.text == _defaultText ) _input.text = "";
			setCurrentState( BasicStateEnum.FOCUSED );
		}
		
		/**
		 * @private
		 * 
		 * Event handler for input field having lost focus. 
		 * @param evt Event
		 */
		protected function handleFocusOut( evt:Event ):void
		{
			if( _input.text.length == 0 ) _input.text = _defaultText;
			setCurrentState( BasicStateEnum.NORMAL );
			_input.scrollV = 0;
		}
		
		/**
		 * @private
		 * 
		 * Event handler for having requested to clear the input field. 
		 * @param evt Event
		 */
		protected function handleClear( evt:MouseEvent ):void
		{
			if( mouseX >= _clearButton.x && mouseX <= ( _clearButton.x + _clearButton.width ) )
			{
				if( mouseY >= _clearButton.y && mouseY <= ( _clearButton.y + _clearButton.height ) )
				{
					invalidateText( "" );
					stage.focus = _input;
					_input.setSelection( 0, 0 );
				}
			} 
		}
		
		/**
		 * @inherit
		 */
		override public function dispose():void
		{
			super.dispose();
			
			while( numChildren > 0 )
				removeChildAt( 0 );
			
			_textChange.removeAll();
			_textChange = null;
		}
		
		/**
		 * Returns signal reference for change in text. 
		 * @return Signal Signal( String )
		 */
		public function get textChange():Signal
		{
			return _textChange;
		}
		
		/**
		 * Returns the background display instance for this control. 
		 * @return Graphics
		 */
		public function get backgroundDisplay():Graphics
		{
			return graphics;
		}
		
		/**
		 * Returns the clear button display instance for this control. 
		 * @return Graphics
		 */
		public function get clearButtonDisplay():Sprite
		{
			return _clearButton;
		}
		
		/**
		 * Returns the input display instance for this control. 
		 * @return TextField
		 */
		public function get inputDisplay():TextField
		{
			return _input;
		}
		
		/**
		 * Accessor/Modifier to display textual content as a password. 
		 * @return Boolean
		 */
		public function get displayAsPassword():Boolean
		{
			return _displayAsPassword;
		}
		public function set displayAsPassword( value:Boolean ):void
		{
			if( _displayAsPassword == value ) return;
			
			_displayAsPassword;
			invalidate( invalidateText, [_text] );
		}
		
		/**
		 * Accessor/Modifier for restriction of characters for input. 
		 * @return String
		 */
		public function get restrict():String
		{
			return _input.restrict;
		}
		public function set restrict( value:String ):void
		{
			_input.restrict = restrict;
		}
		
		/**
		 * Accessor/Modifier for maximum characters of input. 
		 * @return int
		 */
		public function get maxChars():int
		{
			return _input.maxChars;
		}
		public function set maxChars( value:int ):void
		{
			_input.maxChars = value;
		}
		
		/**
		 * Accessor/Modifier for the default boiler-plate text to display on empty input field. 
		 * @return String
		 */
		public function get defaultText():String
		{
			return _defaultText;
		}
		public function set defaultText( value:String ):void
		{
			if( _defaultText == value ) return;
			
			_defaultText = value;
			invalidate( invalidateDefaultText );
		}
		
		/**
		 * Accessor/Modifier for the input text of the control. 
		 * @return String
		 */
		public function get text():String
		{
			return _input.text;
		}
		public function set text( value:String ):void
		{
			invalidate( invalidateText, [value] );
		}
		
		/**
		 * Accessor/Modifier for the multiline value fo the control. The text input can be on a single line or multiple lines. 
		 * @return Boolean
		 */
		public function get multiline():Boolean
		{
			return _input.multiline;
		}
		public function set multiline( value:Boolean ):void
		{
			invalidate( invalidateMultiline, [value] );
		}
	}
}