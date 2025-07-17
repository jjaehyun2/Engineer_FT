/**
 * Created by newkrok on 09/04/16.
 */
package ageofai.forest.event
{
	import flash.events.Event;

	public class ForestEvent extends Event
	{
		public static const FOREST_AMOUNT_UPDATED:String = 'ForestEvent.FOREST_AMOUNT_UPDATED';
		public static const FRUIT_CREATED:String = 'ForestEvent.FRUIT_CREATED';

		public var valueAmount:Number;
		public static const FOREST_RUN_OUT:String = 'ForestEvent.FOREST_RUN_OUT';

		public function ForestEvent( type:String, bubbles:Boolean = false, cancelable:Boolean = false )
		{
			super( type, bubbles, cancelable );
		}

		override public function clone():Event
		{
			var event:ForestEvent = new ForestEvent( this.type, this.bubbles, this.cancelable );
			event.valueAmount = this.valueAmount;

			return event;
		}
	}
}