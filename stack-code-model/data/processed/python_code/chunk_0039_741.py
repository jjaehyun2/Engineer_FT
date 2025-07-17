package services.vo.inHouse
{
	import services.vo.MapValueObject;
	import services.vo.checkOut.payment.CheckoutPaymentVO;
	
	[RemoteClass(alias="MapCheckOutReportsList")]
	public class CheckOutReportsListVO extends MapValueObject
	{
		/**
		 *  This property is list of check out's reports by
		 *  debitor's accounts.
		 *  
		 *  @default []
		 *  
		 *  @see framework.vo.inHouse.CheckOutReportsVO
		 */
		public var aCheckOutReports:/* CheckOutReportsVO */Array = [];
		/**
		 *  This proeprty is URL to report.
		 */
		public var sActualReport:String = "";
		/**
		 *  
		 *  @default new CheckoutPaymentVO()
		 *  
		 *  @see framework.vo.checkOut.itemRouting.CheckoutPaymentVO
		 */
		public var oMapPayment:CheckoutPaymentVO = new CheckoutPaymentVO();
	}
}