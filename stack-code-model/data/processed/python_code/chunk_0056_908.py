package system.loader
{
	public class LoaderListener
	{
		public var onComplete:Function = null;
		public var onProgress:Function = null;
		
		
		
		public function LoaderListener(onComplete:Function,onProgress:Function = null)
		{
			this.onComplete = onComplete;
			this.onProgress = onProgress;
		}
	}
}