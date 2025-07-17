package metaswarm.swarm.patterns   {
import flash.display.*;
import flash.utils.*;
import flash.events.*;
import flash.geom.*;
import flash.text.*;

	public class GridMaker extends Sprite {
		
		//minimum size that text can be rastered at to provide
		//adequate sampling for large display
		//private static const FONTSIZE:Number = 42;
		
		public function GridMaker():void{
		}
		
		//returns a matrix of 2d coordinates
		public function make(numOfPoints:uint, w:uint, h:uint):Array
		{
			var points:Array = new Array();
			
			//trace("for pattern: " + pid + ", and sortOrder: " + sid + ": "); 
			var xMargin:uint = 0;
    		var yMargin:uint = 0;
			var cols:uint = Math.round(Math.sqrt(numOfPoints));
			var xsp:uint = w/(cols+xMargin);
			var ysp:uint = h/(cols+yMargin);
			var xoff:uint = (w - xsp*cols)/2;
			var yoff:uint = (h - ysp*cols)/2;
			
			for(var i:uint=0; i<numOfPoints; i++){
				
				var px:Number = xoff + xsp*(i%cols);
				var py:Number = yoff + ysp*Math.floor(i/cols);
				var nextPoint:Array = [px, py]
				points.push(nextPoint);
			}
			
			return points;
		}
		
	}//end class
}//end pkg