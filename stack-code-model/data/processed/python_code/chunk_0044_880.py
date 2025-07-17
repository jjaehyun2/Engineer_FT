//------------------------------------------------------------------------------
//  Copyright (c) 2011 the original author or authors. All Rights Reserved. 
// 
//  NOTICE: You are permitted to use, modify, and distribute this file 
//  in accordance with the terms of the license agreement accompanying it. 
//------------------------------------------------------------------------------

package org.robotlegs.v2.extensions.mediatorMap.support
{
	import org.robotlegs.v2.core.impl.ContextBuilder;
	import flash.display.Sprite;
	import org.swiftsuspenders.Injector;
	import org.robotlegs.v2.extensions.mediatorMap.api.IMediatorMap;
	import flash.display.MovieClip;
	import org.robotlegs.v2.extensions.mediatorMap.support.TracingMediator;
	import org.robotlegs.v2.core.api.ContextBuilderEvent;
	import org.robotlegs.v2.extensions.mediatorMap.impl.support.MediatorWatcher;
	import org.robotlegs.v2.extensions.mediatorMap.support.TracingV1Mediator;
	import org.robotlegs.v2.extensions.mediatorMap.bundles.RL1AndRL2MediatorsMediatorMapBundle;

	public class MicroAppWithMixedMediators extends Sprite
	{
	
		protected var _mediatorWatcher:MediatorWatcher;
	
		public function buildContext(completeHandler:Function, mediatorWatcher:MediatorWatcher):void
		{
			_mediatorWatcher = mediatorWatcher;
			
			const contextBuilder:ContextBuilder = new ContextBuilder();

			contextBuilder.addEventListener(ContextBuilderEvent.CONTEXT_BUILD_COMPLETE, addMappings);
			contextBuilder.addEventListener(ContextBuilderEvent.CONTEXT_BUILD_COMPLETE, completeHandler);
			
			// eventually this would be done with a bundle
			
			contextBuilder.withContextView(this)
									.withDispatcher(this)
									.withInjector(new Injector())
									.withBundle(RL1AndRL2MediatorsMediatorMapBundle)
									.build();
		}	

		protected function addMappings(e:ContextBuilderEvent):void
		{
			const mediatorMap:IMediatorMap = e.context.injector.getInstance(IMediatorMap);
			mediatorMap.map(MovieClip).toMediator(TracingMediator);
			mediatorMap.map(MovieClip).toMediator(TracingV1Mediator);
			
			e.context.injector.map(MediatorWatcher).toValue(_mediatorWatcher);
		}
	}
}