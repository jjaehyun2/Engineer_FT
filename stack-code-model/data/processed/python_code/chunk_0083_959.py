package services.command.hotels
{
	import com.adobe.cairngorm.commands.ICommand;
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.backend.GetHotelRoomListDelegate;
	import services.events.backend.GetHotelRoomListEvent;
	import framework.model.AppModelLocator;
	
	import mx.collections.ArrayCollection;
	import mx.controls.Alert;
	import mx.rpc.IResponder;

	public class GetHotelRoomListCommand implements ICommand, IResponder
	{
		private var model:AppModelLocator = AppModelLocator.getInstance();
		
		public function execute(event:CairngormEvent):void
		{
			var evt:GetHotelRoomListEvent = GetHotelRoomListEvent( event );
			var delegate:GetHotelRoomListDelegate = new GetHotelRoomListDelegate( this );
			
			delegate.getHotelRoomList( evt );
		}
		
		public function result(data:Object):void
		{
			model.hotelsModule.roomDP = new ArrayCollection( data as Array );
			
			model.appEnabled--;
		}
		
		public function fault(info:Object):void
		{
			Alert.show("Get Hotel Room List failed");
			
			model.appEnabled--;
		}
		
	}
}