package framework.events
{
	import flash.events.Event;
	
	import framework.models.vo.BoardVO;
	
	public class UpdateBoardResultEvent extends Event
	{
		
		public static const RESULT:String = "UpdateBoardResultEvent_result";
		
		public var boardVO:BoardVO;
		
		public function UpdateBoardResultEvent(type:String, _board:BoardVO = null, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
			boardVO = _board;
		}
		
		public override function clone():Event {
			return new UpdateBoardResultEvent(type, boardVO);
		}
	}
}