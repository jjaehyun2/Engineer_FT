package services.command.hotels
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.hotels.HotelsDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.hotels.GetHotelsListEvent;
	
	import mx.collections.ArrayCollection;

	public class GetHotelsListCommand extends BaseCommand
	{
		
		override public function execute(event:CairngormEvent):void
		{
			_event = GetHotelsListEvent( event );
			var delegate:HotelsDelegate = new HotelsDelegate( this );
			delegate.getHotelsList(_event as GetHotelsListEvent);
			super.execute( event );
		}
		
		override public function result(data:Object):void
		{
			model.hotelsModule.hotels = new ArrayCollection(data as Array);
			super.result(data);
		}
	}
}