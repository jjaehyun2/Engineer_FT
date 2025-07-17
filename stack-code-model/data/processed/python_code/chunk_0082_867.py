package com.CSSTextArea {
	
	import flash.text.StyleSheet;
	import fl.controls.TextArea;
	import fl.core.UIComponent;
	
	public class CSSTextArea extends TextArea {
	
		private static var defaultStyles:Object = {
			styleSheet: null
		}
		public static function getDefaultStyles():Object {
			return UIComponent.mergeStyles(defaultStyles, TextArea.getStyleDefinition());
		}
		
		public function CSSTextArea() {
			super();
		}
		
		override protected function drawTextFormat():void {
			var styleSheet:StyleSheet = getStyleValue("styleSheet") as StyleSheet;
			textField.styleSheet = styleSheet;
			if (styleSheet == null) {
				super.drawTextFormat();
			} else {
				setEmbedFont();
				if (_html) { textField.htmlText = _savedHTML; }
			}
		}
	
	}
	
}