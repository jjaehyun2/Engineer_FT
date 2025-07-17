package common.mvc.manifest
{
	import flash.utils.Dictionary;
	
	/**
	 * Interface of manifest.
	 * 
	 * @author vizoli
	 */
	public interface IManifest 
	{
		
		function get manifest():Dictionary;
		
		function setManifest():void;
		
	}
	
}