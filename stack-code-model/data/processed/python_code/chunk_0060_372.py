package services.command.invoiceManagment
{
	import com.adobe.cairngorm.control.CairngormEvent;

	import services.business.invoiceManagment.InvoiceManagmentDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.invoiceManagment.GetInvoiceListEvent;
	import services.vo.checkOut.GridComponentVO;

	public class GetInvoiceListCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = GetInvoiceListEvent(event);
			var delegate:InvoiceManagmentDelegate = new InvoiceManagmentDelegate(this);
			delegate.getInvoiceList(_event as GetInvoiceListEvent);

			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			var context:GridComponentVO = data as GridComponentVO;
			model.invoiceManagmentModule.invoicesCount = context.iTotalPage;
			model.invoiceManagmentModule.invoices = context.oGridData; // InvoiceListVO


			super.result(data);
		}
	}
}