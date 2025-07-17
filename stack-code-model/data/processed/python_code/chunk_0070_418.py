package {
	import com.sixfootsoftware.*;
	import org.flixel.FlxPoint;
	import org.flixel.FlxRect;
	
	public class TileMap extends SfsGroup implements ITileMap, ICloneable, IAlignable {
		
		public static const TILE_SIZE_WIDTH:int   = 32;
		public static const TILE_SIZE_HEIGHT:int  = 32;
		public static const TILE_SHIFT_WIDTH:int  = 5;
		public static const TILE_SHIFT_HEIGHT:int = 5;
		protected const ONSCREEN:FlxRect = new FlxRect( -24, 0, 664, 480 );
		
		protected var tileMapHeight:uint;
		protected var tileMapWidth:uint;
		protected var tileMap:Array;
		protected var _velocity:int;
		protected var storedMapData:String;
		protected var usedTileSet:FreewayTileSet;
		protected var origin:FlxPoint;
		protected var col:FlxRect = new FlxRect( 0, 0, 640, 480 );
		protected var mapDimensions:FlxPoint;
		protected var mapPosition:FlxPoint;
		protected var screenPositionTile:Tile;
		protected var pos:int;
		
		private var _next:TileMap;
		private var _prev:TileMap;
		private var seen :Boolean = false;		
		private var _isNext:Boolean = false;
		
		private var newMapLocation:FlxPoint = new FlxPoint();		
		
		public function TileMap( mapData:String = "", activeTileSet:FreewayTileSet = null, singleColumnMode:int = -1 ) {
			
			if ( mapData == "" ) {
				return;
			}
			
			trace( "> " + singleColumnMode );
			
			this.origin      = new FlxPoint( 0 - (TILE_SIZE_WIDTH * 2), 0 );
			this.mapPosition = new FlxPoint( 0 - (TILE_SIZE_WIDTH * 2), 0 );

			if ( activeTileSet.length() == 0 ) {
				return;
			}
			//Figure out the map dimensions based on the data string
			var columns:Array;
			this.storedMapData     = mapData;
			this.usedTileSet       = activeTileSet;   
			var rows:Array         = mapData.split("\n");
			this.tileMapHeight     = rows.length;
			this.tileMapWidth      = 0;
			var rowIndex:uint      = 0;
			var columnIndex:uint;
			
			while( rowIndex < this.tileMapHeight ) {
				columns = rows[rowIndex].split( "," );
				if( columns.length <= 1 ) {
					this.tileMapHeight = this.tileMapHeight - 1;
					continue;
				}
				if ( this.tileMapWidth == 0 ) {
					this.tileMapWidth = columns.length;
					defineTileDimensions();
				}
				columnIndex = 0;
				while ( columnIndex < this.tileMapWidth ) {
					if ( singleColumnMode == -1 || singleColumnMode == columnIndex ) {
						this.assignTileToMap( rowIndex, columnIndex, columns[columnIndex], activeTileSet );					
					}	
					columnIndex++;
				}
				rowIndex++;
			}
			
			var origCalc:int = 0;
			
			if ( singleColumnMode != -1 ) {
				this.tileMapWidth = 2;
				origCalc = TILE_SIZE_WIDTH * singleColumnMode;
			}
			
			this.origin      = new FlxPoint( 0 - (TILE_SIZE_WIDTH * 2) + origCalc, 0 );
			this.mapPosition = new FlxPoint( 0 - (TILE_SIZE_WIDTH * 2) + origCalc, 0 );			
			
			this.mapDimensions = new FlxPoint( (this.tileMapWidth - 1) << TILE_SHIFT_WIDTH, this.tileMapHeight << TILE_SHIFT_WIDTH );
			col.width          = this.tileMapWidth;
			
			trace( "Finished Tilemap Build" );
			
		}
		
		private function defineTileDimensions():void 
		{
			this.tileMap = new Array( this.tileMapWidth );
			
			for ( var i:int = 0; i < this.tileMap.length; i ++ ) {
				this.tileMap[ i ] = new Array( this.tileMapHeight );
			}
		}	
		
		private function addTileToMap( looseTile:Tile, columnIndex:uint, rowIndex:uint ):Tile {
			looseTile.tileDepthOffset = ( columnIndex << TILE_SHIFT_WIDTH ); 
			looseTile.x               = origin.x + (  columnIndex << TILE_SHIFT_WIDTH ); 
			looseTile.y               = origin.y + rowIndex << TILE_SHIFT_WIDTH;
			looseTile.velocity.x      = this.velocity;
			this.tileMap[columnIndex][rowIndex] = looseTile;
			return looseTile;
		}
		
		private function assignTileToMap( rowIndex:uint, columnIndex:uint, tile:uint, activeTileSet:FreewayTileSet ):void {
			trace( columnIndex + ":" + tile );
			if ( tile >= activeTileSet.length() || tile == 0 ) {
				tile = 0;
				return;
			}

			this.add( this.addTileToMap( ( activeTileSet.tileList[tile] as Tile).clone() as Tile, columnIndex, rowIndex ) );
			
			if ( !this.screenPositionTile ) {
				this.screenPositionTile = this.tileMap[columnIndex][rowIndex];
			}

		}
		
		private function defineVelocity():void {
			for each ( var tileMapComponent:Tile in this.members ) {
				tileMapComponent.velocity.x = this.velocity;
			}		
		}
		
		public function get velocity():int {
			return _velocity;
		}
		
		public function set velocity(value:int):void {
			_velocity = value;
			this.defineVelocity();
		}
		
		public function setScreenXY( screenPosition:FlxPoint ):void {
			pos = screenPosition.x;
			for each ( var tileMapComponent:Tile in this.members ) {
				tileMapComponent.x = pos;			
			}
		}
		
		public function setScrollRate( scrollRate:Number ):void {
			for each ( var tileMapComponent:Tile in this.members ) {
				tileMapComponent.velocity.x =  tileMapComponent.velocity.x * scrollRate;
			}
		}		
		
		public function onScreen():Boolean {
			col.x = getScreenPosition().x;
			
			if ( col.overlaps( ONSCREEN ) ) {
				return true;
			}
			return false;
		}
		
		public function setScreenPosition( pos:FlxPoint ):void {
			for each ( var tileMapComponent:Tile in this.members ) {
				tileMapComponent.x = this.mapPosition.x = pos.x;			
			}			
		}
		
		public function getScreenPosition():FlxPoint {
			this.mapPosition.x = this.screenPositionTile.x;
			return this.mapPosition;
		}
		
		public function getMapDimensions():FlxPoint {	
			return this.mapDimensions;
		}
		
		public function clone():Object {
			var clonedTileMap:TileMap = new TileMap( this.storedMapData, this.usedTileSet );
			clonedTileMap.velocity = this.velocity;
			return clonedTileMap;
		}		
		
		public function get next():TileMap {
			return _next;
		}
		
		public function set next(value:TileMap):void {
			_next = value;
		}
		
		public function get prev():TileMap {
			return _prev;
		}
		
		public function set prev(value:TileMap):void {
			_prev = value;
		}
		
		public function get isNext():Boolean {
			return _isNext;
		}
		
		public function set isNext(value:Boolean):void {
			_isNext = value;
		}		
		
		public function alignWith( parentLayer:IAlignable ):void {
			if ( !parentLayer ) {
				return;
			}
			isNext      = false;			
			prev.isNext = true;
			
			newMapLocation.x = parentLayer.getScreenPosition().x - this.getMapDimensions().x;
			this.setScreenPosition( newMapLocation );
		}	
		
		override public function preUpdate():void {		
			if (isNext && !onScreen()) {				
				alignWith( next );
			} 
		}
		
		override public function postUpdate():void {			
		}		

	}
}