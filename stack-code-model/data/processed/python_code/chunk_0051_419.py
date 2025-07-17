package services.command.backend
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.backend.GetHotelCommonRoomTypesDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.backend.GetHotelCommonRoomTypesEvent;
	import services.vo.backend.RoomQualityObjectVO;
	
	import mx.collections.ArrayCollection;

	public class GetHotelCommonRoomTypesCommand extends BaseCommand
	{
		override public function execute(event:CairngormEvent):void
		{
			_event = GetHotelCommonRoomTypesEvent( event );
			var delegate:GetHotelCommonRoomTypesDelegate = new GetHotelCommonRoomTypesDelegate( this );
			
			delegate.getHotelCommonRoomTypes( _event as  GetHotelCommonRoomTypesEvent);
			
			model.ratesModule.barModule.isBarEnabled = true;
			
			super.execute( event );
		}
		
		override public function result(data:Object):void
		{
			var items:ArrayCollection = new ArrayCollection( data as Array );
			model.roomTypesModule.maxRoomTypesItems = items.length;
			model.roomTypesModule.roomTypesForRates.removeAll();
			for(var i:int = 0; i < items.length; i++)
			{				
				model.roomTypesModule.roomTypesForRates.addItem( items.getItemAt(i) as RoomQualityObjectVO);
			}
			super.result( data ); 
		}
		
		
	}
}