//------------------------------------------------------------------------------
//  Copyright (c) 2011 the original author or authors. All Rights Reserved. 
// 
//  NOTICE: You are permitted to use, modify, and distribute this file 
//  in accordance with the terms of the license agreement accompanying it. 
//------------------------------------------------------------------------------

package org.robotlegs.v2.extensions.viewManager
{
	import org.robotlegs.v2.core.api.IContext;
	import org.robotlegs.v2.core.api.IContextExtension;
	import org.robotlegs.v2.extensions.viewManager.api.IViewManager;
	import org.robotlegs.v2.extensions.viewManager.impl.ContainerRegistry;
	import org.robotlegs.v2.extensions.viewManager.impl.ViewManager;
	import org.robotlegs.v2.extensions.viewManager.impl.ViewProcessor;

	public class ViewManagerExtension implements IContextExtension
	{
		// Really? Yes, there can be only one.
		private static var containerRegistry:ContainerRegistry;

		// Really? Yes, there can be only one.
		private static var viewProcessor:ViewProcessor;
		
		private var context:IContext;
		
		private var viewManager:IViewManager;

		public function install(context:IContext):void
		{
			this.context = context;
			
			// Just one Container Registry
			containerRegistry ||= new ContainerRegistry();
			context.injector.map(ContainerRegistry).toValue(containerRegistry);

			// And just one View Processor
			viewProcessor ||= new ViewProcessor(containerRegistry);
			context.injector.map(ViewProcessor).toValue(viewProcessor);

			// But you get your own View Manager
			context.injector.map(IViewManager).toSingleton(ViewManager);
		}

		public function initialize():void
		{
			viewManager = context.injector.getInstance(IViewManager);
		}

		public function uninstall():void
		{
			viewManager.destroy();
			context.injector.unmap(IViewManager);
			context.injector.unmap(ViewProcessor);
			context.injector.unmap(ContainerRegistry);
		}
	}
}