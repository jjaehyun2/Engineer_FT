package  {
	
	import flash.display.Sprite;
	import flash.events.Event;
	import scaleform.gfx.Extensions;
	import flash.events.KeyboardEvent;
	import flash.ui.Keyboard;
	import com.greensock.TweenLite;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	
	public class TestClass extends Sprite{
		
		private var baseMovie:BaseMovie;
		
		public function TestClass():void {
			Extensions.enabled = true;
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void {
			removeEventListener(Event.ADDED_TO_STAGE, init);
			
			baseMovie = new BaseMovie();
			baseMovie.x = baseMovie.y = 256;
			addChild(baseMovie);
			
			baseMovie.scaleX = baseMovie.scaleY = .0;
			
			//stage.addEventListener(KeyboardEvent.KEY_DOWN, keysListener);
			//myDemoFunctionOn(true)
		}
		
		/*public function keysListener(e:KeyboardEvent):void {
			if (e.keyCode == Keyboard.Y) {
				trace("y")
				baseMovie.rotationY += 5;
			} else if (e.keyCode == Keyboard.U) {
				trace("u");
				baseMovie.rotationY -= 5;
			}
		}*/
		
		public function myDemoFunctionOn(bool:Boolean):void {
			if(bool)TweenLite.to(baseMovie, 2, { scaleX:1, scaleY:1 } );
		}
		
		public function myDemoFunctionOff():void {
			TweenLite.to(baseMovie, 2, { scaleX:.0, scaleY:.0 } );
		}
		
	}
}