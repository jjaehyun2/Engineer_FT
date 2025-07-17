package {
	
	import flash.desktop.NativeApplication;
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import flash.events.KeyboardEvent;
	import flash.media.Camera;
	import flash.media.Video;
	import flash.ui.Keyboard;
	import flash.ui.Multitouch;
	import flash.ui.MultitouchInputMode;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	
	public class Main extends Sprite {
		
		private var cam:Camera;
		
		public function Main():void {
			stage.scaleMode = StageScaleMode.NO_SCALE;
			stage.align = StageAlign.TOP_LEFT;
			Multitouch.inputMode = MultitouchInputMode.TOUCH_POINT;
			
			connectCamera();
			
			stage.addEventListener(KeyboardEvent.KEY_DOWN, onKeyDown);
		}
		
		private function onKeyDown(e:KeyboardEvent):void {
			e.preventDefault();
			if (e.keyCode == Keyboard.HOME) {
				NativeApplication.nativeApplication.exit();
			} else if (e.keyCode == Keyboard.BACK) {
				trace("BACK button pressed");
			}
		}
		
		private function connectCamera():void {
			cam = Camera.getCamera()
			cam.setMode(400, 300, 25);
			cam.setQuality(0, 100);
			var vid:Video = new Video();
			vid.width = 1000;
			vid.height = 1000;
			vid.attachCamera(cam);
			vid.scaleX = 100;
			vid.scaleY = 100;
			
			vid.x = 240;
			vid.y = 0;
			addChild(vid);
		
		}
	}
}