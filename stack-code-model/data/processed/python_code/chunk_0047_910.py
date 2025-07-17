package com.illuzor.leaptest.away3d.tools {
	
	import com.illuzor.leaptest.away3d.events.RotatorEvent;
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	import flash.utils.clearInterval;
	import flash.utils.setInterval;
	
	/**
	 * Класс для создания прелоадеров (preloaders.net)
	 * 
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	
	[Event(name="rotEnds", type="com.illuzor.leaptest.away3d.events.RotatorEvent")]
	public class Rotator extends Sprite {

		private var interval:uint;
		private var frameWidth:uint;
		private var totalElements:uint;
		private var elementsCounter:uint;
		private var intervalID:uint;
		private var rect:Rectangle;
		private var bitmap:Bitmap;
		private var bitmapData:BitmapData;
		
		public function Rotator(bitmapData:BitmapData, rectangle:Rectangle, interval:uint = 100) {
			this.interval = interval;
			this.bitmapData = bitmapData;
			frameWidth = rectangle.width;
			totalElements = bitmapData.width / rectangle.width;
			
			rect = rectangle;
			bitmap = new Bitmap();
			addChild(bitmap);
			update();
			intervalID = setInterval(update, interval);
			addEventListener(Event.REMOVED_FROM_STAGE, onRemoved);
		}

		private function update():void {
			if (elementsCounter < totalElements-1) {
				elementsCounter++;
				updateBitmap(elementsCounter);
			} else {
				//elementsCounter = 0;
				dispatchEvent(new RotatorEvent(RotatorEvent.ROTATOR_ENDS));
			}
			
		}
		
		private function updateBitmap(num:uint):void {
			rect.x = num * frameWidth;
			var bdata:BitmapData = new BitmapData(frameWidth, frameWidth);
			bdata.copyPixels(bitmapData, rect, new Point());
			bitmap.bitmapData = bdata;
		}
		
		private function onRemoved(e:Event):void {
			removeEventListener(Event.REMOVED_FROM_STAGE, onRemoved);
			clearInterval(intervalID);
			bitmapData = null;
			bitmap = null;
			rect = null;
		}
		
	}
}