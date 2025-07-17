package services.command.checkOut
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.checkOut.CheckOutDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.checkOut.GetCheckoutStateFromInHouseEvent;
	import services.vo.checkOut.itemRouting.AppliedItemsVO;
	import services.vo.checkOut.itemRouting.CheckoutInfoFullVO;

	public class GetCheckoutStateFromInHouseCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = GetCheckoutStateFromInHouseEvent(event);
			var delegate:CheckOutDelegate = new CheckOutDelegate(this);
			delegate.getCheckoutStateFromInHouse(_event as GetCheckoutStateFromInHouseEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			var appliedItem:AppliedItemsVO;
			
			model.checkOutModule.reservationSummary = (data as CheckoutInfoFullVO).oMapReservationSummary;
			model.checkOutModule.updateCheckOutState((data as CheckoutInfoFullVO).oMapItemsRouting);
			
			super.result(data);
		}
	}
}