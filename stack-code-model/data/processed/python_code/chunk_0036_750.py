package com.illuzor.spinner.graphics.controls {
	
	import starling.display.Button;
	import starling.display.Sprite;
	import starling.events.Event;
	import starling.textures.Texture;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class ToggleButton extends Sprite {
		
		private var onButton:Button;
		private var offButton:Button;
		private var _off:Boolean;
		
		public function ToggleButton(textureOn:Texture, textureOff:Texture, off:Boolean = false) {
			_off = off;
			onButton = new Button(textureOn);
			addChild(onButton);
			
			offButton = new Button(textureOff);
			addChild(offButton);
			
			onButton.visible = !off;
			offButton.visible = off;
			
			onButton.addEventListener(Event.TRIGGERED, onTriggered);
			offButton.addEventListener(Event.TRIGGERED, onTriggered);
		}
		
		private function onTriggered(e:Event):void {
			dispatchEvent(new Event(Event.TRIGGERED));
		}
		
		public function toggleState():void {
			_off = !_off;
			onButton.visible = !_off;
			offButton.visible = _off;
		}
		
		public function get off():Boolean {
			return _off;
		}
		
		override public function dispose():void {
			onButton.removeEventListener(Event.TRIGGERED, onTriggered);
			offButton.removeEventListener(Event.TRIGGERED, onTriggered);
			super.dispose();
		}
		
	}
}