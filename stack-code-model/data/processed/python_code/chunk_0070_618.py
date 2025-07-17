package masputih.isometric
{
	import as3isolib.display.scene.IsoGrid;
	import as3isolib.geom.Pt;
	import com.greensock.easing.Cubic;
	import com.greensock.easing.Linear;
	import com.greensock.TimelineLite;
	import com.greensock.TweenLite;
	import com.greensock.easing.Linear;
	
	import flash.geom.Point;
	import masputih.isometric.pathfinding.AStar;
	import masputih.isometric.pathfinding.AStarEvent;
	import masputih.isometric.pathfinding.AStarGrid;
	import masputih.isometric.Tile;
	//import nl.demonsters.debugger.MonsterDebugger;

	/**
	 * Base class for all tiles that can move through waypoints.
	 * @author Anggie Bratadinata
	 */
	public class MovableTile extends Tile
	{
        
		protected var _waypoints:Array;
		protected var _animator:TimelineLite;
		protected var _dir:String
        public var screenOrigin:Point
		public var directionAr:Array
		public var dirInc:uint=0
			
		public function MovableTile(grid:IsoGrid)
		{
			super(grid)
		}


		public function walkToCell(originX:int,originY:int,c:int, r:int):void
		{
			screenOrigin=new Point(originX,originY);
			//trace("walkToCell -- type: " + this.container["avatar"]["type"]);
			//trace(_aStar == null);
			_aStar.grid.setStartNode(column, row);
			_aStar.grid.setEndNode(c, r);
			_aStar.addEventListener(AStarEvent.COMPLETE, onAStarComplete);
			_aStar.findPath();
		}

		private function onAStarComplete(e:AStarEvent):void
		{
			dirInc = 0;
			directionAr = new Array();
			_waypoints = _aStar.path;
			if(_animator){
			_animator.stop()}
			_animator = new TimelineLite({onStart:onAnimationStart, onComplete:onAnimationComplete});
			_animator.autoRemoveChildren = true;
			
			/*
			trace("_waypoints.length: " + _waypoints.length);
			trace("_waypoints.column x start: " + _waypoints[0].column + " = " + _waypoints[0].column * _grid.cellSize);
			trace("_waypoints.row y start: " + _waypoints[0].row  + " = " + _waypoints[0].row * _grid.cellSize);
			trace("_waypoints.column x end: " + _waypoints[_waypoints.length-1].column  + " = " + _waypoints[_waypoints.length-1].column * _grid.cellSize);
			trace("_waypoints.row y end: " + _waypoints[_waypoints.length-1].row + " = " + _waypoints[_waypoints.length-1].row * _grid.cellSize);
			*/
			var dir_previous:String = "";

			for (var i:int = 0, len:int = _waypoints.length; i < len; i++)
			{
				var x:Number = _waypoints[i].column * _grid.cellSize
				
				var y:Number = _waypoints[i].row * _grid.cellSize;
				
				var current_id:int = i;
				
				var x_previous:Number = ( i == 0 ) ? ( _waypoints[i].column * _grid.cellSize ) : ( _waypoints[current_id-1].column * _grid.cellSize );
				
				var y_previous:Number = ( i == 0 ) ? ( _waypoints[i].row * _grid.cellSize ) : ( _waypoints[current_id-1].row * _grid.cellSize );
				
				var c_previous:Number = ( i == 0 ) ? (_waypoints[i].column):(_waypoints[current_id-1].column);
				
				var r_previous:Number = ( i == 0 ) ? (_waypoints[i].row):(_waypoints[current_id-1].row);
				
				var y_abs:Number = Math.abs(( y_previous - y ));
				
				//var x_abs:Number = Math.abs(( x_previous ) - ( x + 5 ));
				var x_abs:Number = Math.abs(( x_previous - ( x ) ));
				if(this.container["avatar"]["type"] == "farmer_male")
				{	
					if( y_abs >= x_abs)
					{
						if ( y_previous < y ) { _dir = "forward" };
						if ( y_previous > y ) { _dir = "backward" };
					}else{
					   if ( x < ( x_previous ) ) { _dir = "left" };
					   if ( x > ( x_previous ) ) { _dir = "right" }
					}
				}
				else
				{
					if( y_abs > x_abs)
					{
						if ( y_previous < y ) { _dir = "forward" };
						if ( y_previous > y ) { _dir = "backward" };
					}else{
					   if ( x < ( x_previous ) ) { _dir = "left" };
					   if ( x > ( x_previous ) ) { _dir = "right" }
					}
				}
				dir_previous = _dir;
		
				var t:TweenLite = new TweenLite(this, .2, {
						"x": x, 
						"y": y,
						"onStartParams":[x , y],
						"ease": Linear.easeNone,
						"onStart":onTweenStart,
						"onComplete":onTweenComplete
					});

				_animator.append(t);
				directionAr.push(_dir)
			}

			_animator.play();
           
		}
		private function buildDirectionAr():void {
			
			
		}
		public function onTweenStart(...args):void
		{
			//adjust facing direction
		}
		
		public function onTweenComplete():void
		{
			
		}

		public function onAnimationStart():void
		{
			//trace("onAnimationStart...");
		}

		public function onAnimationComplete():void
		{
         	//trace("onAnimationComplete...");
		}

		public function get waypoints():Array
		{
			return _waypoints;
		}
	}
}