package spider.cat.nova.common.visual {
	
	import flash.display.Shape;
	
	public class BasicShape extends Shape {

		public function BasicShape() {
			// constructor code
		}
		
		public function move( newX:Number , newY:Number ):Shape {
			
			x = newX;
			y = newY;
			return this;
			
		}

	}
	
}