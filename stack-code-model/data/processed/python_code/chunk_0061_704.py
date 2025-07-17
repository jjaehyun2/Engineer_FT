package grid {
	
	import flash.display.Shape;
	import flash.display.Graphics;

	public class TransparentRect extends Shape {

		public function TransparentRect(width:Number, height:Number) {
			// constructor code
			var painter: Graphics = this.graphics;
			painter.beginFill(0x000000, 0.3);
			painter.drawRect(0, 0, width, height);
			painter.endFill();
		}

	}

}