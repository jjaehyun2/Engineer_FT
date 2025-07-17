package common.mvc.manifest
{
	import flash.utils.Dictionary;
	
	/**
	 * Base manifest.
	 * 
	 * @author vizoli
	 */
	public class BaseManifest
	{
		private var _manifest:Dictionary;
		
		public function BaseManifest()
		{
			this._manifest = new Dictionary();
		}
		
		/**
		 * Returns the manifest.
		 */
		public function get manifest():Dictionary 
		{
			return this._manifest;
		}
		
	}

}