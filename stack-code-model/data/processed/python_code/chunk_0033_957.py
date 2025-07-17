package framework.controllers
{
	
	import flash.events.IEventDispatcher;
	
	import framework.events.DeleteCategoryEvent;
	import framework.events.StatusBarMessageEvent;
	import framework.models.BoardModel;
	import framework.services.ISQLService;
	
	import robotlegs.bender.bundles.mvcs.Command;
	
	public class DeleteCategoryCommand extends Command {
		
		[Inject] public var service:ISQLService;
		[Inject] public var event:DeleteCategoryEvent;
		[Inject] public var boardModel:BoardModel;
		[Inject] public var eventDispatcher:IEventDispatcher;
		
		public override function execute():void {
			
			service.deleteCategory(event.categoryId);
			
			/*if(boardModel.categories.length > 1) {
				
			} else {
				eventDispatcher.dispatchEvent(new StatusBarMessageEvent(StatusBarMessageEvent.SHOW_MESSAGE, "The last category can not be deleted."));
			}*/
				
		}
		
	}
}