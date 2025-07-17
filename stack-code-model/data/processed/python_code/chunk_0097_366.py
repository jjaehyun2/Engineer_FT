/*
 PureMVC - Copyright(c) 2006, 2007 FutureScale, Inc., Some rights reserved.
 Your reuse is governed by the Creative Commons Attribution 3.0 United States License
*/
package org.puremvc.patterns.facade
{
	import flash.events.EventDispatcher;
	
	import org.puremvc.interfaces.IFacade;
	import org.puremvc.interfaces.IFacadeClient;
	

	public class FacadeClient extends EventDispatcher implements IFacadeClient
	{
		/**
		 * Set the reference to the related Facade instance
		 * 
		 * This method should usually only be called by the
		 * IFacade instance that instantiated this Object.
		 * 
		 * @param facade should implement <code>IFacade</code>
		 */
		public function setFacade(facade:IFacade):void
		{
			this.facade = facade;
		}
		
		/**
		 * Get the reference to the related Facade instance
		 */
		public function getFacade():IFacade
		{
			return facade;
		}
		
		// protected getter/setter so that Mediator can
		// override getter and pull from static Singleton for
		// legacy implementations
		protected function set facade(facade:IFacade):void
		{
			_facade = facade;
		}
		
		protected function get facade():IFacade
		{
			return _facade;
		}
		
		protected var _facade:IFacade;
	}
}