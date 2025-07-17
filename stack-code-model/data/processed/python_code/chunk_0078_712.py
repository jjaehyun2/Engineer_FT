/**
 * Created by newkrok on 22/11/15.
 */
package src.events
{
	import starling.events.Event;

	public class BaseModuleEvent extends Event
	{
		public static const DISPOSE_REQUEST:String = "BaseModuleEvent.DISPOSE_REQUEST";

		public function BaseModuleEvent( type:String, data:Object = null ):void
		{
			super( type, false, data );
		}
	}
}