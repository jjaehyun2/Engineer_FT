package services.command.common
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.common.GetVipHotelListDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.common.GetVipHotelListEvent;
	import services.vo.GlobalStorage;
	
	import mx.collections.ArrayCollection;

	public class GetVipHotelListCommand extends BaseCommand
	{
		override public function execute(event:CairngormEvent):void
		{
			var evt:GetVipHotelListEvent = GetVipHotelListEvent( event );
			var delegate:GetVipHotelListDelegate = new GetVipHotelListDelegate( this );
			delegate.getVIPHotelList(evt as GetVipHotelListEvent);
			
			super.execute(event);
		}
		
		override public function result(data:Object):void
		{
			GlobalStorage.vipHotel = new ArrayCollection(data as Array);
			
			super.result(data);
		}
	}
}