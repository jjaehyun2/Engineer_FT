package framework.controllers
{
	import framework.events.CreateCategoryEvent;
	import framework.models.BoardModel;
	import framework.services.ISQLService;
	
	import robotlegs.bender.bundles.mvcs.Command;
	
	public class CreateCategoryCommand extends Command {
		
		[Inject] public var event:CreateCategoryEvent;
		[Inject] public var service:ISQLService;
		[Inject] public var boardModel:BoardModel;
		
		public override function execute():void {
			service.insertCategory(boardModel.selectedBoardId, event.color, event.title);	
		}
	}
}