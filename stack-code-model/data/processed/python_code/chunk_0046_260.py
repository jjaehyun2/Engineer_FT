package 
{
	import flash.display.DisplayObject;
	import flash.display.MovieClip;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import flash.events.IOErrorEvent;
	import flash.events.ProgressEvent;
	import flash.text.TextField;
	import flash.text.TextFormat;
	import flash.utils.getDefinitionByName;
	
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class Preloader extends MovieClip 
	{
		public var t:TextField = new TextField();
		
		public function Preloader() 
		{
			if (stage) {
				stage.scaleMode = StageScaleMode.NO_SCALE;
				stage.align = StageAlign.TOP_LEFT;
			}
			addEventListener(Event.ENTER_FRAME, checkFrame);
			loaderInfo.addEventListener(ProgressEvent.PROGRESS, progress);
			loaderInfo.addEventListener(IOErrorEvent.IO_ERROR, ioError);
			
			// TODO show loader
			t.defaultTextFormat = new TextFormat("Arial", 12, 0xFFFFFF, true);
			t.width = 640;
			t.text = "Music credit goes to http://www.nosoapradio.us/";
			addChild(t);
		}
		
		private function ioError(e:IOErrorEvent):void 
		{
			trace(e.text);
		}
		
		private function progress(e:ProgressEvent):void 
		{
			// TODO update loader
			graphics.clear();
			graphics.beginFill(0xFFFFFF, .8);
			graphics.drawRect(640 / 2 - 50, 480 / 2 - 2, int((e.bytesLoaded / e.bytesTotal) * 100), 4);
			graphics.endFill();
		}
		
		private function checkFrame(e:Event):void 
		{
			if (currentFrame == totalFrames) 
			{
				stop();
				loadingFinished();
			}
		}
		
		private function loadingFinished():void 
		{
			removeEventListener(Event.ENTER_FRAME, checkFrame);
			loaderInfo.removeEventListener(ProgressEvent.PROGRESS, progress);
			loaderInfo.removeEventListener(IOErrorEvent.IO_ERROR, ioError);
			
			// TODO hide loader
			graphics.clear();
			removeChild(t);
			startup();
		}
		
		private function startup():void 
		{
			var mainClass:Class = getDefinitionByName("Main") as Class;
			addChild(new mainClass() as DisplayObject);
		}
		
	}
	
}