package spider.cat.nova.common.visual.sign {
	
	import spider.cat.nova.common.visual.BasicShape;
	import spider.cat.nova.common.visual.element.Line;
	
	import flash.geom.Point;
	
	public class Square extends BasicShape {

		public function Square( size:Number , strokeBreadth:Number , color:int ) {
			// constructor code
			
			var one:Point = new Point( 0 , 0 );
			var two:Point = new Point( size , 0 );
			var three:Point = new Point( size , size );
			var four:Point = new Point( 0 , size );
			var lineOne:Line = new Line( one , two );
			var lineTwo:Line = new Line( two , three );
			var lineThree:Line = new Line( three , four );
			var lineFour:Line = new Line( four , one );
			
			lineOne.drawUsingGraphics( this.graphics , strokeBreadth , color );
			lineTwo.drawUsingGraphics( this.graphics , strokeBreadth , color );
			lineThree.drawUsingGraphics( this.graphics , strokeBreadth , color );
			lineFour.drawUsingGraphics( this.graphics , strokeBreadth , color );
			
		}

	}
	
}