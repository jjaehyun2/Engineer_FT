package org.pong.mvcs
{
	import org.pong.mvcs.controller.bootstraps.*;
	import robotlegs.bender.extensions.mediatorMap.api.IMediatorMap;
	import robotlegs.bender.extensions.signalCommandMap.api.ISignalCommandMap;
	import robotlegs.bender.framework.api.IConfig;
	import robotlegs.bender.framework.api.IInjector;
	
	/**
	 *
	 * AppConfig is Robotlegs internal context. All DI mapped data is done here.
	 *
	 * @author mc
	 */
	public class AppConfig implements IConfig
	{
		/**
		 * The <code>Injector</code> manages the mappings and acts as the central hub from which all
		 * injections are started.
		 */
		[Inject]
		public var injector:IInjector;
		
		/**
		 * The Signal Command Map allows you to bind Signals to Commands
		 */
		[Inject]
		public var signalCommandMap:ISignalCommandMap;
		
		/**
		 * The Mediator Map allows you to bind Mediators to objects
		 */
		[Inject]
		public var mediatorMap:IMediatorMap;
		
		/**
		 * Configure method bootstraps injection in multiple fragmated classes
		 */
		public function configure():void
		{
			trace(this + "configure()");
			
			new BootstrapModels(injector);
			new BootstrapServices(injector);
			new BootstrapSignals(injector);
			new BootstrapSignalCommandMap(signalCommandMap);
			new BootstrapMediatorMap(mediatorMap);
			new BootstrapManagers(injector);
			new BootstrapUtils(injector);
		}
	}
}