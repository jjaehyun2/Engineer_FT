package visual {
	
	import flash.display.Shape;
	
	public class Rectangle extends Shape {

		public function Rectangle(width:Number, height:Number, color:int, alpha:Number) {
			// constructor code
			graphics.beginFill(color, alpha);
			graphics.drawRect(0, 0, width, height);
			graphics.endFill();
		}

	}
	
}