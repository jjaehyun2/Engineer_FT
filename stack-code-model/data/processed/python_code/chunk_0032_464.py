/**
 * @author Peter Hansen
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.zzznake.Util
{
	import flash.text.TextField;
	import flash.text.TextFormat;
	
	import flash.display.Sprite;
	
	import de.p3337.zzznake.Main.Zzznake;

	/**
	 * This class provides a simple input field with a label for general use.
	 * The input field can also be used just as a normal non-editable text field.
	 */
	public class DefaultInput extends Sprite {
		private var textFormat:TextFormat;
		
		private var label:TextField;
		private var input:TextField;
		
		public const _height:uint = 25;
		
		
		/**
		 * Creates a new label and input field. 
		 * 
		 * @param labelValue The initial value for the label.
		 * @param inputValue The initial value for the input field.
		 * @param type Non-editible if 'dynamic', 'input' otherwise. Default is 'input'.
		 */
		public function DefaultInput(labelValue:String = "", inputValue:String = "", type:String = "input") {
			super();
			
			textFormat = new TextFormat();
			textFormat.font = "Courier New";
			textFormat.color = 0x000000;
			textFormat.size = 18;
			
			addLabel(labelValue);
			addInput(inputValue, type);
		}
		
		private function addLabel(text:String):void {
			label = new TextField();
			label.defaultTextFormat = textFormat;
			label.text = text;
			label.width = (Zzznake.ZZZNAKE_WIDTH - (Zzznake.ZZZNAKE_PADDING * 2));
			label.height = _height;
			label.mouseEnabled = false;
			addChild(label);
		}
		
		private function addInput(value:String, type:String):void {
			input = new TextField();
			input.defaultTextFormat = textFormat;
			input.type = type;
			input.border = type === "input";
			input.width = (Zzznake.ZZZNAKE_WIDTH - (Zzznake.ZZZNAKE_PADDING * 2));
			input.height = _height;
			input.text = value;
			input.mouseEnabled = type === "input";
			input.y = label.y + label.height;
			addChild(input);
		}
		
		public function getInputValue():String {
			return input.text;
		}
		
		public function setInputValue(text:String):void {
			input.text = text;
		}
		
		public function getInputTextField():TextField {
			return input;
		}
	}
}