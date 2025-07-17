package services.command.checkOut
{
	import com.adobe.cairngorm.control.CairngormEvent;
		
	import mx.collections.ArrayCollection;
	
	import services.business.checkOut.CheckOutDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.checkOut.UnmergeItemEvent;

	public class UnmergeItemCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = UnmergeItemEvent(event);
			var delegate:CheckOutDelegate = new CheckOutDelegate(this);
			delegate.unmergeItem(_event as UnmergeItemEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			super.result(data);
		}
	}
}