package classes
{
	import flash.display.Loader;
	import flash.events.Event;
	import flash.events.ProgressEvent;
	import flash.net.URLRequest;

	public class ImageLoader
	{
		public function ImageLoader(url:String, onLoaderReady:Function, onProgressStatus:Function)
		{
			var myLoader:Loader = new Loader();

			myLoader.contentLoaderInfo.addEventListener(ProgressEvent.PROGRESS, onProgressStatus);
			myLoader.contentLoaderInfo.addEventListener(Event.COMPLETE, onLoaderReady);
			
			var fileRequest:URLRequest = new URLRequest(url);
			myLoader.load(fileRequest);
		}
	}
}