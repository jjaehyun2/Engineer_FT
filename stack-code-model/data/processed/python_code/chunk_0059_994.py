package com.illuzor.test.bezier{
	import adobe.utils.CustomActions;
	import flash.display.Shape;
	import flash.display.Sprite;
	import flash.events.Event;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	public class Main extends Sprite {
		
		private var jsonString:String = '[{"x":20,"y":20},{"x":20,"y":20},{"x":21,"y":162},{"x":40,"y":180},{"x":63,"y":201},{"x":112,"y":30},{"x":60,"y":40},{"x":39,"y":44},{"x":136,"y":216},{"x":80,"y":180},{"x":43,"y":156},{"x":140,"y":60},{"x":140,"y":60}]';
		
		public function Main() {
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void {
			removeEventListener(Event.ADDED_TO_STAGE, init);
			
			var array:Array = JSON.parse(jsonString) as Array;
			
			//var count:uint = 0;
			
			var firstPoint:Object = array.splice(0, 1)[0];
			
			var shape:Shape = new Shape();
			addChild(shape);
			shape.graphics.lineStyle(1, 0x400000);
			shape.graphics.moveTo(firstPoint.x, firstPoint.y)
			
			trace(array.length)
			
			for (var i:int = 0; i < array.length; i += 3) {
				trace('shape')
				shape.graphics.cubicCurveTo(array[i].x, array[i].y, array[i+1].x, array[i+1].y,  array[i+2].x, array[i+2].y);
			}
			
		}
		
	}
	
}