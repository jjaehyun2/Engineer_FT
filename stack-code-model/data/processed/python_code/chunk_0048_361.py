package framework.events
{
	import flash.events.Event;
	
	import mx.collections.ArrayCollection;
	
	public class BoardDataLoadedEvent extends Event
	{
		public static const BOARDS_LOADED:String = "BoardDataLoadedEvent_boardsLoaded";
		public static const CONTAINERS_LOADED:String = "BoardDataLoadedEvent_containersLoaded";
		public static const TASKS_LOADED:String = "BoardDataLoadedEvent_tasksLoaded";
		public static const CATEGORIES_LOADED:String = "BoardDataLoadedEvent_categoriesLoaded";
		
		public var result:ArrayCollection;
		public var selectBoardId:uint;
		
		public function BoardDataLoadedEvent(type:String, _result:ArrayCollection = null, _boardId:uint = 0, bubbles:Boolean=false, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
			result = _result;
			selectBoardId = _boardId;
		}
		
		public override function clone():Event {
			return new BoardDataLoadedEvent(type, result, selectBoardId);
		}
	}
}