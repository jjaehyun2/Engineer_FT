package {

	import org.flixel.*;
	import actor.*;

	public class PlayState extends FlxState
	{	

		private var i:uint, j:uint = 0;
		
		private const LAYERED_TILE_MAP_HEIGHT:uint = 6;
		private const LAYERED_TILE_MAP_WIDTH:uint  = 24;
				
		override public function create():void {
			
			Registry.register();
			
			FlxG.bgColor = 0xff9fd3f8;
			
			this.add( Registry.road );			
			this.add( Registry.player );	
			this.add( Registry.enemy );	
			
			var level:Level1 = new Level1();
			
			for ( j = 0; j < Registry.nightScene.members.length; j ++ ) {
					this.add( Registry.nightScene.members[j] );
			}
			
			var levelLayers:Object = level.getLayers(); 
			
			for ( i = 0; i < LAYERED_TILE_MAP_WIDTH; i++ ) {
				for ( j= 0; j < levelLayers[i].members.length; j ++ ) {
					this.add( levelLayers[i].members[j] );
				}
			}	
		
		}
		
		private function toggleNight():void {
			Registry.nightScene.toggleNight();	
		}
		
		private function renderNightLightMap():void {
			if ( Registry.nightScene.isNight || Registry.nightScene.alpha > 0 ) {
				Registry.nightScene.reset();
				Registry.player.stampNight( Registry.nightScene );
				Registry.enemy.stampNight( Registry.nightScene );
				Registry.nightScene.stamp( Registry.nightScene.sky, 0, 0 );
			}
		}
		
		override public function update():void {		
			if ( FlxG.keys.justPressed( "L" ) ) {
				this.toggleNight();
			}
			this.renderNightLightMap();
			super.update();
		}
						
		private function drawBasicTile( basicTile:FlxBasic ):void {
			if( ( basicTile != null ) && basicTile.exists && basicTile.visible ) {
				basicTile.draw();	
			}
		}
		
		override public function draw(): void {
			members.sortOn( "zOrder", Array.NUMERIC );
			i = 0;
			while ( i < length ) {
				this.drawBasicTile( members[i] as FlxBasic );
				i++;
			}
		}
	}
}