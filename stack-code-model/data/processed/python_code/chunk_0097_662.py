package services.events.rates.packages
{
	import services.controller.AppController;
	import services.cairngorm.BaseEvent;

	/**
	* The GetTransactionGroupListEvent class is
	*
	* @author Anton Kirzyk / Ramada
	*
	* @version $Revision 1.0 $ $Date: 2009-07-18 11:52:03 +0300 (Сб, 18 июл 2009) $
	*
	*/
	public class GetTransactionGroupListEvent extends BaseEvent
	{
		public var sGroupName:String;
		public var iHotelId:int;

		public function GetTransactionGroupListEvent(type:String, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(AppController.PACKAGES_GET_TRANSACTION_GROUP_LIST_EVENT, bubbles, cancelable);
		}

	}
}