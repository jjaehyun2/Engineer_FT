package spider.cat.nova.common.visual.element {
	
	import spider.cat.nova.common.visual.BasicShape;
	
	public class ColorRectangle extends BasicShape {

		public function ColorRectangle( width:Number , height:Number , color:int ) {
			// constructor code
			
			graphics.beginFill( color );
			graphics.drawRect( 0 , 0 , width , height );
			graphics.endFill();
			
		}

	}
	
}