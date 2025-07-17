package com.illuzor.otherside.editor.screen.components {
	
	import com.bit101.components.HUISlider;
	import com.illuzor.otherside.editor.events.ComponentEvent;
	import flash.events.Event;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class TextWithSlider extends ComponentBase {
		
		private var slider:HUISlider;
		
		public function TextWithSlider(text:String, min:uint, max:uint, eventType:uint, tick:Number = 1, w:uint = 200) {
			super(eventType, w, text);
			slider = new HUISlider(this, label.width + 4, 0, "");
			slider.tick = tick;
			slider.minimum = min;
			slider.maximum = max;
			slider.width = w - label.width +10;
			slider.addEventListener(Event.CHANGE, onChange);
		}
		
		private function onChange(e:Event):void {
			dispatchEvent(new ComponentEvent(ComponentEvent.CHANGE_VALUE, { type:eventType, value:slider.value } ));
		}
		
		public function setValue(value:Number):void {
			slider.value = value;
		}
		
		override public function dispose():void {
			slider.removeEventListener(Event.CHANGE, onChange);
		}
		
	}
}