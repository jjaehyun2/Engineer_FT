package org.pong.mvcs.controller.bootstraps 
{
	import robotlegs.bender.framework.api.IInjector;
	import starling.utils.AssetManager;
	
	/**
	 * Bootstrap dependency injector for all Managers.
	 * 
	 * @see org.pong.mvcs.AppConfig
	 * @author mc
	 */
	
	public class BootstrapManagers 
	{
		public function BootstrapManagers(injector:IInjector)
		{
			injector.map(AssetManager).asSingleton();
		}
	}

}