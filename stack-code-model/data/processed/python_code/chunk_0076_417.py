package framework.controllers
{
	import flash.events.IEventDispatcher;
	
	import framework.models.BoardModel;
	import framework.views.events.CategoryDataEvent;
	
	import robotlegs.bender.bundles.mvcs.Command;
	
	public class GetCategoryDataCommand extends Command {
		
		[Inject] public var boardModel:BoardModel;
		[Inject] public var eventDispatcher:IEventDispatcher;
		
		public override function execute():void {
			
			eventDispatcher.dispatchEvent(new CategoryDataEvent(CategoryDataEvent.CATEGORIES_DATA_RETURN, boardModel.categories));
		}
	}
}