package framework.controllers
{
	import framework.events.CreateTaskEvent;
	import framework.models.BoardModel;
	import framework.models.vo.TaskVO;
	import framework.services.ISQLTaskService;
	
	import robotlegs.bender.bundles.mvcs.Command;
	
	public class CreateTaskCommand extends Command {
		
		[Inject] public var event:CreateTaskEvent;
		[Inject] public var service:ISQLTaskService;
		[Inject] public var model:BoardModel;
		
		public override function execute():void {
			var newTask:TaskVO = event.task;
			newTask.boardId = model.selectedBoardId;
			newTask.containerId = model.getBacklogId();
			
			service.insertTask(event.task);
		}
	}
}