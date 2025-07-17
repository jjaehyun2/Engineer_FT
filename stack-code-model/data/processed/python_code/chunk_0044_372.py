package com.illuzor.otherside.editor.screen.gameElements {
	
	import com.illuzor.otherside.editor.events.EnemyEvent;
	import flash.display.Bitmap;
	import flash.display.Shape;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class Enemy extends Sprite {
		
		public var data:Object = { };
		private var image:Bitmap;
		private var type:String;
		private var _selected:Boolean;
		private var selectBox:Shape;
		
		public function Enemy(image:Bitmap, type:String) {
			this.type = type;
			this.image = image;
			data.type = type;
			
			addEventListener(Event.ADDED_TO_STAGE, onAdded);
		}
		
		private function onAdded(e:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, onAdded);
			
			addChild(image);
			graphics.beginFill(0x0, 0);
			graphics.drawRect(0, 0, this.width, this.height);
			graphics.endFill();
			
			selectBox = new Shape();
			addChild(selectBox);
			selectBox.graphics.lineStyle(1, 0xFFFFFF, 1);
			selectBox.graphics.beginFill(0xFFFFFF, .2);
			selectBox.graphics.drawRect(0,0, this.width, this.height)
			selectBox.graphics.endFill();
			selectBox.visible = false;
			
			addEventListener(MouseEvent.CLICK, onSelect);
			addEventListener(Event.REMOVED_FROM_STAGE, onRemoved);
		}
		
		private function onSelect(e:MouseEvent):void {
			if (!_selected) {
				_selected = true;
				selectBox.visible = true;
				dispatchEvent(new EnemyEvent(EnemyEvent.SELECTED, this));
			}
		}
		
		public function deselect():void {
			if(_selected){
				_selected = false;
				selectBox.visible = false;
			}
		}
		
		private function onRemoved(e:Event):void {
			removeEventListener(Event.REMOVED_FROM_STAGE, onRemoved);
			removeEventListener(MouseEvent.CLICK, onSelect);
		}
		
		public function get selected():Boolean {
			return _selected;
		}

	}
}