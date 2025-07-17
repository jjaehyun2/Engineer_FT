package services.command.roomTypes
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.roomTypes.RoomTypesDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.roomTypes.DeleteBedTypeEvent;

	public class DeleteBedTypeCommand extends BaseCommand
	{
		
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = DeleteBedTypeEvent( event );
			var delegate:RoomTypesDelegate = new RoomTypesDelegate( this );
			
			delegate.deleteBedType(_event as DeleteBedTypeEvent);
			
			super.execute(event);
		}
		
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			if (data is Array)
			{
				var items:Array = data as Array;
				model.roomTypesModule.roomBedTypes.removeAll();
				
				_event.callBack((_event as DeleteBedTypeEvent).numberOfDescription);
				
				for(var i:int = 0;i<items.length;i++)
				{
					model.roomTypesModule.roomBedTypes.addItem( items[i] );
				}
			}			
			model.appEnabled--;
		}
	}
}