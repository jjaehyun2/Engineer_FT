package com.illuzor.thegame.editor.notifications {
	
	import com.bit101.components.Label;
	import com.bit101.components.PushButton;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.filters.DropShadowFilter;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com  //  illuzor@gmail.com
	 */
	
	public class AskWindow extends Sprite {
		
		private var text:String;
		private var buttons:Vector.<Object>;
		private var buttonContainer:Sprite;
		
		public function AskWindow(text:String, buttons:Vector.<Object>) {
			this.buttons = buttons;
			this.text = text;
			
			addEventListener(Event.ADDED_TO_STAGE, onAdded);
		}
		
		private function onAdded(e:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, onAdded);
			
			var invBackground:Sprite = new Sprite();
			invBackground.graphics.beginFill(0);
			invBackground.graphics.drawRect(0, 0, stage.stageWidth, stage.stageHeight);
			invBackground.graphics.endFill();
			invBackground.alpha = 0;
			addChild(invBackground);
			
			var container:Sprite = new Sprite();
			container.graphics.beginFill(0xF3F3F3);
			container.graphics.drawRect(0,0, 300, 80);
			container.graphics.endFill();
			container.filters = [new DropShadowFilter(0,0, 0, .7)];
			addChild(container);
			
			buttonContainer = new Sprite();
			container.addChild(buttonContainer);
			
			var label:Label = new Label(container);
			label.text = text.toUpperCase();
			label.width = 280
			label.x = 10;
			label.y = 10;
			
			for (var i:int = 0; i < buttons.length; i++) {
				var button:PushButton = new PushButton(buttonContainer);
				button.label = buttons[i].label;
				if (i > 0) button.x = buttonContainer.width + 20;
				button.addEventListener(MouseEvent.CLICK, buttons[i].func);
			}
			
			buttonContainer.y = 40;
			buttonContainer.x = (300 - buttonContainer.width) / 2;
			
			container.x = (stage.stageWidth - container.width) / 2;
			container.y = (stage.stageHeight - container.height) / 2;
			
			addEventListener(Event.REMOVED_FROM_STAGE, onRemove);
		}
		
		private function onRemove(e:Event):void {
			removeEventListener(Event.REMOVED_FROM_STAGE, onRemove);
			for (var i:int = 0; i < buttonContainer.numChildren; i++) {
				(buttonContainer.getChildAt(i) as PushButton).removeEventListener(MouseEvent.CLICK, buttons[i].func);
			}
		}
		
	}
}