package services.command.hotels
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.hotels.HotelsDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.hotels.DeleteHotelEvent;
	
	public class DeleteHotelCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = DeleteHotelEvent(event);
			var delegate:HotelsDelegate = new HotelsDelegate(this);
			delegate.deleteHotel(_event as DeleteHotelEvent);
			
			super.execute(event);
		}
	}
}