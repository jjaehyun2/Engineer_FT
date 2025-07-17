package dom.tidesdk.worker
{
	/**
	 * <p>A module for creating Worker threads in
	 * TideSDK.</p>
	 */
	public class TWorkerBase
	{
		//
		// METHODS
		//

		/**
		 * <p>Create a worker thread instance.</p>
		 * 
		 * @param source  Either a JavaScript function (does not support closures), the URL of a JavaScript file, or a string containing JavaScript source. 
		 * 
		 * @return Ti.Worker.Worker   
		 */
		public function createWorker(source:*):TWorker { return null; }

		public function TWorkerBase() {}
	}
}