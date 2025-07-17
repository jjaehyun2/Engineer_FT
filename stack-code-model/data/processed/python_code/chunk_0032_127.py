package services.command.roomTypes
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.roomTypes.RoomTypesDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.roomTypes.GetRoomTypesDataEvent;
	
	import mx.collections.ArrayCollection;
	import mx.controls.Alert;

	public class GetRoomTypesDataCommand extends BaseCommand
	{
		override public function execute(event:CairngormEvent):void
		{
			_event = GetRoomTypesDataEvent( event );
			var delegate:RoomTypesDelegate = new RoomTypesDelegate( this );
			 
			delegate.getRoomTypesData();
			super.execute( event );
		}
		
 		override public function result(data:Object):void
		{
			var items:ArrayCollection = new ArrayCollection( data as Array );
			model.roomTypesModule.maxRoomTypesItems = items.length;

			model.roomTypesModule.roomTypesDP.removeAll();
			model.roomTypesModule.roomTypesDP = items;
			super.result( data );
		}
		
	}
}