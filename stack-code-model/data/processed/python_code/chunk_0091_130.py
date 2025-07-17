package my.sharp.tools.visual {
	
	import flash.display.Sprite;
	import my.sharp.tools.visual.Line;
	
	public class PlusSign extends Sprite {

		public function PlusSign( color:int , lineThickness:Number , size:Number ) {
			// constructor code
			
			addChild( new Line( color , lineThickness , size , 0 ).moveTo( 0 , size/2 ) );
			addChild( new Line( color , lineThickness , 0 , size ).moveTo( size/2 , 0 ) );
			
		}

	}
	
}