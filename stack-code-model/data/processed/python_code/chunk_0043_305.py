package view {
	
	import flash.display.Graphics;
	import flash.display.Sprite;
	
	/**
	 * ...
	 * @author 鸿杰
	 */
	public final class ScaleRect extends Sprite {
		
		private var _isEnabeld:Boolean = true;
		
		private var _w:int = 10;
		
		private var _h:int = 10;
		
		public function ScaleRect(alpha:Number) {
			super();
			isEnabeld = true;
			this.alpha = alpha;
		}
		
		public function get isEnabeld():Boolean {
			return _isEnabeld;
		}
		
		public function set isEnabeld(value:Boolean):void {
			_isEnabeld = value;
			_drawMe();
		}
		
		public function setSize(w:int, h:int):void {
			_w = w;
			_h = h;
			_drawMe();
		}
		
		private function _drawMe():void {
			const g:Graphics = this.graphics;
			g.clear();
			g.beginFill(_isEnabeld ? 0x00ff00 : 0xc9c9c9);
			g.drawRect((_w >> 1) * -1, (_h >> 1) * -1, _w, _h);
			g.endFill();
		}
	
	}

}