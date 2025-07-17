package services.command.hotels
{
	import com.adobe.cairngorm.control.CairngormEvent;

	import services.business.hotels.HotelsDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.hotels.GetRealRoomTypeListEvent;

	import mx.collections.ArrayCollection;

	public class GetRealRoomTypeListCommand extends BaseCommand
	{

		override public function execute(event:CairngormEvent):void
		{
			_event = GetRealRoomTypeListEvent( event );
			var delegate:HotelsDelegate = new HotelsDelegate( this );
			delegate.getRealRoomTypeList(_event as GetRealRoomTypeListEvent);
			super.execute( event );
		}

		override public function result(data:Object):void
		{
			model.hotelsModule.realRoomTypeList = new ArrayCollection( data as Array );
			super.result( data );

		}
	}
}