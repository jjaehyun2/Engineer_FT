package services.events.search
{
	import services.controller.AppController;
	import services.cairngorm.BaseEvent;
	import services.vo.search.RsvSearchRequestVO;

	public class ExecuteSearchEvent extends BaseEvent
	{
		public var rsvSearchReqest:RsvSearchRequestVO = new RsvSearchRequestVO();

		public function ExecuteSearchEvent(bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(AppController.EXECUTE_RESERVATION_SEARCH, bubbles, cancelable);
		}

	}
}