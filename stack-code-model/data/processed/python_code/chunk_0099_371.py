package services.command.items.management
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.items.ItemsDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.items.management.GetAllowedHotelsEvent;
	import services.vo.items.AllowedHotelsVO;
	import services.vo.hotels.HotelInfoTotalVO;
	
	import mx.collections.ArrayCollection;

	public class GetAllowedHotelsCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = GetAllowedHotelsEvent(event);
			var delegate:ItemsDelegate = new ItemsDelegate(this);
			delegate.getAllowedHotels(_event as GetAllowedHotelsEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			model.transactionModule.allowedHotels = new ArrayCollection();
			
			var res:AllowedHotelsVO = data as AllowedHotelsVO;
			var hotel:HotelInfoTotalVO;
			var i:int = 0;
			
			if (res)
			{
				if (res.bIsSystemAllowed)
				{
					var system:HotelInfoTotalVO = new HotelInfoTotalVO();
					system.iHotelId = -1;
					system.sHotelName = "Basic List";
					model.transactionModule.allowedHotels.addItem(system);
					
					for (i = 0; i < model.hotelsModule.hotels.length; i++)
					{
						hotel = model.hotelsModule.hotels.getItemAt(i) as HotelInfoTotalVO;
						model.transactionModule.allowedHotels.addItem(hotel);
					}
				}
				else
				{
					var hotels:Array = res.aAllowedHotelsId;
					var len:int = (hotels) ? hotels.length : 0;
					for(i = 0; i < len; i++)
					{
						for (var j:int = 0; j < model.hotelsModule.hotels.length; j++)
						{
							hotel = model.hotelsModule.hotels.getItemAt(j) as HotelInfoTotalVO;
							if (hotel.iHotelId == hotels[i])
								model.transactionModule.allowedHotels.addItem(hotel);
						}
					}
				}
			}
			
			super.result(data);
		}
	}
}