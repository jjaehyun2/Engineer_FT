package services.command.hotels
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.hotels.HotelsDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.hotels.UpdateHotelInfoEvent;
	import services.vo.hotels.HotelInfoTotalVO;

	public class UpdateHotelInfoCommand extends BaseCommand
	{
		override public function execute(event:CairngormEvent):void
		{
			_event = UpdateHotelInfoEvent( event );
			var delegate:HotelsDelegate = new HotelsDelegate( this );
			delegate.updateHotelInfo( _event as UpdateHotelInfoEvent );
			super.execute( _event as UpdateHotelInfoEvent );
		}
		
		override public function result(data:Object):void
		{
			if(!( _event as UpdateHotelInfoEvent ).isEdit)
			{
				model.hotelsModule.hotels.addItem( data as HotelInfoTotalVO );
			}
			else
			{
				model.hotelsModule.hotels.setItemAt( data as HotelInfoTotalVO, ( _event as UpdateHotelInfoEvent ).hotelIndex );
			}
			
			model.hotelsModule.hotelTotalInfo = data as HotelInfoTotalVO;
			model.hotelsModule.currPage = ( _event as UpdateHotelInfoEvent ).pageIndex;
			super.result( data );
		}
	}
}