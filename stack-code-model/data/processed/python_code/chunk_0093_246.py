package
{
	import container.Stack;
	
	import flash.display.BitmapData;
	import flash.geom.Point;
	
	import net.flashpunk.Entity;
	import net.flashpunk.FP;
	import net.flashpunk.Graphic;
	import net.flashpunk.Mask;
	import net.flashpunk.graphics.Tilemap;
	import net.flashpunk.masks.Grid;
	
	public class MazeGenerator
	{
		private var maze:Tilemap;
		private var mask:Grid;
		private var lava:Grid;
		private var exit:Grid;
		private var start:Grid;
		
		private var tileWidth:uint;
		private var tileHeight:uint;
		
		private var stack:Stack;
		
		private var startPoint:Point;
		private var exitPoint:Point;
		
		private var mazePoint:Point;
		private var lavaPoints:Array;
		
		private var level:uint;
		
		public function MazeGenerator(asset:Class, tileWidth:uint, tileHeight:uint)
		{
			maze  = new Tilemap(asset, FP.screen.width, FP.screen.height, tileWidth, tileHeight);
			mask  = new Grid(FP.screen.width, FP.screen.height, tileWidth, tileHeight);
			lava  = new Grid(FP.screen.width, FP.screen.height, tileWidth, tileHeight);
			exit  = new Grid(FP.screen.width, FP.screen.height, tileWidth, tileHeight);
			start = new Grid(FP.screen.width, FP.screen.height, tileWidth, tileHeight);
			
			this.tileWidth  = tileWidth;
			this.tileHeight = tileHeight;
			
			level = 1;
			
			reset();
		}
		
		public function reset():void
		{
			maze.setRect(0, 0, maze.columns, maze.rows, 0);
			lava.setRect(0, 0, lava.columns, lava.rows, false);
			mask.setRect(0, 0, mask.columns, mask.rows, true);
			exit.setRect(0, 0, exit.columns, exit.rows, false);
			start.setRect(0, 0, start.columns, start.rows, false);
			
			stack = new Stack;
			
			startPoint = new Point;
			exitPoint  = new Point;
			
			if (Math.random() < .5)
			{
				startPoint.x = int(Math.random() < .5 ? 0 : FP.screen.width / tileWidth - 1);
				startPoint.y = int(3 + Math.random() * (FP.screen.height / tileHeight - 4));
				
				exitPoint.x = int(FP.screen.width / tileWidth - 1 - startPoint.x);
				exitPoint.y = int(3 + Math.random() * (FP.screen.height / tileHeight - 4));
			} else
			{
				startPoint.x = int(3 + Math.random() * (FP.screen.width / tileWidth - 4));
				startPoint.y = int(Math.random() < .5 ? 0 : FP.screen.height / tileHeight - 1);
				
				exitPoint.x = int(3 + Math.random() * (FP.screen.width / tileWidth - 4));
				exitPoint.y = int(FP.screen.height / tileHeight - 1 - startPoint.y);
			}
			
			mazePoint  = startPoint.clone();
			lavaPoints = new Array(mazePoint);
			
			start.setTile(startPoint.x, startPoint.y, true);
			exit.setTile(exitPoint.x, exitPoint.y, true);
		}
		
		public function getLevel():uint
		{
			return level;
		}
		
		public function setLevel(level:uint):void
		{
			this.level = level;
		}
		
		public function getTileWidth():uint
		{
			return tileWidth;
		}
		
		public function getTileHeight():uint
		{
			return tileHeight;
		}
		
		public function getMaze():Tilemap
		{
			return maze;
		}
		
		public function getMask():Grid
		{
			return mask;
		}
		
		public function getLava():Grid
		{
			return lava;
		}
		
		public function getExit():Grid
		{
			return exit;
		}
		
		public function getStart():Grid
		{
			return start;
		}
		
		public function getStartPoint():Point
		{
			return startPoint.clone();
		}
		
		public function getExitPoint():Point
		{
			return exitPoint.clone();
		}
		
		public function generateMaze():void
		{
			while (generateMazeStep()) {};
			generateExit();
		}
		
		public function generateMazeStep():Boolean
		{
			if (mazePoint == null)
				return false;
			
			mazePoint = generatePoint(mazePoint);
			
			while (mazePoint == null)
			{
				if (stack.empty())
					return false;
				
				mazePoint = generatePoint(stack.pop());
			}
			
			return true;
		}
		
		public function propogateLava():void
		{
			while (propogateLavaStep()) {};
		}
		
		public function propogateLavaStep():Boolean
		{
			var newLavaPoints:Array = new Array;
			
			var point:Point;
			for each (point in lavaPoints)
				propogateLavaPoint(point, newLavaPoints);
			
			lavaPoints = newLavaPoints;
			return lavaPoints.length != 0;
		}
		
		private function generatePoint(point:Point):Point
		{
			maze.setTile(point.x, point.y, 1);
			mask.setTile(point.x, point.y, false);
			
			var neighbors:Array = getPointNeighbors(point, 2, 1);
			if (neighbors == null)
				return null;
			
			var nextPoint:Point = neighbors[int(Math.random() * neighbors.length)];
			stack.push(point);
			
			var wallPoint:Point = new Point(point.x + (nextPoint.x - point.x) / 2, point.y + (nextPoint.y - point.y) / 2);
			maze.setTile(wallPoint.x, wallPoint.y, 1);
			mask.setTile(wallPoint.x, wallPoint.y, false);
			return nextPoint;
		}
		
		private function generateExit():void
		{
			maze.setTile(exitPoint.x, exitPoint.y, 1);
			mask.setTile(exitPoint.x, exitPoint.y, false);
			
			var neighbors:Array = getPointNeighbors(exitPoint, 2, 3);
			if (neighbors == null)
				return;
			
			var nextPoint:Point = neighbors[int(Math.random() * neighbors.length)];
			maze.setTile(nextPoint.x, nextPoint.y, 1);
			mask.setTile(nextPoint.x, nextPoint.y, false);
			
			var wallPoint:Point = new Point(exitPoint.x + (nextPoint.x - exitPoint.x) / 2, exitPoint.y + (nextPoint.y - exitPoint.y) / 2);
			maze.setTile(wallPoint.x, wallPoint.y, 1);
			mask.setTile(wallPoint.x, wallPoint.y, false);
		}
		
		private function propogateLavaPoint(point:Point, newLavaPoints:Array):void
		{
			maze.setTile(point.x, point.y, 2);
			lava.setTile(point.x, point.y, true);
			
			var points:Array = getPointNeighbors(point, 1, 2);
			if (points == null)
				return;
			
			for each (point in points)
				newLavaPoints.push(point);
		}
		
		private function getPointNeighbors(point:Point, offset:int, checkTile:uint):Array
		{
			var neighbors:Array = new Array;
			
			var n1:Point = getPoint(int(point.x) - offset, int(point.y), checkTile);
			var n2:Point = getPoint(int(point.x) + offset, int(point.y), checkTile);
			var n3:Point = getPoint(int(point.x), int(point.y) - offset, checkTile);
			var n4:Point = getPoint(int(point.x), int(point.y) + offset, checkTile);
			
			if (n1 != null) neighbors.push(n1);
			if (n2 != null) neighbors.push(n2);
			if (n3 != null) neighbors.push(n3);
			if (n4 != null) neighbors.push(n4);
			
			return neighbors.length == 0 ? null : neighbors;
		}
		
		private function getPoint(x:int, y:int, checkTile:uint):Point
		{
			if (x <= 0 || y <= 0 || x >= (FP.screen.width / tileWidth - 1) || y >= (FP.screen.height / tileHeight - 1))
				return null;
			
			var tile:uint = maze.getTile(x, y);
			if (tile == checkTile || (checkTile == 2 && tile == 0))
				return null;
			
			return new Point(x, y);
		}
	}
}