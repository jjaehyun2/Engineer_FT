package framework.events
{
	import flash.events.Event;
	
	import framework.models.vo.BoardVO;
	
	public class CreateUpdateBoardEvent extends Event {
		
		public static const CREATE:String = "CreateUpdateBoardEvent_create";
		public static const UPDATE:String = "CreateUpdateBoardEvent_update";
		
		public var boardVO:BoardVO;
		public var catFromBoardId:uint;
		
		public function CreateUpdateBoardEvent(type:String, _boardVO:BoardVO = null, _catFromBoardId:uint = 0, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super(type, bubbles, cancelable);
			boardVO = _boardVO;
			catFromBoardId = _catFromBoardId;
		}
		
		public override function clone():Event {
			return new CreateUpdateBoardEvent(type, boardVO, catFromBoardId);
		}
	}
}