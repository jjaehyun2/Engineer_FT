package services.vo.invoiceManagment
{
	import com.adobe.cairngorm.vo.IValueObject;

	[RemoteClass(alias="MapInvoiceSeach")]
	[Bindable]
	public class InvoiceSearchVO implements IValueObject
	{
		public var iInvoiceNumber:int = 0;
		public var sGuestName:String     	= "";
		public var sGuestSurName:String   	= "";
		public var sCompanyName:String   	= "";
		public var sTAName:String   		= "";
		public var sArrivalDate:String    	= "";
		public var sDepartureDate:String  	= "";
		public var iCurrentPage:int    		= 1;
  		public var iResultsPerPage:int		= 25;
  		
 		
	}
}