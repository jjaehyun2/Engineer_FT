//------------------------------------------------------------------------------
//  Copyright (c) 2011 the original author or authors. All Rights Reserved. 
// 
//  NOTICE: You are permitted to use, modify, and distribute this file 
//  in accordance with the terms of the license agreement accompanying it. 
//------------------------------------------------------------------------------

package org.robotlegs.v2.extensions.stageWatcher
{
	import org.robotlegs.v2.core.api.IContext;
	import org.robotlegs.v2.core.api.IContextExtension;
	import org.robotlegs.v2.view.api.IViewManager;
	import org.robotlegs.v2.view.impl.StageWatcher;

	public class StageWatcherExtension implements IContextExtension
	{

		private static const stageWatcher:StageWatcher = new StageWatcher();

		public function initialize(context:IContext):void
		{
			const viewManager:IViewManager = context.injector.getInstance(IViewManager);
			viewManager.addWatcher(stageWatcher);
		}

		public function install(context:IContext):void
		{
		}

		public function uninstall(context:IContext):void
		{
			const viewManager:IViewManager = context.injector.getInstance(IViewManager);
			viewManager.removeWatcher(stageWatcher);
		}
	}
}