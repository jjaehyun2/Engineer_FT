package {
	import com.sixfootsoftware.*;
	import org.flixel.FlxBasic;
	import org.flixel.FlxPoint;
	
	public class LayeredTileMap extends SfsGroup implements ICloneable {
		
		public var id:int;
		
		private var _velocity:int;
		private var mapDimensions:FlxPoint;
		private var mapPosition:TileMap;
			
		public function LayeredTileMap() {
		
		}
					
		private function defineVelocity():void {
			for each ( var tileMapLayer:TileMap in this.members ) {
				tileMapLayer.velocity = this.velocity;
			}		
		}
		
		public function get velocity():int {
			return _velocity;
		}
		
		public function set velocity(value:int):void {
			_velocity = value;
			this.defineVelocity();
		}
		
		public function onScreen():Boolean {
			for each ( var tileMapLayer:TileMap in this.members ) {
				if ( tileMapLayer.onScreen() ) {
					return true;
				}
			}
			return false;
		}
		
		public function drawLayer( layer:int ):void {
			if ( !onScreen() )  {
				return;
			}
			var basic:FlxBasic;
			if( layer < length ) {
				basic = members[layer] as FlxBasic;
				if((basic != null) && basic.exists && basic.visible)
					basic.draw();
			}	
		}	
		
		public function layer( layer:int ):TileMap {
			return this.members[ layer ];
		}
		
		public function clone():Object {
			var clonedLayeredTileMap:LayeredTileMap = new LayeredTileMap();
			for each( var tileMapItem:TileMap in this.members ) {
				clonedLayeredTileMap.add( tileMapItem.clone() as TileMap );
			}
			return clonedLayeredTileMap;
		}	

	}
	
}