/**
 * This custom component is made in order to facilitate the number only fields in SEMAPresentation.
 * This component can be customized to have different lengths of whole number and exponent.
 * 
 * In MXML you can use this component as follows, just the same we as TextInput.
 * 
 * <comp:NumberInput id="numberComponent"/>
 * 
 * By default this component has the following properties.
 * 	maxWholeNumberLength = 5
 *  maxExponentLength    = 2
 * 
 * If you want to override these values, you can do like this.
 * 
 * <comp:NumberInput id="numberComponent" maxWholeNumberLength=10 maxExponentLength=2/>
 * 
 * @author Zone24x7
 */
package CustomComps
{
	import flash.events.FocusEvent;
	import flash.events.KeyboardEvent;
	import flash.events.MouseEvent;
	import flash.events.TextEvent;
	import flash.ui.Keyboard;
	
	import mx.controls.TextInput;
	
	public class NumberInput extends TextInput
	{
		/* This will keep the maximum length of the whole number which would allowed by this component. */
		private var __maxWholeNumberLength : Number = 5;
		
		/* This will keep the maximum length of the exponent which would allowed by this component */ 
		private var __maxExponentLength : Number = 2;
		
		/* This will keep the position of cursor. */
		private var __position : Number = 0;
		
		/**
		 * Public constructor for component
		 */
		public function NumberInput()
		{
			super();
			addEventListener(TextEvent.TEXT_INPUT,interceptChar,true,0);
			addEventListener(MouseEvent.CLICK,setPosition,true);
			addEventListener(KeyboardEvent.KEY_DOWN,interceptKey,true);
			addEventListener(FocusEvent.FOCUS_IN,interceptFocus,false);
		}
		
		/**
		 * This will return the maxWholeNumberLength value which is the maximum allowed length for the whole number.
		 * 
		 * @return maximum allowed length for the whole number
		 * @author Zone24x7
		 */
		public function get maxWholeNumberLength() : Number
		{
			return __maxWholeNumberLength;
		}
		
		/**
		 * This will set the maxWholeNumberLength value which is the maximum allowed length for the whole number.
		 * 
		 * @param length maximum allowed length for the whole number
		 * @author Zone24x7
		 */
		public function set maxWholeNumberLength(length : Number) : void
		{
			if (length > 0)
			{
				__maxWholeNumberLength = length;
			}
		}
		
		/**
		 * This will return the maxExponentLength value which is the maximum allowed length for the exponent.
		 * 
		 * @return maximum allowed length for the exponent
		 * @author Zone24x7
		 */
		public function get maxExponentLength() : Number
		{
			return __maxExponentLength;
		}
		
		/**
		 * This will set the maxExponentLength value which is the maximum allowed length for the exponent.
		 * 
		 * @param length maximum allowed length for the exponent
		 * @author Zone24x7
		 */
		public function set maxExponentLength(length : Number) : void
		{
			if (length > 0)
			{
				__maxExponentLength = length;
			}
		}
		
		/**
		 * This will check if the passing value is a valid <B>Number</B> or not
		 * 
		 * @param value String value to check.
		 * @return whether the passed value is a valid number or not.
		 * @author Zone24x7
		 */
		private function isValidNumber(value : String) : Boolean
		{
			var exp : String = "^(\\d{1," + maxWholeNumberLength + "}+(\\.\\d{0," + maxExponentLength + "})?)$";
			return new RegExp(exp).test(value.toString());
		}
		
		/**
		 * This will trigger at every key press and it will check for the validity and if valid it will
		 * allow to display the current character.
		 * 
		 * @param event textevent occured from the key press.
		 * @author Zone24x7
		 */
		private function interceptChar( event:TextEvent ) : void
		{
			var str : String = super.text.substr(0, this.selectionBeginIndex).concat(event.text).concat(super.text.substr(this.selectionEndIndex, __position));
			if (!isValidNumber(str))
			{
				event.preventDefault();
				return;
			}
		}
		
		/**
		 * This will trigger when the mouse is clicked on the component.
		 * 
		 * @param event MouseEvent occured from the mouse click.
		 * @author Zone24x7
		 */
		private function setPosition( event : MouseEvent ) : void
		{
			reposition();
		}
		
		/**
		 * This will set the current cursor position by reading it from the super component. This should be called
		 * at every explicit position change in order to make sure interceptChar works as expected.
		 * 
		 * @author Zone24x7
		 */
		private function reposition() : void
		{
			__position = this.selectionBeginIndex;
		}
		
		/**
		 * This will trigger at every focus-in operation. Whenever the focus is received position needs to be 
		 * re-adjusted.
		 * 
		 * by default, text box will be highlighted when it receives focus through tab button. If this functionlity
		 * needs to be changed to remove this highlight, comment the current code and un-comment the commented
		 * code.
		 * 
		 * @param event FocusEvent occured
		 * @author Zone24x7 
		 */
		private function interceptFocus( event : FocusEvent) : void
		{
			//setSelection( super.text.length, super.text.length);
			//__position = 0;
			__position = this.selectionBeginIndex;
		}
		
		/**
		 * This will handle all the special keys and it will call the reposition to adjust the current position
		 * of the cursor.
		 * 
		 * @param event KeyboardEvent occured by the special character.
		 * @author Zone24x7
		 */
		private function interceptKey( event:flash.events.KeyboardEvent ) : void
		{
			if ((event.keyCode == Keyboard.BACKSPACE) ||
				(event.keyCode == Keyboard.DELETE) || 
				(event.keyCode == Keyboard.LEFT)  ||
				(event.keyCode == Keyboard.RIGHT) || 
				(event.keyCode == Keyboard.END) || 
				(event.keyCode == Keyboard.HOME))
			{
				reposition();
			}
			invalidateDisplayList();
		}
		
		/**
		 * This will override the existing text assignment functionlity and it only allows strings to be set
		 * only if it's in the proper format.
		 * 
		 * @param value value needs to be set.
		 * @author Zone24x7
		 */
		override public function set text(value:String):void
		{
			if ((value==null)||(value.length==0)||(isValidNumber(value)))
			{
				super.text = value;
			}
		}
	}
}