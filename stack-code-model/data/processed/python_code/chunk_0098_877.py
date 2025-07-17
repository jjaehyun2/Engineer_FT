package com.github.knose1.debug.input {
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.FocusEvent;
	import flash.events.KeyboardEvent;
	import flash.events.MouseEvent;
	import flash.text.TextField;
	import flash.text.TextFieldType;
	import flash.ui.Keyboard;
	
	/**
	 * ...
	 * @author Knose1
	 */
	public class DraggableTextInput extends Sprite {
		
		private var textField:TextField = new TextField();
		private var type:uint;
		private var oldValue:String = '';
		
		public function set value(pValue:*):void {
			
			switch (type) {
				case DraggableTextInputType.INT: textField.text = String(int(pValue)) || '';
				case DraggableTextInputType.NUMBER: textField.text = String(Number(pValue)) || '';
				default: textField.text = String(pValue);
			}
		}
		
		public function get value():* {
			
			switch (type) {
				case DraggableTextInputType.INT: return int(textField.text);
				case DraggableTextInputType.NUMBER: return Number(textField.text);
				default: return textField.text;
			}
		}
		
		public function DraggableTextInput(pType:uint) {
			super();
			
			type = pType;
			
			switch (type) {
				case DraggableTextInputType.INT: textField.text = '0';
				case DraggableTextInputType.NUMBER: textField.text = '';
				default: textField.text = '';
			}
			
			textField.type = TextFieldType.INPUT;
			
			textField.addEventListener(Event.CHANGE, valueChange);
			
			textField.addEventListener(MouseEvent.MOUSE_DOWN, registerClick);
			textField.addEventListener(MouseEvent.MOUSE_UP, unregisterClick);
			textField.addEventListener(FocusEvent.FOCUS_OUT, unregisterClick);
			textField.addEventListener(KeyboardEvent.KEY_DOWN, click);
			
			addChild(textField);
			
			graphics.beginFill(0, 0.5);
			graphics.drawRect(0, 0, textField.width, textField.height);
		}
		
		public function destroy():void {
			if (parent) parent.removeChild(this);
			
			textField.removeEventListener(MouseEvent.MOUSE_DOWN, registerClick);
			textField.removeEventListener(MouseEvent.MOUSE_UP, unregisterClick);
			textField.removeEventListener(FocusEvent.FOCUS_OUT, unregisterClick);
			textField.removeEventListener(KeyboardEvent.KEY_UP, click);
		}
		
		private function click(pEvent:KeyboardEvent):void {
			
			if (type == DraggableTextInputType.INT || type == DraggableTextInputType.NUMBER) {
				
				switch (pEvent.keyCode) {
					case Keyboard.UP: value += 1;
						break;
					
					case Keyboard.DOWN: value -= 1;
				}
				
				oldValue = value;
				
			}
		}
		
		private function valueChange(pEvent:Event):void {
			
			switch (type) {
				case DraggableTextInputType.INT :
					if (String(int(textField.text)) != textField.text) textField.text = oldValue;
					break;
				
				case DraggableTextInputType.NUMBER :
					if (String(Number(textField.text)) != textField.text) textField.text = oldValue;
					break;
			}
			
			
			oldValue = textField.text;
			
			graphics.clear();
			
			graphics.beginFill(0, 0.5);
			graphics.drawRect(0, 0, textField.width, textField.height);
		}
		
		private function registerClick(pEvent:MouseEvent) : void {
			startDrag();
		}
		
		private function unregisterClick(pEvent:Event) : void {
			stopDrag();
		}
		
	}
	


}