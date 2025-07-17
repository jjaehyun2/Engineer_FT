package com.illuzor.circles.ui {
	
	import com.illuzor.circles.tools.Assets;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	import starling.display.Image;
	import starling.display.Sprite;
	import starling.events.Event;
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.events.TouchPhase;
	import starling.text.TextField;
	import starling.text.TextFieldAutoSize;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class Checkbox extends Sprite {
		
		private var _activated:Boolean;
		private var circleOff:Image;
		private var circleOn:Image;
		private var textBounds:Rectangle;
		
		public function Checkbox(text:String, textH:uint, active:Boolean = false) {
			circleOff = new Image(Assets.atlas.getTexture("checkboxOff"));
			addChild(circleOff);
			circleOff.width = circleOff.height = textH;
			circleOff.y = textH * .12;
			
			circleOn = new Image(Assets.atlas.getTexture("checkboxOn"));
			addChild(circleOn);
			circleOn.width = circleOn.height = textH;
			circleOn.y = textH * .12;
			
			activated = active;
			
			var textContainer:Sprite = new Sprite();
			addChild(textContainer);
			var textField:TextField = new TextField(10, 10, text, "play", 100, 0xFFFFFF);
			textField.batchable = true;
			textField.autoSize = TextFieldAutoSize.BOTH_DIRECTIONS;
			textContainer.addChild(textField);
			textContainer.height = textH;
			textContainer.scaleX = textContainer.scaleY;
			textContainer.x = textH * 1.2;
			
			textBounds = this.bounds;
			
			this.addEventListener(TouchEvent.TOUCH, onButtonClick);
		}
		
		private function onButtonClick(e:TouchEvent):void {
			if(stage){
				var globalTouch:Touch = e.getTouch(stage);
				switch (globalTouch.phase) {
					case TouchPhase.ENDED:
						var localPosition:Point = e.getTouch(this).getLocation(this);
						if (textBounds.contains(localPosition.x, localPosition.y)) {
							activated = !activated;
							dispatchEvent(new Event(Event.CHANGE));
						}
					break;
				}
			}
		}
		
		public function get activated():Boolean {
			return _activated;
		}
		
		public function set activated(value:Boolean):void {
			_activated = value;
			if (_activated) {
				circleOff.visible = false;
				circleOn.visible = true;
			} else {
				circleOff.visible = true;
				circleOn.visible = false;
			}
		}
		
	}
}