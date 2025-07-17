package nmath {
    import flash.errors.IllegalOperationError;
    import flash.utils.Dictionary;

	import ncollections.TDictionary;

	import ncollections.grid.Grid;
    import ncollections.grid.IGridObject;

    public class GraphUtils {
		private static const EMPTY_ARRAY:Array = [];

		private static var _seen:TDictionary = TDictionary.EMPTY;

		private static var _neighbors:Array = [];
		private static var _selected:Array  = [];
		private static var _queue:Array     = [];

		public function GraphUtils() {
			throw new IllegalOperationError('GraphUtils is static!');
		};
		
		public static function bfs(pIndexX:uint, pIndexY:uint,
								   pGrid:Grid, pAddHeighbors:Function,
                                   pComparator:Function):Array {
			var current:IGridObject;
			var searched:IGridObject = pGrid.take(pIndexX, pIndexY) as IGridObject;
			
			if (!searched) {
				return EMPTY_ARRAY;
			}
			
			_neighbors.length = 0;

			_seen.clean();

			_selected.length = 0;

			_queue.length    = 0;
			_queue.push(searched);
			
			while (_queue.length) {
				current = _queue.shift();
				
				if (!current) {
					continue;
				}
				
				pAddHeighbors(pGrid, current.indexX, current.indexY, _neighbors);
				
				for each (var neighbor:IGridObject in _neighbors) {
					if (!neighbor) {
						continue;
					}
					
					if (_seen.contains(neighbor)) {
						continue;
					}
					
					_seen.add(neighbor, true);
					
					if (pComparator(neighbor, searched)) {
						_selected.push(neighbor);
						_queue.push(neighbor);
					} else {
						continue;
					}	
				}
				
				_neighbors.length = 0;
			}
			
			return _selected.concat();
		};
		
		public static function addNeighborsHorizontal(pGrid:Grid, 
													  pIndexX:int, pIndexY:int, 
													  pContainer:Array):void {
			pContainer.push(pGrid.take(pIndexX - 1, pIndexY), pGrid.take(pIndexX + 1, pIndexY));
		};
		
		public static function addNeighborsVertical(pGrid:Grid, 
													pIndexX:int, pIndexY:int, 
													pContainer:Array):void {
			pContainer.push(pGrid.take(pIndexX, pIndexY - 1), pGrid.take(pIndexX, pIndexY + 1));
		};
		
		public static function addNeighborsVerticalHorizintal(pGrid:Grid, 
													pIndexX:int, pIndexY:int, 
													pContainer:Array):void {
			addNeighborsVertical(pGrid, pIndexX, pIndexY, pContainer);
			addNeighborsHorizontal(pGrid, pIndexX, pIndexY, pContainer);
		};

        public static function reflectionComparator(pNeighbor:IGridObject,
                                                    pSearched:IGridObject):Boolean {
            return pNeighbor.reflection == pSearched.reflection;
        };
	};
}