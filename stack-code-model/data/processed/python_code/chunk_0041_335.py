package com.illuzor.cats {
	
	import com.illuzor.cats.constants.ItemType;
	import flash.display.Sprite;
	
	public class Item extends Sprite {
		
		/** список категорий, которые принадлежат квадрату */
		private var categories:Vector.<String> = new Vector.<String>();
		
		public function Item() {
			draw(0xA8A8A8);
		}
		
		private function draw(color:uint):void {
			this.graphics.clear();
			this.graphics.beginFill(color);
			this.graphics.drawRoundRect(0, 0, 50, 50, 10);
			this.graphics.endFill();
		}
		
		public function addCategory(category:String):void {
			categories.push(category);
		}
		
		public function containsCategory(category:String):Boolean {
			for (var i:int = 0; i < categories.length; i++) {
				if (categories[i] == category) return true;
			}
			return false;
		}
		
		public function clear():void {
			draw(0xA8A8A8);
		}
		
		public function colorize(category:String):void {
			switch (category) {
				case ItemType.BLUE:
					draw(0x0080C0)
				break;
				case ItemType.GREEN:
					draw(0x004000)
				break;
				case ItemType.RED:
					draw(0xAA0000)
				break;
				case ItemType.YELLOW:
					draw(0xD2D200)
				break;
			}
		}
		
	}
}