package  {
	
	import flash.display.Sprite;
	import flash.filters.GlowFilter;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	
	public class ScaleformButton extends Sprite {
		
		private var design:MyScaleformButtonDesign;
		private var _selected:Boolean = false;
		
		public function ScaleformButton() {
			design = new MyScaleformButtonDesign();
			addChild(design);
		}
		
		public function set label(value:String):void {
			design.textField.text = value;
		}
		
		public function set selected(value:Boolean):void {
			_selected = value;
			if (value) {
				design.back.alpha = .9;
				design.back.filters = [new GlowFilter(0x0000FF, 1, 12, 12, 2, 2)];
				design.textField.textColor = 0xFF2424;
			} else {
				design.back.alpha = 1;
				design.back.filters = null;
				design.textField.textColor = 0xFFFFFF;
			}
		}
		
	}
}