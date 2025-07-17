package {
	import flash.display.DisplayObject;
	import flash.display.MovieClip;
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import flash.events.IOErrorEvent;
	import flash.events.ProgressEvent;
	import flash.utils.getDefinitionByName;
	
	/**
	 * ...
	 * @author Adam Vernon
	 */
	public class Preloader extends MovieClip {
		
		private var _loaderSprite:Sprite = new Sprite();
		
		public function Preloader() {
			if (stage) {
				stage.scaleMode = StageScaleMode.NO_SCALE;
				stage.align = StageAlign.TOP_LEFT;
			}
			addEventListener(Event.ENTER_FRAME, checkFrame);
			loaderInfo.addEventListener(ProgressEvent.PROGRESS, progress);
			loaderInfo.addEventListener(IOErrorEvent.IO_ERROR, ioError);
			
			this.addChild(_loaderSprite);
		}
		
		private function ioError(e:IOErrorEvent):void {
			trace(e.text);
		}
		
		private function progress(e:ProgressEvent):void {
			// TODO update loader
			_loaderSprite.graphics.clear();
			_loaderSprite.graphics.beginFill(0xEEEEEE, 0.9);
			_loaderSprite.graphics.drawRect(10, 10, (e.bytesLoaded / e.bytesTotal) * (this.stage.stageWidth - 20), 100); 
			_loaderSprite.graphics.endFill();
		}
		
		private function checkFrame(e:Event):void {
			if (currentFrame == totalFrames) {
				stop();
				loadingFinished();
			}
		}
		
		private function loadingFinished():void {
			removeEventListener(Event.ENTER_FRAME, checkFrame);
			loaderInfo.removeEventListener(ProgressEvent.PROGRESS, progress);
			loaderInfo.removeEventListener(IOErrorEvent.IO_ERROR, ioError);
			
			this.removeChild(_loaderSprite);
			
			startup();
		}
		
		private function startup():void {
			var mainClass:Class = getDefinitionByName("Main") as Class;
			addChild(new mainClass() as DisplayObject);
		}
		
	}
	
}