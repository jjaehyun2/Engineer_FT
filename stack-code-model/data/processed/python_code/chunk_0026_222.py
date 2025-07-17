package framework.services
{

	import flash.events.IEventDispatcher;
	
	import framework.services.helper.ISQLRunnerDelegate;

	public class SQLCategoryService implements ISQLCategoryService
	{
		[Inject] public var eventDispatcher:IEventDispatcher;
		[Inject] public var sqlRunner:ISQLRunnerDelegate;
		
		public function SQLCategoryService() {
		}
		
		
	}
}