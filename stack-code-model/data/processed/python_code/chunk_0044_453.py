package framework.services
{
	import flash.utils.Dictionary;
	
	import framework.models.vo.TaskVO;

	public interface ISQLTaskService {
		function updateTask(_updateDict:Dictionary, _taskId:uint):void;
		function updateTask2(_columnId:String, _columnValue:*, _taskId:uint, _resultHandler:Function = null):void;
		function updateTaskBoardId(_taskId:uint, _boardId:uint):void;
		function insertTask(_task:TaskVO):void;
		function deleteTask(_taskId:uint):void;
		//function updateTasksForCategory(_oldCategoryId:uint, _newCategoryId:uint):void;
	}
}