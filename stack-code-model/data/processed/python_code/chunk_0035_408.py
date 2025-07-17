package services.command.invoiceManagment
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.invoiceManagment.InvoiceManagmentDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.invoiceManagment.GetInvoiceFileEvent;

	public class GetInvoiceFileCommand extends BaseCommand
	{
		override public function execute(event:CairngormEvent):void
		{
			_event = GetInvoiceFileEvent(event);
			var delegate:InvoiceManagmentDelegate = new InvoiceManagmentDelegate(this);
			delegate.getInvoiceFile(_event as GetInvoiceFileEvent);
			
			super.execute(event);
		}

		override public function result(data:Object):void
		{
			model.invoiceManagmentModule.aIinvoiceFileURL = data as Array; // 
			
			super.result(data);
		}		
	}
}