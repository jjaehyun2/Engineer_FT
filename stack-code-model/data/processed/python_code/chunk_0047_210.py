package preloaders {
	import flash.display.*;
	import flash.text.*;
	import flash.utils.*;
	import flash.events.*;
	import mx.preloaders.*;
	import mx.events.*;
	
	public class Preloader extends mx.preloaders.DownloadProgressBar {
		public function Preloader() {   
			super();
			this.downloadingLabel = 'Downloading...';
			initializingLabel = 'Initializing...';
		}
		
		override public function set preloader(preloader:Sprite):void {
			preloader.addEventListener(ProgressEvent.PROGRESS, 
				function (event:ProgressEvent):void {
				}
			);   
			preloader.addEventListener(Event.COMPLETE, 
				function (event:Event):void {
				}
			);
			
			preloader.addEventListener(FlexEvent.INIT_PROGRESS, 
				function (event:Event):void {
				}
			);
			preloader.addEventListener(FlexEvent.INIT_COMPLETE, 
				function (event:Event):void {
					var timer:Timer = new Timer(2000,1);
					timer.addEventListener(TimerEvent.TIMER, 
						function (event:TimerEvent):void {
							dispatchEvent(new Event(Event.COMPLETE));
						}
					);
					timer.start();
				}
			);
		}
	}
}