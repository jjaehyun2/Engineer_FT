package services.events.checkOut
{
	import services.cairngorm.BaseEvent;
	import services.vo.checkOut.CheckOutSearchVO;

	public class GetGuestListEvent extends BaseEvent
	{
		public var checkOutSearch:CheckOutSearchVO = new CheckOutSearchVO();
		public var currentPage:int = 1;
		public var countOnPage:int = 20;
		public var searchType:Boolean = false;
		public var hotelId:int;
	
		
		public function GetGuestListEvent(type:String)
		{
			super(type);
		}
		
	}
}