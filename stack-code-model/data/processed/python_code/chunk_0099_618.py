package framework.services
{
	
	import com.probertson.data.QueuedStatement;
	
	import flash.data.SQLResult;
	import flash.errors.SQLError;
	import flash.events.IEventDispatcher;
	import flash.utils.Dictionary;
	
	import framework.appConfig.Constants;
	import framework.events.BoardEvent;
	import framework.events.GlobalErrorEvent;
	import framework.models.BoardModel;
	import framework.models.vo.ContainerVO;
	import framework.models.vo.TaskVO;
	import framework.services.helper.ISQLRunnerDelegate;

	public class SQLContainerService implements ISQLContainerService
	{
		
		[Inject] public var sqlRunner:ISQLRunnerDelegate;
		[Inject] public var boardModel:BoardModel;
		[Inject] public var eventDispatcher:IEventDispatcher;
		
		private var updateId:uint = 0;
		
		public function SQLContainerService() {
		}
		
		public function createContainer(_boardId:uint, _containerVO:ContainerVO, _containerList:Array):void {
			
		
			//title, position, boardId, parentId, maxItems, type
			var statements:Vector.<QueuedStatement> = new Vector.<QueuedStatement>();
			
			statements[statements.length] = new QueuedStatement(INSERT_CONTAINER_SQL, 
				{title: "New", position: _containerVO.position, boardId: _boardId, parentId: 0, maxItems: 5, type: Constants.CONTAINER_TYPE_NORMAL});
			
			
			for(var i:uint = 0; i < _containerList.length; i++) {
				//trace("new update pos:"+(_containerList[i] as ContainerVO).position);
				var updateItem:ContainerVO = _containerList[i] as ContainerVO;
				statements[statements.length] = new QueuedStatement(UPDATE_CONTAINER_POSITION_SQL, {newPosition: updateItem.position, id: updateItem.id});
			}
			
			sqlRunner.executeModify(statements, createContainerResultHandler, onSQLErrorHandler, null);
		}
		public function deleteContainer(_containerId:uint,  _updateContainerList:Array, _updateTaskList:Array):void {
		
			var statements:Vector.<QueuedStatement> = new Vector.<QueuedStatement>();
			statements[statements.length] = new QueuedStatement(DELETE_CONTAINER_SQL, {containerId: _containerId});
			
			var backlogId:uint = boardModel.getBacklogId();
			
			for(var i:uint = 0; i < _updateContainerList.length; i++) {
				//trace("new update pos:"+(_containerList[i] as ContainerVO).position);
				var updateItem:ContainerVO = _updateContainerList[i] as ContainerVO;
				statements[statements.length] = new QueuedStatement(UPDATE_CONTAINER_POSITION_SQL, {newPosition: updateItem.position, id: updateItem.id});
			}
			
			for(var j:uint = 0; j < _updateTaskList.length; j++) {
				var item:TaskVO = _updateTaskList[j] as TaskVO;
				statements[statements.length] = new QueuedStatement(RESET_TASKS_CONTAINER_SQL, {backLogId: backlogId, oldContainer: item.containerId});
			}
			
			sqlRunner.executeModify(statements, deleteContainerResultHandler, onSQLErrorHandler, null);
		
		}
		public function updateContainer(_updateDict:Dictionary, _containerId:uint):void {
		
			var sqlText:String = "UPDATE main.Containers ";
			sqlText += "SET "
			
			for (var key:String in _updateDict) {
				sqlText += key + " = :"+key + ", ";
				
			}
			sqlText = sqlText.substring(0, sqlText.length -2);
			
			sqlText += " WHERE id = :containerId";
			
			_updateDict["containerId"] = _containerId;
			
			updateId = _containerId;
			trace(sqlText);
			
			var statements:Vector.<QueuedStatement> = new Vector.<QueuedStatement>();
			statements[statements.length] = new QueuedStatement(sqlText, _updateDict);
			sqlRunner.executeModify(statements, updateContainerResultHandler, onSQLErrorHandler, null);
		}
		
		
		private function loadContainerById(containerId:uint):void {
			sqlRunner.execute(SELECT_CONTAINER_SQL, {id:containerId}, loadContainerResultHandler, ContainerVO, onSQLErrorHandler);
		}
		protected function createContainerResultHandler(results:Vector.<SQLResult>):void {
		
			var result:SQLResult = results[0];
			if (result.rowsAffected > 0) {
				//loadContainerById(result.lastInsertRowID);
				eventDispatcher.dispatchEvent(new BoardEvent(BoardEvent.GET_BOARD_DATA, boardModel.selectedBoardId));
				
			}
		}
		protected function deleteContainerResultHandler(results:Vector.<SQLResult>):void {
			
			var result:SQLResult = results[0];
			if (result.rowsAffected > 0) {
				//loadContainerById(result.lastInsertRowID);
				eventDispatcher.dispatchEvent(new BoardEvent(BoardEvent.GET_BOARD_DATA , boardModel.selectedBoardId));
				
			}
		}
		
		protected function updateContainerResultHandler(results:Vector.<SQLResult>):void {
			var result:SQLResult = results[0];
			if (result.rowsAffected > 0 && updateId > 0) {
				loadContainerById(updateId);
				updateId = 0;
			}
		}
		protected function loadContainerResultHandler(ev:SQLResult):void {
			boardModel.updateContainer(ev.data[0] as ContainerVO);
		}
		
		protected function onSQLErrorHandler(ev:SQLError):void {
			trace("SQLService::onSQLErrorHandler");
			trace(ev.details);
			updateId = 0;
			eventDispatcher.dispatchEvent(new GlobalErrorEvent(GlobalErrorEvent.GLOBAL_ERROR, ev.details, ev.operation));
		}
		//SQL
		[Embed(source="/assets/sql/insert/InsertContainer.sql", mimeType="application/octet-stream")]
		private static const InsertContainerStatementText:Class;
		public static const INSERT_CONTAINER_SQL:String = new InsertContainerStatementText();
		
		[Embed(source="/assets/sql/update/UpdateContainerPosition.sql", mimeType="application/octet-stream")]
		private static const UpdateContainerPositionStatementText:Class;
		public static const UPDATE_CONTAINER_POSITION_SQL:String = new UpdateContainerPositionStatementText();
		
		[Embed(source="/assets/sql/select/SelectContainerById.sql", mimeType="application/octet-stream")]
		private static const SelectContainerStatementText:Class;
		public static const SELECT_CONTAINER_SQL:String = new SelectContainerStatementText();
		
		[Embed(source="/assets/sql/remove/DeleteContainer.sql", mimeType="application/octet-stream")]
		private static const DeleteContainerStatementText:Class;
		public static const DELETE_CONTAINER_SQL:String = new DeleteContainerStatementText();
		
		[Embed(source="/assets/sql/update/ResetTaskContainer.sql", mimeType="application/octet-stream")]
		private static const ResetTasksContainerStatementText:Class;
		public static const RESET_TASKS_CONTAINER_SQL:String = new ResetTasksContainerStatementText();
	}
}