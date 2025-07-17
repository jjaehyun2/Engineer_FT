package 
{
	import flash.display.Sprite;
	import flash.events.Event;
	
	/**
	 * ...
	 */
	[SWF(width = 544, height = 409, backgroundColor = 0xFFFFFF)]
	public class Main extends Sprite 
	{
		
		public function Main() : void 
		{
			if ( stage ) init();
			else addEventListener( Event.ADDED_TO_STAGE, init );
		}
		
		private function init( e:Event = null ) : void 
		{
			removeEventListener( Event.ADDED_TO_STAGE, init );
			// entry point
			var video : VideoFactory = new VideoFactory("http://example.com/sample.flv");
			video.connect();
			addChild( video );
			
			var videoControl : VideoControl = new VideoControl( video.param );
			videoControl.y = video.param.video.height;
			addChild( videoControl );
		}
		
	}
	
}