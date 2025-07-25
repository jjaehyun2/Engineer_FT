//------------------------------------------------------------------------------
//  Copyright (c) 2011 the original author or authors. All Rights Reserved. 
// 
//  NOTICE: You are permitted to use, modify, and distribute this file 
//  in accordance with the terms of the license agreement accompanying it. 
//------------------------------------------------------------------------------

package org.robotlegs.base
{
	import flash.events.Event;
	import flash.events.IEventDispatcher;

	import org.robotlegs.core.IContext;

	/**
	 * An abstract <code>IContext</code> implementation
	 */
	public class ContextBase implements IContext, IEventDispatcher
	{
		/**
		 * @private
		 */
		protected var _eventDispatcher:IEventDispatcher;

		//---------------------------------------------------------------------
		//  API
		//---------------------------------------------------------------------

		/**
		 * @inheritDoc
		 */
		public function get eventDispatcher():IEventDispatcher
		{
			return _eventDispatcher;
		}

		//---------------------------------------------------------------------
		//  Constructor
		//---------------------------------------------------------------------

		/**
		 * Abstract Context Implementation
		 *
		 * <p>Extend this class to create a Framework or Application context</p>
		 */
		public function ContextBase(dispatcher:IEventDispatcher)
		{
			_eventDispatcher = dispatcher;
		}

		//---------------------------------------------------------------------
		//  EventDispatcher Boilerplate
		//---------------------------------------------------------------------

		/**
		 * @private
		 */
		public function addEventListener(type:String, listener:Function, useCapture:Boolean = false, priority:int = 0, useWeakReference:Boolean = false):void
		{
			eventDispatcher.addEventListener(type, listener, useCapture, priority);
		}

		/**
		 * @private
		 */
		public function dispatchEvent(event:Event):Boolean
		{
			if (eventDispatcher.hasEventListener(event.type))
				return eventDispatcher.dispatchEvent(event);
			return false;
		}

		/**
		 * @private
		 */
		public function hasEventListener(type:String):Boolean
		{
			return eventDispatcher.hasEventListener(type);
		}

		/**
		 * @private
		 */
		public function removeEventListener(type:String, listener:Function, useCapture:Boolean = false):void
		{
			eventDispatcher.removeEventListener(type, listener, useCapture);
		}

		/**
		 * @private
		 */
		public function willTrigger(type:String):Boolean
		{
			return eventDispatcher.willTrigger(type);
		}
	}
}