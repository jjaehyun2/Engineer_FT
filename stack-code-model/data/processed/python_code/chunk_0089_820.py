package {
	
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.utils.ByteArray;
	import mx.core.BitmapAsset;	
		
	public class Level {
		[Embed(source = './data/freeway.png')] private var renderedTileSet:Class;			
		
		private var _tileSet:FreewayTileSet;
		private var _tileMapList:Object;
		private var _layeredTileMapList:Object;
		
		private var i:uint, j:uint = 0;
		
		public const LAYERED_TILE_MAP_HEIGHT:uint = 6;
		public const LAYERED_TILE_MAP_WIDTH:uint  = 24;
		
		private function initialiseLayeredTileMap():void {
			for ( i = 0; i < LAYERED_TILE_MAP_WIDTH; i++ ) {
				this.layeredTileMapList[i] = new LayeredTileMap();
				this.layeredTileMapList[i].id = i;
			}
		}		
		
		public function initialiseTilePalette():void {
						
			var tmpBitmapAsset:BitmapAsset = this.getBitmapData( renderedTileSet );
			this.tileSet = new FreewayTileSet( tmpBitmapAsset, TileMap.TILE_SIZE_WIDTH, TileMap.TILE_SIZE_WIDTH, Math.floor( tmpBitmapAsset.width >> TileMap.TILE_SHIFT_WIDTH ), Math.floor( tmpBitmapAsset.height >> TileMap.TILE_SHIFT_HEIGHT ) );
		
		}	
		
		protected function loadMapFile( mapData:Class ):String {			
			var b:ByteArray = new mapData();
			return b.readUTFBytes( b.length );
		}	
		
		protected function getBitmapData( tempTileSet:Class ):BitmapAsset {
			var bitmapAsset:BitmapAsset = new tempTileSet();
			return bitmapAsset;
		}		
		
		public function getLayers():Object {
			return this.layeredTileMapList;	
		}
		
		public function get tileSet():FreewayTileSet {
			return _tileSet;
		}
		
		public function set tileSet( value:FreewayTileSet ):void {
			_tileSet = value;
		}
		
		public function get tileMapList():Object {
			return _tileMapList;
		}
		
		public function set tileMapList( value:Object ):void {
			_tileMapList = value;
		}
		
		public function get layeredTileMapList():Object {
			return _layeredTileMapList;
		}
		
		public function set layeredTileMapList( value:Object ):void {
			_layeredTileMapList = value;
		}
	}
}