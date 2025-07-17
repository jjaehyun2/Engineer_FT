package spider.cat.nova.ai.game.falling.blocks.role {
	
	import spider.cat.nova.ai.game.falling.blocks.view.element.RoundRectangle;
	
	import flash.geom.Point;
	
	public class Role extends RoundRectangle {

		public function Role( size:Number , color:int ) {
			// constructor code
			
			super( size , size , 10 , color );
			
		}
		
		public function getCenter():Point {
			
			return new Point( x + width/2 , y + height/2 );
			
		}

	}
	
}