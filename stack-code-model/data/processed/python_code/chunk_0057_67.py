package framework.events
{
	import flash.events.Event;
	
	public class DeleteTaskEvent extends Event {
		
		public static const DELETE_TASK:String = "DeleteTaskEvent_deleteTask";
		public var taskId:uint;
		
		public function DeleteTaskEvent(type:String, _taskId:uint, bubbles:Boolean=false, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
			taskId = _taskId;
		}
		
		public override function clone():Event {
			return new DeleteTaskEvent(type, taskId);
		}
	}
}