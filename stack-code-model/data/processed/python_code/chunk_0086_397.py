package controls {
	import mx.core.UIComponent;
	import flash.display.Graphics;
	
	public class VolumeSlider extends UIComponent {
		public function VolumeSlider() {
			super();
		}
		
		override protected function updateDisplayList(w:Number, h:Number):void {
			super.updateDisplayList(w,h);
			if (w == 0 && h == 0) { return; }
			//trace("w = " + w + " h = " + h);
			if(this.parent) {
				var g:Graphics = this.graphics;
				g.clear();
				x = 0; y = 1;
				g.lineStyle(1, 0x000000, 1);
				while (x < w) {
					//trace("draw line starting at " + x + "," + h + ' to ' + x + ',' + (y-h));
					g.moveTo(x, h);
					g.lineTo(x, y-h);
					y++;
					x+=2;
				}
			}
		}    
	}
}