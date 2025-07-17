package {

	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import mx.core.BitmapAsset;
	import org.flixel.*;
	import com.sixfootsoftware.*;
	
	/**
	 * ...
	 * @author David Long
	 */
	
	public class Tile extends SfsSprite implements ICloneable
	{
		protected static var _cache:Object;
		protected static var _cacheIndex:int = 0;
		
		private var _previousTile:Tile;
		private var _nextTile:Tile;
		private var TileWidth:int;
		private var TileHeight:int;
		private var tileIndex:int;
		private var _tileDepthOffset:int;
		private var utilityIndex:int;
		
		public function Tile( TileGraphic:BitmapData, TileWidth:int = TileMap.TILE_SIZE_WIDTH, TileHeight:int = TileMap.TILE_SIZE_WIDTH, tileNum:int = -1 ) {
			
			this.TileHeight = TileHeight;
			this.TileWidth = TileWidth;
			this.dirty  = true;
			if ( tileNum != -1 ) {
				this.tileIndex = tileNum;
			} else {
				this.tileIndex = _cacheIndex;
			}
			if ( !checkBitmapCache( String( this.tileIndex ) ) ) {
				_cache[ String( this.tileIndex ) ] = new Bitmap( TileGraphic );
				_cacheIndex++;				
			}
			this.pixels      = (_cache[ String( this.tileIndex ) ] as Bitmap).bitmapData;
			this.framePixels = _cache[ String( this.tileIndex ) ];
		}		
		
		public function get tileDepthOffset():int 
		{
			return _tileDepthOffset;
		}
		
		public function set tileDepthOffset(value:int):void 
		{
			_tileDepthOffset = value;
		}
		
		public function clone():Object {
			var clonedTile:Tile = new Tile( (_cache[ String( this.tileIndex ) ] as Bitmap).bitmapData, this.TileWidth, this.TileHeight, this.tileIndex );
			clonedTile.x = this.x;
			clonedTile.y = this.y;
			return clonedTile;
		}
		
		override public function onScreen( Camera:FlxCamera=null ):Boolean {
			if(Camera == null)
				Camera = FlxG.camera;
			getScreenXY(_point,Camera);
			return (_point.x + width > 0) && (_point.x < Camera.width) && (_point.y + height > 0) && (_point.y < Camera.height);
		}
		
		static public function checkBitmapCache(Key:String):Boolean
		{
			return (_cache[Key] != undefined) && (_cache[Key] != null);
		}		
		
		static public function initCache():void
		{
			_cache = new Object();
		}		
		
	}

}