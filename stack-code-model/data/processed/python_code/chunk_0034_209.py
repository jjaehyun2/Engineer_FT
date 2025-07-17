package spider.cat.nova.common.visual.element {
	
	import flash.geom.Point;
	import flash.display.Shape;
	import flash.display.Graphics;
	
	public class Line { // should add a getSectors method
		
		private var start:Point;
		private var finish:Point;

		public function Line( start:Point , finish:Point ) {
			// constructor code
			
			this.start = start;
			this.finish = finish;
			
		}
		
		public function draw( breadth:Number , color:int ):Shape {
			
			var result:Shape = new Shape();
			result.graphics.lineStyle( breadth , color );
			result.graphics.moveTo( start.x , start.y );
			result.graphics.lineTo( finish.x , finish.y );
			return result;
			
		}
		
		public function drawUsingGraphics( g:Graphics , breadth:Number , color:int ):void {
			
			g.lineStyle( breadth , color );
			g.moveTo( start.x , start.y );
			g.lineTo( finish.x , finish.y );
			
		}

	}
	
}