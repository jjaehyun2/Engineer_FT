package services.events.checkOut
{
	import framework.view.pages.checkOut.events.CheckOutEvent;

	public class UnmergeItemEvent extends CheckOutEvent
	{
		public var itemId:int;
		
		public function UnmergeItemEvent(type:String)
		{
			super(type);
		}
		
	}
}