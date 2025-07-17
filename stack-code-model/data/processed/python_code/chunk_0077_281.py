package services.command.items.itemGroups
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.items.ItemsDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.items.itemGroups.ApplySystemGroupsToHotelEvent;
	
	import mx.collections.ArrayCollection;

	public class ApplySystemGroupsToHotelCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = ApplySystemGroupsToHotelEvent(event);
			var delegate:ItemsDelegate = new ItemsDelegate(this);
			delegate.setSysGroupsToHotel(_event as ApplySystemGroupsToHotelEvent);
			
			super.execute(event);
		}
		
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			model.transactionModule.hotelGroupsList = new ArrayCollection(data as Array);
			
			super.result(data);
		}
	}
}