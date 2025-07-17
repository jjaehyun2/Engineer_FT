package services.command.roomTypes
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.roomTypes.RoomTypesDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.roomTypes.SetRoomTypeCapacityEvent;

	public class SetRoomTypeCapacityCommand extends BaseCommand
	{	
		override public function execute(event:CairngormEvent):void
		{
			_event = SetRoomTypeCapacityEvent( event );
			var delegate:RoomTypesDelegate = new RoomTypesDelegate( this );
			delegate.setRoomTypeCapacity(_event as SetRoomTypeCapacityEvent);
			super.execute( event );
		}
		
		override public function result(data:Object):void
		{
			super.result( data );
		}	
		
	}
}