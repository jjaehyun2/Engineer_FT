package worlds {
	import flash.utils.ByteArray;
	import net.flashpunk.Entity;
	import net.flashpunk.graphics.Tilemap;
	import net.flashpunk.masks.Grid;

	public class Level1 extends Entity {
		private var tilemap:Tilemap;
		private var grid:Grid;
		public var xmlData:XML;
		
		public function Level1(xml:Class) {
			type = 'level';
			layer = 1;
			loadLevel(xml);
		}
		
		private function loadLevel(xml:Class):void {
			var rawData:ByteArray = new xml;
			xmlData = new XML(rawData.readUTFBytes(rawData.length));
			
			graphic = tilemap = new Tilemap(GC.LEVEL1_PNG, xmlData.@width, xmlData.@height, GC.TILE_SIZE, GC.TILE_SIZE);
			mask = grid = new Grid(xmlData.@width, xmlData.@height, GC.TILE_SIZE, GC.TILE_SIZE, 0, 0)
			grid.usePositions = true;
			
			for each(var tile:XML in xmlData.Tiles.tile) {
				tilemap.setTile(tile.@x, tile.@y, tile.@id);
			}

			for each (var solid:XML in xmlData.Solids.rect) {
				grid.setRect(solid.@x, solid.@y, solid.@w, solid.@h);
			}
		}
	}
}