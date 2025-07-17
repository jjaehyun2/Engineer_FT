package  
{
	import net.flashpunk.Entity;
	import net.flashpunk.graphics.Tilemap;
	import net.flashpunk.masks.Grid;
	
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class LavaGrid extends Entity 
	{
		[Embed(source = "Assets/Graphics/SpriteSheets/tiles_SS.png")]private static const TILESHEET:Class;
		public var _tiles:Tilemap;
		public var _grid:Grid;
		public function LavaGrid() 
		{
			_tiles = new Tilemap(TILESHEET, 5120, 960, 16, 16);
			graphic = _tiles;
			layer = 100;
			
			_grid = new Grid(5120, 960, 16, 16, 0, 0);
			mask = _grid;
			
			type = 'Lava';
		}
		
	}

}