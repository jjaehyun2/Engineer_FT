package framework.controllers
{
	import flash.data.SQLResult;
	
	import mx.collections.ArrayCollection;
	
	import eu.alebianco.robotlegs.utils.impl.AsyncCommand;
	
	import framework.events.BoardEvent;
	import framework.models.BoardModel;
	import framework.services.ISQLService;
	
	public class LoadBoardTasksCommand extends AsyncCommand {
		
		[Inject] public var service:ISQLService;
		[Inject] public var event:BoardEvent;
		[Inject] public var boardModel:BoardModel;
		
		public override function execute():void {
			//trace("LoadBoardTasksCommand::execute");
			service.loadTasks(event.boardId, onTasksResultHandler);
		}
		
		protected function onTasksResultHandler(ev:SQLResult):void {
			var resultCollection:ArrayCollection = new ArrayCollection(ev.data);
			boardModel.tasks = resultCollection;
			dispatchComplete(true);
			
		}
	}
}