package masputih.isometric.pathfinding
{
	import flash.utils.Dictionary;
	
	public class FloodFill
	{
		private var _grid:AStarGrid;
		private var _startNode:Node;
		private var _isWalkAbleNode:Boolean = true;

		private var _open:Array;

		public var _endNode:Node = null;
		public var _resultFound:Boolean = false;
		
		private var filledNodes:Dictionary;
		
		public function FloodFill()
		{
		}
		
		public function findNode( fromNode:Node, grid:AStarGrid, walkabl:Boolean = true ):void{
			_grid = grid.clone();
			_open = [];
			_startNode = fromNode;
			_isWalkAbleNode = walkabl;
			_resultFound = false;
			//dispatchEvent(new AStarEvent(AStarEvent.SEARCH));
			
			filledNodes = new Dictionary();
			floodFill( _startNode.column, _startNode.row );
		}
		
		private function floodFill( col:int, row:int):void{
			if ( ( col >= 0 && col < _grid.numCols) &&
				 ( row >= 0 && row < _grid.numRows) &&
				 _resultFound == false ){
				var currentNode:Node = _grid.getNode(col, row);

				if (filledNodes[currentNode] != null){
					return;
				}
				
				filledNodes[currentNode] = true;

				if ( currentNode.walkable ){
					_resultFound = true;
					_endNode = currentNode;
					return;
				}
				floodFill( col, row + 1);
				floodFill( col, row - 1);				
				floodFill( col + 1, row);							
				floodFill( col - 1, row);										
			}
		}
		
	}
}