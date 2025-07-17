// class for wrapping text on button label

package controls
{
	import flash.text.TextFieldAutoSize;
	import mx.controls.Button;
	
	public class WrapButton extends Button
	{
		public function WrapButton()
		{
			super();
		}
		
		override protected function createChildren():void
		{
			super.createChildren();
			
			textField.multiline = true;
			textField.wordWrap = true;
			textField.autoSize = TextFieldAutoSize.CENTER;
		}
		
		override protected function updateDisplayList(unscaledWidth:Number, unscaledHeight:Number):void
		{
			super.updateDisplayList(unscaledWidth, unscaledHeight);
			textField.y = (this.height - textField.height) >> 1;
			
			height = textField.height + getStyle("paddingTop") + getStyle("paddingBottom");
		}
	}
}