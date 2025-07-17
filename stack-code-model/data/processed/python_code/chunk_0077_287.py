package framework.models
{
	import flash.events.IEventDispatcher;
	
	import mx.collections.ArrayCollection;
	import mx.collections.ISort;
	import mx.collections.ISortField;
	
	import spark.collections.Sort;
	import spark.collections.SortField;
	
	import framework.appConfig.Constants;
	import framework.events.BoardDataLoadedEvent;
	import framework.models.vo.BoardVO;
	import framework.models.vo.CategoryVO;
	import framework.models.vo.ContainerVO;
	import framework.models.vo.TaskVO;

	public class BoardModel {
		
		[Inject] public var eventDispatcher:IEventDispatcher;
		
		public const MAX_BOARDS_ALLOWED:uint = 11;
		public var selectedBoardId:uint = 0;
		public var requestBoardId:uint = 0;
		
		public var FINISHED_TASKS_VIEW_MODE:String = Constants.FINISHED_TASKS_CONDENSED_MODE;
		
		private var _boards:ArrayCollection;
		private var _containers:ArrayCollection;
		private var _tasks:ArrayCollection;
		private var _categories:ArrayCollection;
		
		public function BoardModel() {
		}

		public function get categories():ArrayCollection {
			return _categories;
		}

		public function set categories(value:ArrayCollection):void {
			_categories = value;
			
			eventDispatcher.dispatchEvent(new BoardDataLoadedEvent(BoardDataLoadedEvent.CATEGORIES_LOADED, _categories));
		}

		public function get tasks():ArrayCollection {
			return _tasks;
		}

		public function set tasks(value:ArrayCollection):void {
			_tasks = value;
			eventDispatcher.dispatchEvent(new BoardDataLoadedEvent(BoardDataLoadedEvent.TASKS_LOADED, _tasks));
		}

		public function get containers():ArrayCollection {
			return _containers;
		}

		public function set containers(value:ArrayCollection):void {
			_containers = value;
			
			//sort the containers on the position property
			
			var sort:ISort = new Sort();
			var sortField:ISortField = new SortField("position");
			sort.fields = [sortField];
			
			_containers.sort = sort;
			_containers.refresh();
			
			eventDispatcher.dispatchEvent(new BoardDataLoadedEvent(BoardDataLoadedEvent.CONTAINERS_LOADED, _containers));
		}

		public function get boards():ArrayCollection {
			return _boards;
		}

		public function set boards(value:ArrayCollection):void {
			_boards = value;
			if(requestBoardId == 0 && _boards.length > 0) {
				requestBoardId = (_boards.getItemAt(0) as BoardVO).id;
			}
			eventDispatcher.dispatchEvent(new BoardDataLoadedEvent(BoardDataLoadedEvent.BOARDS_LOADED, _boards, requestBoardId));
			
		}
		
		public function getSelectedBoard():BoardVO {
			
			var selectedBoardItem:BoardVO = null;
			for each(var boardItem:BoardVO in boards) {
				if(boardItem.id == selectedBoardId) {
					selectedBoardItem = boardItem; 
				}
			}
			
			return selectedBoardItem;
		}
		public function getBacklogId():uint {
			for each(var item:ContainerVO in _containers) {
				if(item.type == Constants.CONTAINER_TYPE_BACKLOG) {
					return item.id;
				}
			}
			
			return 0;
		}
		
		public function getDefaultCategoryId(_toDeleteId:uint):uint {
			
			// we could be deleting the first one - last one should not be deletable (checked in view)
			if((categories.getItemAt(0) as CategoryVO).id != _toDeleteId)
				return (categories.getItemAt(0) as CategoryVO).id;
			else
				return (categories.getItemAt(1) as CategoryVO).id;
		}
		
		public function getNewBoardPosition():uint {
			if(boards.length > 0)
				return (boards.getItemAt(boards.length -1) as BoardVO).position + 1;
			else
				return 1;
		}
		/*public function setRequestedBoardBeforePosition(_boardId:uint):void {
			var beforePos:uint;
			
			for each(var bItem:BoardVO in boards) {
				if(bItem.id == _boardId) {
					beforePos = bItem.position - 1;
					break;
				}
			}
			
			var found:Boolean = false;
			for each(var item:BoardVO in boards) {
				if(item.position == beforePos) {
					requestBoardId = item.id;
					found = true;
					break;
				}
			}
			
			if(!found) {
				requestBoardId = boards.
			}
		}*/
		
		public function updateBoard(_boardVO:BoardVO):void {
			for (var i:uint; i < boards.length; i++) {
				var item:BoardVO = boards[i] as BoardVO;
				if(item.id == _boardVO.id) {
					item.title = _boardVO.title;
					item.backgroundColor = _boardVO.backgroundColor;
					boards.itemUpdated(item);
					break;
				}
			}
		}
		public function updateTask(_task:TaskVO):void {
			
			for(var i:uint = 0; i < tasks.length; i++) {
				var item:TaskVO = tasks.getItemAt(i) as TaskVO;
				if(item.id == _task.id) {
					tasks.removeItemAt(i);
					break;
				}
			}
			
			tasks.addItem(_task);
			tasks.refresh();
			
		}
		
		public function removeTask(_taskId:uint):void {
			for(var i:uint = 0; i < tasks.length; i++) {
				var item:TaskVO = tasks.getItemAt(i) as TaskVO;
				if(item.id == _taskId) {
					tasks.removeItemAt(i);
					break;
				}
			}
		}
		
		public function updateContainer(_containerVO:ContainerVO):void {
			for (var i:uint; i < containers.length; i++) {
				var item:ContainerVO = containers[i] as ContainerVO;
				if(item.id == _containerVO.id) {
					item.title = _containerVO.title;
					item.maxItems = _containerVO.maxItems;
					containers.itemUpdated(item);
					break;
				}
			}
			
		}

	}
}