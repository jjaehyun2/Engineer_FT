package framework.controllers
{
	import flash.net.SharedObject;
	
	import framework.events.SharedObjectEvent;
	import framework.models.BoardModel;
	import framework.models.vo.SharedObjectVO;
	
	import robotlegs.bender.bundles.mvcs.Command;
	
	public class SaveSharedObjectCommand extends Command {
		
		//[Inject] public var sharedObj:SharedObjectVO;
		[Inject] public var event:SharedObjectEvent;
		[Inject] public var boardModel:BoardModel;
		
		public override function execute():void {
			var sO:SharedObject = SharedObject.getLocal("KanbanApp");
			sO.data[event.key] = event.value;
			
			if(event.flushFlag)
				sO.flush();
			
			if(event.key == SharedObjectVO.FINISHED_TASK_VIEW_MODE)
				boardModel.FINISHED_TASKS_VIEW_MODE = event.value;
		}
	}
}