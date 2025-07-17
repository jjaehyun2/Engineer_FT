package  {
	
	import flash.display.Sprite;
	import flash.text.TextField;
	import flash.text.TextFieldAutoSize;
	
	/**
	 * Класс простой кнопки
	 */
	
	public class TextButton extends Sprite {
		
		private var _text:String;
		
		public function TextButton(text:String, w:uint = 80, h:uint = 20) {
			this._text = text;
			graphics.beginFill(0x0, .15);
			graphics.lineStyle(1, 0x0, .6);
			graphics.drawRect(0, 0, w, h);
			buttonMode = true;
			
			var tf:TextField = new TextField();
			tf.mouseEnabled = false;
			addChild(tf);
			tf.autoSize = TextFieldAutoSize.LEFT;
			tf.text = text;
			tf.x = (w - tf.width) >> 1;
		}
		
		public function get text():String {
			return _text;
		}
		
	}
}