package com.illuzor.lib.notifications {
	
	import com.illuzor.common.TextArea;
	import com.illuzor.lib.graphics.FastRect;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.filters.DropShadowFilter;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	
	internal class Notification extends Sprite {
		private var text:String;
		
		public function Notification(type:String, text:String, forcedWidth:uint = 0, forcedHeight:uint = 0) {
			this.text = text;
			addEventListener(Event.ADDED_TO_STAGE,addedToStage);
		}
		
		private function addedToStage(e:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, addedToStage);
			
			var rect:FastRect = new FastRect(0, 0, 0x072f3e, .9);
			addChild(rect);
			
			var textArea:TextArea = new TextArea();
			textArea.text = text;
			if (textArea.textWidth > stage.stageWidth / 4) {
				textArea.multiline = true;
				textArea.wordWrap = true;
				textArea.width = stage.stageWidth / 4;
			} else {
				textArea.width = textArea.textWidth + 4;
			}
			
			textArea.height = textArea.textHeight + 4;
			addChild(textArea);
			
			rect.width = textArea.width+20;
			rect.height = textArea.height + 20;
			
			textArea.x = uint((rect.width - textArea.width) / 2);
			textArea.y = uint((rect.height - textArea.height) / 2);
			
			rect.filters  = [new DropShadowFilter(0, 0, 0xFFFFFF, .3,16,16,2,3)];
		}
		
		private function addButtons():void {
			
		}
		
	}
}