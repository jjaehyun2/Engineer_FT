/*
include "../includes/License.as.inc";
 */

package temple.core.net 
{
	import temple.core.debug.Registry;
	import temple.core.debug.log.Log;
	import temple.core.debug.log.LogLevel;
	import temple.core.debug.objectToString;
	import temple.core.destruction.DestructEvent;
	import temple.core.events.EventListenerManager;
	import temple.core.events.ICoreEventDispatcher;
	import temple.core.templelibrary;

	import flash.events.Event;
	import flash.events.IEventDispatcher;
	import flash.net.NetConnection;

	/**
	 * Base class for all NetConnections in the Temple. The CoreNetConnection handles some core features of the Temple:
	 * <ul>
	 * 	<li>Registration to the Registry class.</li>
	 * 	<li>Event dispatch optimization.</li>
	 * 	<li>Easy remove of all EventListeners.</li>
	 * 	<li>Wrapper for Log class for easy logging.</li>
	 * 	<li>Completely destructible.</li>
	 * 	<li>Tracked in Memory (of this feature is enabled).</li>
	 * </ul>
	 * 
	 * <p>You should always use and/or extend the CoreNetConnection instead of NetConnection if you want to make use of
	 * the Temple features.</p>
	 * 
	 * @see temple.core.Temple#registerObjectsInMemory
	 * 
	 * @author Thijs Broerse
	 */
	dynamic public class CoreNetConnection extends NetConnection implements ICoreEventDispatcher
	{
		include "../includes/ConstructNamespace.as.inc";
		
		private const _toStringProps:Vector.<String> = new Vector.<String>();
		private var _eventListenerManager:EventListenerManager;
		private var _isDestructed:Boolean;
		private var _registryId:uint;
		private var _emptyPropsInToString:Boolean = true;

		public function CoreNetConnection() 
		{
			construct::coreNetConnection();
		}
		
		/**
		 * @private
		 */
		construct function coreNetConnection():void
		{
			_registryId = Registry.add(this);
		}
		
		include "../includes/CoreObjectMethods.as.inc";
		
		include "../includes/CoreEventDispatcherMethods.as.inc";

		include "../includes/LogMethods.as.inc";
		
		include "../includes/ToStringPropsMethods.as.inc";
		
		include "../includes/ToStringMethods.as.inc";
		
		include "../includes/IsDestructed.as.inc";
		
		/**
		 * @inheritDoc
		 */
		public function destruct():void 
		{
			if (_isDestructed) return;
			
			dispatchEvent(new DestructEvent(DestructEvent.DESTRUCT));
			
			removeAllEventListeners();
			client = this;
			close();
			
			if (_eventListenerManager)
			{
				_eventListenerManager.destruct();
				_eventListenerManager = null;
			}
			_isDestructed = true;
		}
	}
}