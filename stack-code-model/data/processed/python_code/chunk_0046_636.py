package framework.events
{
	import flash.events.Event;
	import flash.utils.Dictionary;
	
	public class UpdateTaskEvent extends Event {
		
		public static const UPDATE_TASK:String = "UpdateTaskEvent_updateTask";
		public static const UPDATE_TASK_BOARD_ID:String = "UpdateTaskEvent_UpdateTaskBoardId";
		public var taskId:uint;
		public var paramDict:Dictionary;
		
		public function UpdateTaskEvent(type:String, _taskId:uint = 0, _paramDict:Dictionary = null, bubbles:Boolean=false, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
			taskId = _taskId;
			paramDict = _paramDict;
		}
		
		public override function clone():Event {
			return new UpdateTaskEvent(type, taskId, paramDict);
		}
	}
}