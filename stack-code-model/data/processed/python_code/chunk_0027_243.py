package  {
	
	import flash.display.Bitmap;
	import flash.display.Shape;
	import flash.display.Sprite;
	import flash.events.Event;
	import com.greensock.TweenMax;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	
	public class IntroObject extends Sprite {
		private var scrMask:Sprite;
		private var screen:Bitmap;
		
		public function IntroObject() {
			screen = new Bitmap(new Screen());
			screen.cacheAsBitmap = true;
			addChild(screen);
			
			scrMask = new Sprite();
			scrMask.cacheAsBitmap = true;
			addChild(scrMask);
			screen.mask = scrMask;
			
			addEventListener(Event.ADDED_TO_STAGE, added);
		}
		
		private function added(e:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, added);
			
			var mx:uint = 0;
			var my:uint = 0;
			
			for (var i:int = 0; i < 1024; i++) {
				var shape:Shape = genShape();
				shape.x = mx*64;
				shape.y = my * 64;
				shape.alpha = .5*Math.random();
				scrMask.addChild(shape);
				mx++;
				if (mx == 64) {
					mx = 0;
					my++;
				}
				
				var rand:Number = Math.random();
				if (rand <= .5) {
					shape.scaleY = 0;
					TweenMax.to(shape, 3 * Math.random(), { scaleY:1,alpha:1 } );
				} else {
					shape.scaleX = 0;
					TweenMax.to(shape, 3 * Math.random(), { scaleX:1,alpha:1 } );
				}
			}
			
		}
		
		private function genShape():Shape {
			var shape:Shape = new Shape();
			shape.graphics.beginFill(0x000000);
			shape.graphics.drawRect(0, 0, 64, 64);
			shape.graphics.endFill();
			return shape;
		}
		
	}
}