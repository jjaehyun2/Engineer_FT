package  {
	
	import flash.display.Shape;
	
	public class ShapeWithPaint {

		public function ShapeWithPaint() {
			// constructor code
		}
		
		public static function make( color:int ):Shape {
			
			var shape:Shape = new Shape();
			shape.graphics.beginFill( color );
			return shape;
			
		}

	}
	
}