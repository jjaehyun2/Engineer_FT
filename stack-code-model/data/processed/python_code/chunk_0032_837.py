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
	
	public class Maze extends Entity
	{
		private var generator:MazeGenerator;
		
		public function Maze(generator:MazeGenerator)
		{
			this.generator = generator;
			
			generator.reset();
			generator.generateMaze();
			
			type    = "maze";
			layer   = 1;
			graphic = generator.getMaze();
			mask    = generator.getMask();
			
			var point:Point;
			point = generator.getStartPoint();
			generator.getMaze().setTile(point.x, point.y, 4);
			point = generator.getExitPoint();
			generator.getMaze().setTile(point.x, point.y, 3);
		}
	}
}