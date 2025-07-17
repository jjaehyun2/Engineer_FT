package com.illuzor.bubbles.graphics {
	
	import com.illuzor.bubbles.tools.ResourceManager;
	import starling.display.Button;
	import starling.display.Image;
	import starling.display.Sprite;
	import starling.text.TextField;
	import starling.text.TextFieldAutoSize;
	import starling.textures.Texture;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class TextButton extends Button {
		
		public function TextButton(upState:Texture, text:String) {
			super(upState);
			
			var tf:TextField = new TextField(10, 10, text, "font", 40, 0xFFFFFF);
			tf.autoSize = TextFieldAutoSize.BOTH_DIRECTIONS;
			addChild(tf);
			
			tf.x = (width - tf.width) >> 1;
			tf.y = (height - tf.height) >> 1;
			
			pivotX = this.width >> 1;
			pivotY = this.height >> 1;
		}
		
	}
}