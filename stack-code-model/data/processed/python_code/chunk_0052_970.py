/**
 * @author Peter Hansen
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.zzznake.Util
{
	import flash.text.TextField;
	import flash.text.TextFormat;
	import flash.text.TextFormatAlign;
	
	import flash.display.Sprite;
	
	import de.p3337.zzznake.Main.Zzznake;
	
	/**
	 * This class provides a simple button for general use.
	 */
	public class DefaultButton extends Sprite {
		
		public const _height:uint = 50;
		
		
		/**
		 * Creates a new button.
		 * 
		 * @param text The value for the default button.
		 */
		public function DefaultButton(text:String) {
			super();
			
			graphics.beginFill(0xbbbcc0);
			graphics.drawRect(0, 0, (Zzznake.ZZZNAKE_WIDTH - (Zzznake.ZZZNAKE_PADDING * 2)), _height);
			graphics.endFill();
			
			useHandCursor = true;
			buttonMode = true;
			mouseChildren = false;
			
			var myFormat:TextFormat = new TextFormat();
			myFormat.size = 18;
			myFormat.font = "Courier New";
			myFormat.bold = true;
			myFormat.align = TextFormatAlign.CENTER;
			
			var textField:TextField = new TextField();
			textField.defaultTextFormat = myFormat;
			textField.text = text;
			textField.width = (Zzznake.ZZZNAKE_WIDTH - (Zzznake.ZZZNAKE_PADDING * 2));
			textField.height = _height / 2;
			textField.y = 12;
			textField.mouseEnabled = false;
			addChild(textField);
		}
	}
}