package services.command.checkOut
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.checkOut.CheckOutDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.checkOut.AddDebitorPaymentEvent;
	import services.vo.checkOut.itemRouting.ItemCheckOutVO;
	import services.vo.checkOut.payment.CheckoutPaymentVO;

	public class AddDebitorPaymentCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = AddDebitorPaymentEvent(event);
			var delegate:CheckOutDelegate = new CheckOutDelegate(this);
			delegate.addDebitorPayment(_event as AddDebitorPaymentEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			var payment:CheckoutPaymentVO = data as CheckoutPaymentVO;
			
			// add new debitor payments by account
			var paymentItem:ItemCheckOutVO = new ItemCheckOutVO();
			paymentItem.lId = payment.lId;
			paymentItem.fPrice = payment.fValue;
			paymentItem.dDate = payment.dDate;
			paymentItem.sTransName = payment.sName;
			paymentItem.iPaymentType = payment.iType;
			paymentItem.lAppliedPayment = payment.lAppliedPayment;
			paymentItem.bIsChecked = true;
			paymentItem.bIsPayment = true;
				
			model.checkOutModule.routingItems.addItem(paymentItem);
			model.checkOutModule.routedPaymentItems.addItem(payment);
			
			super.result(data);
		}
	}
}