package framework.appConfig
{
	import flash.events.IEventDispatcher;
	import flash.filesystem.File;
	
	import mx.controls.FlexNativeMenu;
	import mx.core.IVisualElementContainer;
	
	import spark.components.WindowedApplication;
	
	import framework.controllers.BoardPositionChangedCommand;
	import framework.controllers.CreateBoardCommand;
	import framework.controllers.CreateCategoryCommand;
	import framework.controllers.CreateContainerCommand;
	import framework.controllers.CreateTaskCommand;
	import framework.controllers.DeleteBoardCommand;
	import framework.controllers.DeleteCategoryCommand;
	import framework.controllers.DeleteContainerCommand;
	import framework.controllers.DeleteTaskCommand;
	import framework.controllers.EditCreateTaskCommand;
	import framework.controllers.GetCategoryDataCommand;
	import framework.controllers.LoadBoardsCommand;
	import framework.controllers.SaveSharedObjectCommand;
	import framework.controllers.ShowErrorCommand;
	import framework.controllers.StartupCommand;
	import framework.controllers.UpdateBoardCommand;
	import framework.controllers.UpdateCategoryCommand;
	import framework.controllers.UpdateContainerCommand;
	import framework.controllers.UpdateTaskBoardIdCommand;
	import framework.controllers.UpdateTaskCommand;
	import framework.controllers.guards.NotLastCategory;
	import framework.controllers.macros.BoardDataMacro;
	import framework.events.BoardEvent;
	import framework.events.ButtonPositionChangedEvent;
	import framework.events.CreateCategoryEvent;
	import framework.events.CreateContainerEvent;
	import framework.events.CreateTaskEvent;
	import framework.events.CreateUpdateBoardEvent;
	import framework.events.DatabaseEvent;
	import framework.events.DeleteCategoryEvent;
	import framework.events.DeleteContainerEvent;
	import framework.events.DeleteTaskEvent;
	import framework.events.GlobalErrorEvent;
	import framework.events.SharedObjectEvent;
	import framework.events.UpdateCategoryEvent;
	import framework.events.UpdateContainerEvent;
	import framework.events.UpdateTaskEvent;
	import framework.models.BoardModel;
	import framework.models.vo.SharedObjectVO;
	import framework.services.ISQLContainerService;
	import framework.services.ISQLService;
	import framework.services.ISQLTaskService;
	import framework.services.SQLContainerService;
	import framework.services.SQLService;
	import framework.services.SQLTaskService;
	import framework.services.helper.DatabaseCreator;
	import framework.services.helper.ISQLRunnerDelegate;
	import framework.services.helper.SQLRunnerDelegate;
	import framework.views.BoardTabMediator;
	import framework.views.BoardViewMediator;
	import framework.views.BottomBoardMediator;
	import framework.views.CreateTaskMediator;
	import framework.views.LegendItemMediator;
	import framework.views.NativeMenuMediator;
	import framework.views.TaskContainerMediator;
	import framework.views.TestViewMediator;
	import framework.views.events.CategoryDataEvent;
	import framework.views.events.EditCreateTaskEvent;
	import framework.views.ui.BoardTabView;
	import framework.views.ui.BoardView;
	import framework.views.ui.BottomBoardView;
	import framework.views.ui.CreateTaskView;
	import framework.views.ui.LegendItem;
	import framework.views.ui.TaskContainerView;
	import framework.views.ui.TestView;
	
	import robotlegs.bender.extensions.contextView.ContextView;
	import robotlegs.bender.extensions.eventCommandMap.api.IEventCommandMap;
	import robotlegs.bender.extensions.mediatorMap.api.IMediatorMap;
	import robotlegs.bender.extensions.viewProcessorMap.api.IViewProcessorMap;
	import robotlegs.bender.framework.api.IConfig;
	import robotlegs.bender.framework.api.IContext;
	import robotlegs.bender.framework.api.IInjector;
	
	
	public class AppConfig implements IConfig {
		
		[Inject] public var context:IContext;
		[Inject] public var injector:IInjector;
		[Inject] public var mediatorMap:IMediatorMap;
		[Inject] public var commandMap:IEventCommandMap;
		[Inject] public var viewProcessorMap:IViewProcessorMap;
		[Inject] public var contextView:ContextView;
		[Inject] public var eventDispatcher:IEventDispatcher;
		
		
		private static const DB_FILE_NAME:String = "Kanban_01.db";
		//private static const DB_FILE_NAME:String = "Kanban_Test_02.db";
		
		
		public function configure():void {
			
			mediatorMap.map(Kanban).toMediator(KanbanMediator);
			mediatorMap.map(TestView).toMediator(TestViewMediator);
			mediatorMap.map(BoardTabView).toMediator(BoardTabMediator);
			mediatorMap.map(BoardView).toMediator(BoardViewMediator);
			mediatorMap.map(BottomBoardView).toMediator(BottomBoardMediator);
			mediatorMap.map(TaskContainerView).toMediator(TaskContainerMediator);
			mediatorMap.map(CreateTaskView).toMediator(CreateTaskMediator);
			mediatorMap.map(LegendItem).toMediator(LegendItemMediator);
			
			mediatorMap.map(FlexNativeMenu).toMediator(NativeMenuMediator);
			
			injector.map(ISQLService).toSingleton(SQLService);
			injector.map(ISQLTaskService).toSingleton(SQLTaskService);
			injector.map(ISQLContainerService).toSingleton(SQLContainerService);
			
			injector.map(BoardModel).asSingleton();
			
			injector.map(SharedObjectVO).toType(SharedObjectVO);
			
			viewProcessorMap.map(BoardView).toInjection();
			viewProcessorMap.map(TaskContainerView).toInjection();
			
			//Service commands
			
			commandMap.map(DatabaseEvent.DATABASE_READY).toCommand(StartupCommand); //was loadBoardsCommand
			commandMap.map(DatabaseEvent.DATABASE_RELOAD).toCommand(LoadBoardsCommand);
			commandMap.map(BoardEvent.GET_BOARD_DATA).toCommand(BoardDataMacro);
			commandMap.map(UpdateTaskEvent.UPDATE_TASK).toCommand(UpdateTaskCommand);
			commandMap.map(UpdateTaskEvent.UPDATE_TASK_BOARD_ID).toCommand(UpdateTaskBoardIdCommand);
			commandMap.map(CreateTaskEvent.CREATE_TASK).toCommand(CreateTaskCommand);
			commandMap.map(DeleteTaskEvent.DELETE_TASK).toCommand(DeleteTaskCommand);
			commandMap.map(CreateCategoryEvent.CREATE_CATEGORY).toCommand(CreateCategoryCommand);
			commandMap.map(UpdateCategoryEvent.UPDATE_CATEGORY).toCommand(UpdateCategoryCommand);
			commandMap.map(CreateContainerEvent.CREATE).toCommand(CreateContainerCommand);
			commandMap.map(DeleteContainerEvent.DELETE).toCommand(DeleteContainerCommand);
			commandMap.map(UpdateContainerEvent.UPDATE).toCommand(UpdateContainerCommand);
			commandMap.map(CreateUpdateBoardEvent.CREATE).toCommand(CreateBoardCommand);
			commandMap.map(CreateUpdateBoardEvent.UPDATE).toCommand(UpdateBoardCommand);
			commandMap.map(BoardEvent.DELETE).toCommand(DeleteBoardCommand);
			commandMap.map(ButtonPositionChangedEvent.POSITION_CHANGED).toCommand(BoardPositionChangedCommand);
			//Model commands
			commandMap.map(CategoryDataEvent.GET_CATEGORIES_DATA).toCommand(GetCategoryDataCommand);
			
			//Guarded
			commandMap.map(DeleteCategoryEvent.DELETE).toCommand(DeleteCategoryCommand).withGuards(NotLastCategory);
			
			//App commands
			commandMap.map(EditCreateTaskEvent.SHOW_TASK_PANEL).toCommand(EditCreateTaskCommand);
			commandMap.map(SharedObjectEvent.SAVE).toCommand(SaveSharedObjectCommand);
			commandMap.map(GlobalErrorEvent.GLOBAL_ERROR).toCommand(ShowErrorCommand);
			context.afterInitializing(init);
			
		}
		
		protected function init():void {
			//Bootstrap
			var dbFile:File = File.applicationStorageDirectory.resolvePath(DB_FILE_NAME);
			var sqlRunner:ISQLRunnerDelegate = new SQLRunnerDelegate(dbFile);
			
			
			
			injector.map(ISQLRunnerDelegate).toValue(sqlRunner);
			
			
			if (!dbFile.exists) {
				//var creator:DatabaseCreator = injector.instantiate(DatabaseCreator);
				injector.map(DatabaseCreator);
				var creator:DatabaseCreator = injector.getInstance(DatabaseCreator);
				creator.createDBStructure();
			}
			else {
				trace("AppConfig::configure -> db exists allready");
				eventDispatcher.dispatchEvent(new DatabaseEvent(DatabaseEvent.DATABASE_READY));
				
			}
			
			
			//(contextView.view as IVisualElementContainer).addElement(new TestView());
		}
	}
}