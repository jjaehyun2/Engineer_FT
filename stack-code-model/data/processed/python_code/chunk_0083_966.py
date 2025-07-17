package controls {
	import flash.display.DisplayObject;
	import flash.text.TextFieldAutoSize;
	
	import mx.controls.Label;
	import mx.core.UITextField;
	
	public class MultiLineLabel extends Label {
		
		public function set _text(text:String):void {
			super.text = text;
			//trace('(+++) MultiLineLabel.text='+text);
		}
		
		override protected function createChildren() : void {
			if (!textField) {
				textField = new SpecialUITextField();
				textField.styleName = this;
				addChild(DisplayObject(textField));
			}
			super.createChildren();
			textField.multiline = true;
			textField.wordWrap = true;
			textField.autoSize = TextFieldAutoSize.LEFT;
			//trace('(+++) MultiLineLabel.textField.text='+textField.text+', textField.textWidth='+textField.textWidth);
		}
	}
}