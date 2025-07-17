package org.robotlegs.core
{
	import flash.events.IEventDispatcher;
	
	/**
	 * The Robotlegs Context contract
	 */
	public interface IContext
	{
		/**
		 * The <code>IContext</code>'s <code>IEventDispatcher</code>
		 */
		function get eventDispatcher():IEventDispatcher;
	
	}
}