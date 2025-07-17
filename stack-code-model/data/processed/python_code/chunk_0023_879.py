/**
 * Created by newkrok on 09/04/16.
 */
package ageofai.fruit.event
{
	import ageofai.fruit.vo.FruitVO;

	import flash.events.Event;

	public class FruitViewEvent extends Event
	{
		public static const FRUIT_CREATED:String = 'FruitViewEvent.FRUIT_CREATED';

		public var fruitVO:FruitVO;

		public function FruitViewEvent( type:String, bubbles:Boolean = false, cancelable:Boolean = false )
		{
			super( this.type, this.bubbles, this.cancelable )
		}

		override public function clone():Event
		{
			var event:FruitViewEvent = new FruitViewEvent( this.type, this.bubbles, this.cancelable );
			event.fruitVO = this.fruitVO;

			return event;
		}
	}
}