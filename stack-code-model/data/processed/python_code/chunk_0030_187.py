package framework.view.pages.reservationCreate.events
{
	import flash.events.Event;

	public class RemoveBasketItemEvent extends Event
	{
		public static const REMOVE_ITEM:String = "removeItem";
		
		public var index:int = 0;
		
		public function RemoveBasketItemEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
		}
		
	}
}