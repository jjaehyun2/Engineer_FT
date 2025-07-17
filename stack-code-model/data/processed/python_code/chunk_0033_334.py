package com.illuzor.lib.graphics {
	
	import flash.display.Shape;
	
	/**
	 * Класс быстрого прямоугольника
	 * 
	 * @author illuzor || illuzor@gmail.com
	 */
	
	public class FastRect extends Shape {
		
		private var _color:uint;
		private var _width:uint;
		private var _height:uint;
		private var _aplha:Number;
		
		public function FastRect(width:uint, height:uint, color:uint = 0x000000, alpha1:Number = 1) {
			_color = color;
			_width = width;
			_height = height;
			_aplha = alpha1;
			draw(width, height);
		}
		
		public override function set width (value:Number):void {
			_width = value;
			draw(value, _height );
		}
		
		public override function get width():Number {
			return _width;
		}
		
		public override function set height (value:Number):void {
			_height = value;
			draw(_width, value );
		}
		
		public override function get height():Number {
			return _height;
		}

		private function draw(width:uint, height:uint):void {
			this.graphics.clear();
			this.graphics.beginFill(_color, _aplha);
			this.graphics.drawRect(0, 0, width, height);
			this.graphics.endFill();
		}
		
	}
}