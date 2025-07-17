package services.command.checkOut
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.checkOut.CheckOutDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.checkOut.AddPaymentsEvent;
	import services.vo.checkOut.itemRouting.ItemCheckOutVO;
	import services.vo.checkOut.payment.CheckoutPaymentVO;
	import services.vo.inHouse.CheckOutReportsListVO;

	public class AddPaymentsCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = AddPaymentsEvent(event);
			var delegate:CheckOutDelegate = new CheckOutDelegate(this);
			delegate.addPayments(_event as AddPaymentsEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			for each(var reportList:CheckOutReportsListVO in (data as Array))
			{
				var payment:CheckoutPaymentVO = reportList.oMapPayment;
				var item:ItemCheckOutVO = new ItemCheckOutVO();
				item.lId = payment.lId;
				item.fPrice = payment.fValue;
				item.dDate = payment.dDate;
				item.sTransName = payment.sName;
				item.iPaymentType = payment.iType;
				item.bIsChecked = true;
				item.bIsPayment = true;
				
				model.checkOutModule.routingItems.addItem(item);
			}
			
			// TO DO : 
			super.result(data);
		}
	}
}