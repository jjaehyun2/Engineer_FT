/**
 * Created by newkrok on 09/04/16.
 */
package ageofai.forest.event
{
	import flash.events.Event;

	public class ForestViewEvent extends Event
	{
		public static const FOREST_CREATED:String = 'ForestViewEvent.FOREST_CREATED';

		//public var forestVO:ForestVO;

		public function ForestViewEvent( type:String, bubbles:Boolean, cancelable:Boolean )
		{
			super( this.type, this.bubbles, this.cancelable )
		}

		override public function clone():Event
		{
			var event:ForestViewEvent = new ForestViewEvent( this.type, this.bubbles, this.cancelable );
			//event.forestVO = this.forestVO;

			return event;
		}
	}
}