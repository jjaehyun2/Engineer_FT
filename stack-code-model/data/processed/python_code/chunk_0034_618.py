package services.command.hotels
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.hotels.HotelsDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.hotels.GetHotelRoomSettingsEvent;

	public class GetHotelRoomSettingsCommand extends BaseCommand
	{	
		override public function execute(event:CairngormEvent):void
		{
			_event = GetHotelRoomSettingsEvent( event );
			var delegate:HotelsDelegate = new HotelsDelegate( this );
			
			delegate.getHotelRoomSettings( _event as GetHotelRoomSettingsEvent );
			super.execute( event );
		}
		
		override public function result(data:Object):void
		{
			var items:Array = data as Array;
			model.hotelsModule.hotelRoomSettings.removeAll();
			for(var e:int=0;e<items.length;e++)
				model.hotelsModule.hotelRoomSettings.addItem( items[e] );
			
			model.hotelsModule.hotelRoomSettings.refresh();
			super.result( data ); 
		}	
		
	}
}