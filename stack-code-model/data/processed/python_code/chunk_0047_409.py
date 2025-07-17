package framework.services.helper
{
	import com.probertson.data.QueuedStatement;
	
	import flash.data.SQLResult;
	import flash.errors.SQLError;
	import flash.events.IEventDispatcher;
	import flash.events.SQLErrorEvent;
	
	import framework.events.DatabaseEvent;
	import framework.models.BoardModel;
	
	public class DatabaseCreator
	{
		
		[Inject] public var sqlRunner:ISQLRunnerDelegate;
		[Inject] public var eventDispatcher:IEventDispatcher;
		[Inject] public var boardModel:BoardModel;
		
		private var createdBoardId:uint = 0;
		private var copyCatFromBoardId:uint = 0;
		
		public function DatabaseCreator() {
			
		}
		
		public function createDBStructure():void {
			
			var statements:Vector.<QueuedStatement> = new Vector.<QueuedStatement>();
			statements[statements.length] = new QueuedStatement(CREATE_BOARDS_SQL);
			statements[statements.length] = new QueuedStatement(CREATE_CONTAINERS_SQL);
			statements[statements.length] = new QueuedStatement(CREATE_TASKS_SQL);
			statements[statements.length] = new QueuedStatement(CREATE_ATTACHEMENTS_SQL);
			statements[statements.length] = new QueuedStatement(CREATE_CATEGORIES_SQL);
			
			/*statements[statements.length] = new QueuedStatement(INSERT_BOARDS_DEFAULT_SQL);
			statements[statements.length] = new QueuedStatement(INSERT_CONTAINERS_DEFAULT_SQL);
			statements[statements.length] = new QueuedStatement(INSERT_CATEGORIES_DEFAULT_SQL);
			statements[statements.length] = new QueuedStatement(INSERT_TASKS_DEFAULT_SQL);*/
			
			sqlRunner.executeModify(statements, executeBatchCompleteHandler, executeBatchErrorHandler, null);
		}
		
		public function createNewBoard(_title:String = "", _position:uint = 0, _copyCatId:uint = 0):void {
			if(_title == "")
				_title = "My kanban board";
			
			copyCatFromBoardId = _copyCatId;
			
			var statements:Vector.<QueuedStatement> = new Vector.<QueuedStatement>();
			statements[statements.length] = new QueuedStatement(INSERT_BOARDS_DEFAULT_SQL2, {title: _title, position: _position});
			sqlRunner.executeModify(statements,createBoardResultHandler, executeBatchErrorHandler, null);
		}
		
		
		private function insertContainers(_boardId:uint):void {
			var statements:Vector.<QueuedStatement> = new Vector.<QueuedStatement>();
			statements[statements.length] = new QueuedStatement(INSERT_CONTAINERS_DEFAULT_SQL2, {boardId: _boardId});
			if(copyCatFromBoardId == 0)
				statements[statements.length] = new QueuedStatement(INSERT_CATEGORIES_DEFAULT_SQL2, {boardId: _boardId});
			else
				statements[statements.length] = new QueuedStatement(INSERT_CATEGORIES_FROM_BOARD_SQL, {newBoardId: _boardId, copyFromBoardId: copyCatFromBoardId});
			
			sqlRunner.executeModify(statements,insertContainersResultHandler, executeBatchErrorHandler, null);
		}
		protected function createBoardResultHandler(results:Vector.<SQLResult>):void {
			var result:SQLResult = results[0] as SQLResult;
			if(result.rowsAffected > 0) {
				createdBoardId = result.lastInsertRowID;
				boardModel.requestBoardId = createdBoardId;
				insertContainers(createdBoardId);
			}
		}
		protected function insertContainersResultHandler(results:Vector.<SQLResult>):void {
			var resultContainers:SQLResult = results[0] as SQLResult;
			var resultCategories:SQLResult = results[1] as SQLResult;
			if(resultContainers.rowsAffected > 0 && resultCategories.rowsAffected > 0) {
				//eventDispatcher.dispatchEvent(new DatabaseEvent(DatabaseEvent.DATABASE_READY));
				eventDispatcher.dispatchEvent(new DatabaseEvent(DatabaseEvent.DATABASE_RELOAD));
				createdBoardId = 0;
			}
		}
		private function executeBatchCompleteHandler(results:Vector.<SQLResult>):void {
			trace("DatabaseCreator::executeBatchCompleteHandler");
			//eventDispatcher.dispatchEvent(new DatabaseEvent(DatabaseEvent.DATABASE_READY));
			createNewBoard();
		}
		
		
		private function executeBatchErrorHandler(error:SQLError):void {
			eventDispatcher.dispatchEvent(new SQLErrorEvent(SQLErrorEvent.ERROR, false, false, error));
			trace("DatabaseCreator::executeBatchErrorHandler");
			trace(error.details);
		}
		//SQL Statements
		
		[Embed(source="/assets/sql/create/CreateBoardsTable.sql", mimeType="application/octet-stream")]
		private static const CreateBoardsStatementClass:Class;
		public static const CREATE_BOARDS_SQL:String = new CreateBoardsStatementClass();
		
		[Embed(source="/assets/sql/create/CreateContainersTable.sql", mimeType="application/octet-stream")]
		private static const CreateContainersStatementClass:Class;
		public static const CREATE_CONTAINERS_SQL:String = new CreateContainersStatementClass();
		
		[Embed(source="/assets/sql/create/CreateTasksTable.sql", mimeType="application/octet-stream")]
		private static const CreateTasksStatementClass:Class;
		public static const CREATE_TASKS_SQL:String = new CreateTasksStatementClass();
		
		[Embed(source="/assets/sql/create/CreateAttachementsTable.sql", mimeType="application/octet-stream")]
		private static const CreateAttachementsStatementClass:Class;
		public static const CREATE_ATTACHEMENTS_SQL:String = new CreateAttachementsStatementClass();
		
		[Embed(source="/assets/sql/create/CreateCategoriesTable.sql", mimeType="application/octet-stream")]
		private static const CreateCategoriesStatementClass:Class;
		public static const CREATE_CATEGORIES_SQL:String = new CreateCategoriesStatementClass();
		
		[Embed(source="/assets/sql/create/InsertBoardsDefault.sql", mimeType="application/octet-stream")]
		private static const InsertBoardsDefaultStatementClass:Class;
		public static const INSERT_BOARDS_DEFAULT_SQL:String = new InsertBoardsDefaultStatementClass();
		
		[Embed(source="/assets/sql/create/InsertBoardsDefault2.sql", mimeType="application/octet-stream")]
		private static const InsertBoardsDefaultStatementClass2:Class;
		public static const INSERT_BOARDS_DEFAULT_SQL2:String = new InsertBoardsDefaultStatementClass2();
		
		[Embed(source="/assets/sql/create/InsertContainersDefault.sql", mimeType="application/octet-stream")]
		private static const InsertContainersDefaultStatementClass:Class;
		public static const INSERT_CONTAINERS_DEFAULT_SQL:String = new InsertContainersDefaultStatementClass();
		
		[Embed(source="/assets/sql/create/InsertContainersDefault2.sql", mimeType="application/octet-stream")]
		private static const InsertContainersDefaultStatementClass2:Class;
		public static const INSERT_CONTAINERS_DEFAULT_SQL2:String = new InsertContainersDefaultStatementClass2();
		
		[Embed(source="/assets/sql/create/InsertCategoriesDefault.sql", mimeType="application/octet-stream")]
		private static const InsertCategoriesDefaultStatementClass:Class;
		public static const INSERT_CATEGORIES_DEFAULT_SQL:String = new InsertCategoriesDefaultStatementClass();
		
		[Embed(source="/assets/sql/create/InsertCategoriesDefault2.sql", mimeType="application/octet-stream")]
		private static const InsertCategoriesDefaultStatementClass2:Class;
		public static const INSERT_CATEGORIES_DEFAULT_SQL2:String = new InsertCategoriesDefaultStatementClass2();
		
		[Embed(source="/assets/sql/create/InsertTasksDefault.sql", mimeType="application/octet-stream")]
		private static const InsertTasksDefaultStatementClass:Class;
		public static const INSERT_TASKS_DEFAULT_SQL:String = new InsertTasksDefaultStatementClass();
		
		[Embed(source="/assets/sql/create/InsertCategoriesFromBoard.sql", mimeType="application/octet-stream")]
		private static const InsertCategoriesFromBoardStatementClass:Class;
		public static const INSERT_CATEGORIES_FROM_BOARD_SQL:String = new InsertCategoriesFromBoardStatementClass();
		
	}
}