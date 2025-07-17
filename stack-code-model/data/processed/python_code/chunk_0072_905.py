package services.command.roomTypes
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import flash.utils.Dictionary;
	
	import services.business.roomTypes.RoomTypesDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.roomTypes.GetRoomTypesPageEvent;
	
	import mx.collections.ArrayCollection;

	public class GetRoomTypesPageCommand extends BaseCommand
	{
		override public function execute(event:CairngormEvent):void
		{
			_event = GetRoomTypesPageEvent( event );
			var delegate:RoomTypesDelegate = new RoomTypesDelegate( this );
			 
			delegate.getPage();
			super.execute( event );
		}
		
 		override public function result(data:Object):void
		{
			var items:Dictionary = new Dictionary(data as Array);
			var test:Array = data['ROOM_TYPES'];// it's hack
			model.roomTypesModule.maxRoomTypesItems = (data['ROOM_TYPES'] as Array).length ;

			model.roomTypesModule.roomTypesDP.removeAll();
			model.roomTypesModule.roomTypesDP = new ArrayCollection(data['ROOM_TYPES'] as Array);
			model.roomTypesModule.roomBedTypes = new ArrayCollection(data['BED_TYPES'] as Array);
			super.result( data );
		}		
	}
}