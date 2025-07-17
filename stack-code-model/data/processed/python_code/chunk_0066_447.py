package masputih.isometric
{
	import as3isolib.display.IsoSprite;
	import as3isolib.display.scene.IsoGrid;
	import as3isolib.geom.Pt;
	import as3isolib.utils.IsoDrawingUtil;
	
	import masputih.isometric.pathfinding.AStar;
	import masputih.isometric.pathfinding.AStarGrid;
	
	//import nl.demonsters.debugger.MonsterDebugger;
	
	/**
	 * Base class of all tiles.
	 * @author Anggie Bratadinata
	 */
	public class Tile extends IsoSprite
	{
		
		public var draggable:Boolean = true;
		public var fillColor:uint;
		
		protected var _tempWalkable:Boolean;
		protected var _walkable:Boolean = true;
		
		protected var _aStar:AStar;
		protected var _aStarGrid:AStarGrid;
		
		//# of gric-cells occupied by this tile
		protected var _colSpan:Number = 1;
		protected var _rowSpan:Number = 1;
		protected var _spans:Array;
		
		//the occupied cells <col>_<row>
		protected var _occupiedCells:Array;
		
		//referenced grid
		protected var _grid:IsoGrid;
		protected var _cellSize:Number;
		
		//grid-based position
		protected var _col:int = 0;
		protected var _row:int = 0;
		
		//tile name <column_row_z>
		protected var _name:String = '';
		
		public function Tile(grid:IsoGrid)
		{
			_grid = grid;
			_cellSize = grid.cellSize;
			
			spans = [_colSpan, _rowSpan];
			//moveToCell(0, 0, 0);
			
		}
		
		public function moveToCell(col:int, row:int, z:Number = 0):void {
			
			//store the original walkable value
			_tempWalkable = walkable;
			//temporary set the tile walkable
			walkable = true;
			
			super.moveTo(col * _cellSize, row * _cellSize , z);
		}
		
		protected function drawGeometry():void {
			container.graphics.clear();
			container.graphics.beginFill(fillColor);
			IsoDrawingUtil.drawIsoRectangle(container.graphics, new Pt(0, 0, 0), width, length);
			container.graphics.endFill();
		}
		
		/**********************************************
		 * OVERRIDES
		 **********************************************/
		
		override public function invalidatePosition():void
		{
			super.invalidatePosition();
			
			_col = Math.floor(x / _cellSize);
			_row = Math.floor(y / _cellSize);
			
			_occupiedCells = [];
			
			for (var i:int = 0 ; i < _colSpan ; i++) {
				for (var j:int = 0; j < _rowSpan ; j++) {
					_occupiedCells.push((_col + i) + "_" + (_row + j));
				}
			}
			
			//update name
			_name = String(_col) + "_" + String(_row) +"_" + String(this.z);
			
			//put back the original walkable value (before this tile moved)
			walkable = _tempWalkable;
			
			//MonsterDebugger.trace(this, this.name + ' occupies : ' +  occupiedCells);
		}
		
		
		override public function render(recursive:Boolean = true):void 
		{
			//if the tile has no skins and has been invalidated
			if (sprites.length == 0 && isInvalidated) drawGeometry();
			
			super.render(recursive);
			
		}
		
		/**********************************************
		 * GETTERS/SETTERS
		 **********************************************/
		
		public function get name():String { return _name; }
		
		public function get grid():IsoGrid { return _grid; }
		
		public function get colSpan():Number { return _colSpan; }
		
		public function get rowSpan():Number { return _rowSpan; }
		
		/**
		 * return [column span, row span ]
		 *
		 */
		public function get spans():Array { return _spans; }
		
		public function set spans(value:Array):void
		{
			_spans = value;
			_colSpan = _spans[0];
			_rowSpan = _spans[1];
			
			setSize(_cellSize * colSpan, _cellSize * rowSpan, height);
			
		}
		
		/**
		 * Array of String <col_row>
		 */
		public function get occupiedCells():Array {
			return _occupiedCells;
		}
		
		public function get column():int { return _col; }
		
		public function get row():int{ return _row };
		
		public function get walkable():Boolean { return _walkable; }
		
		public function set walkable(value:Boolean):void 
		{
			_walkable = value;
			updateAstarGrid();
		}
		
		public function get aStarGrid():AStarGrid { return _aStar.grid; }
		
		public function set aStarGrid(value:AStarGrid):void 
		{
			_aStar = new AStar(value);
			updateAstarGrid();
		}
		
		public function get aStar():AStar { return _aStar; }
		
		protected function updateAstarGrid():void {
			try {
				for (var i:int = 0, len:int = occupiedCells.length; i < len; i++) {
					var cr:Array = String(occupiedCells[i]).split('_');
					_aStar.grid.setWalkable(cr[0], cr[1], _walkable);
				}
			}catch (e:Error) { };
		}
		
	}
	
}