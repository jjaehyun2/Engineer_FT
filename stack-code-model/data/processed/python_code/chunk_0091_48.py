package framework.views
{
	import framework.events.BoardDataLoadedEvent;
	import framework.events.BoardEvent;
	import framework.events.CreateCategoryEvent;
	import framework.events.StatusBarMessageEvent;
	import framework.views.events.EditCreateTaskEvent;
	import framework.views.ui.BottomBoardView;
	
	import robotlegs.bender.bundles.mvcs.Mediator;
	
	public class BottomBoardMediator extends Mediator {
		
		[Inject] public var view:BottomBoardView;
		
		public override function initialize():void {
			this.addContextListener(BoardDataLoadedEvent.CATEGORIES_LOADED, onCategoriesLoadedHandler);
			this.addContextListener(BoardEvent.BOARD_LOADED, onBoardLoaded);
			this.addContextListener(BoardEvent.BOARD_DISSABLED, onBoardDissabled);
			this.addViewListener(EditCreateTaskEvent.SHOW_TASK_PANEL, dispatch);
			this.addViewListener(CreateCategoryEvent.CREATE_CATEGORY, dispatch);
			this.addViewListener(StatusBarMessageEvent.SHOW_MESSAGE, dispatch);
		}
		
		protected function onCategoriesLoadedHandler(ev:BoardDataLoadedEvent):void {
			view.generateLegend(ev.result);
		}
		
		protected function onBoardLoaded(ev:BoardEvent):void {
			view.boardEnabled(true);
		}
		protected function onBoardDissabled(ev:BoardEvent):void {
			view.boardEnabled(false);
		}
	}
}