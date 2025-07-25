package preload
{
	import flash.display.Sprite;
    import flash.events.Event;
    import flash.events.ProgressEvent;
    import flash.utils.Timer;
    import flash.events.TimerEvent;
    import mx.events.*;
    import mx.preloaders.Preloader;
	import mx.preloaders.DownloadProgressBar;
	import preload.WelcomeScreen;
	import flash.external.*;

	public class CustomPreloader extends DownloadProgressBar {

        public var wcs:WelcomeScreen;
    
        public function CustomPreloader() 
        {
            super(); 
            wcs = new WelcomeScreen();
            this.addChild(wcs)                   
        }
    
        override public function set preloader( preloader:Sprite ):void 
        {         	      
            preloader.addEventListener( ProgressEvent.PROGRESS , SWFDownloadProgress );    
            preloader.addEventListener( Event.COMPLETE , SWFDownloadComplete );
            preloader.addEventListener( FlexEvent.INIT_PROGRESS , FlexInitProgress );
            preloader.addEventListener( FlexEvent.INIT_COMPLETE , FlexInitComplete );
        }
    
        private function SWFDownloadProgress( event:ProgressEvent ):void {}
    
		private function signalSWFDownloadComplete(boolClosed:Boolean):void {
			var parms:Object = new Object();
			parms.boolSWFDownloadComplete = boolClosed;
		    ExternalInterface.call("signalSWFDownloadComplete",parms); 
		}

        private function SWFDownloadComplete( event:Event ):void {
        	signalSWFDownloadComplete(true);
        //	wcs.closeScreen();
        }
    
        private function FlexInitProgress( event:Event ):void {}
    
        private function FlexInitComplete( event:Event ):void 
        {      
        	wcs.ready = true;  	
            dispatchEvent( new Event( Event.COMPLETE ) );
        }
        
 	}

}