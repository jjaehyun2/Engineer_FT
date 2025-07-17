package services.events.rates.packages
{
	import services.controller.AppController;
	import services.cairngorm.BaseEvent;
	import services.vo.backend.PackageItemVO;
	/**
	* The DeleteTransactionEvent class is 
	*
	* @author Anton Kirzyk / Ramada
	*
	* @version $Revision 1.0 $ $Date: 2009-07-18 11:52:03 +0300 (Сб, 18 июл 2009) $
	*
	*/
	public class DeleteTransactionEvent extends BaseEvent
	{
		public var iPackageId:int;
		public var iTransactionToDeleteId:int;
		public var transactionForDelete:PackageItemVO;
		
		public function DeleteTransactionEvent(bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(AppController.PACKAGES_DELETE_TRANSACTION_EVENT, bubbles, cancelable);
		}
		
	}
}