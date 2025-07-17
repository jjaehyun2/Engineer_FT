package org.pong.mvcs.controller.bootstraps
{
	import org.pong.utils.graphic.*;
	import robotlegs.bender.framework.api.IInjector;
	
	/**
	 * 
	 * Bootstrap dependency injector for all Util classes.
	 * 
	 * @see org.pong.mvcs.AppConfig
	 * @author mc
	 */
	public class BootstrapUtils
	{
		public function BootstrapUtils(injector:IInjector)
		{
			injector.map(GraphicUtils).asSingleton();
		}
	}
}