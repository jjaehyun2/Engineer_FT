package it.sharpedge.navigator.core
{

	public class NavigationStatePool
	{
		private static var MAX_CACHE : int = 100;
		private static var _nsPool : Vector.<NavigationState>;

		/**
		 * Fetches a node from the pool.
		 */
		public static function getNavigationState( ...segments : Array ) : NavigationState
		{
			var ns : NavigationState = ( _nsPool && _nsPool.length > 0 ) ? _nsPool.pop() : new NavigationState( );
			ns.segments = segments;
			
			return ns;
		}

		/**
		 * Adds a node to the pool.
		 */
		public static function disposeNavigationState( state : NavigationState ) : void
		{
			if( !_nsPool ) _nsPool = new Vector.<NavigationState>();
			else if ( _nsPool.length >= MAX_CACHE || _nsPool.indexOf( state ) != -1 ) return;
			
			_nsPool.push( state );
		}
		
		
		public static function dispose() : void
		{
			_nsPool = null;
		}
	}
}