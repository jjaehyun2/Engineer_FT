package {
	
	import org.flixel.FlxG;
	
	public class Enemy extends Actor {
		
		public static const ENEMY_ROAD_LANE_1:int = Actor.ACTOR_ROAD_BOUNDS_BOTTOM - 196;
		public static const ENEMY_ROAD_LANE_2:int = Actor.ACTOR_ROAD_BOUNDS_BOTTOM - 138;
		public static const ENEMY_ROAD_LANE_3:int = Actor.ACTOR_ROAD_BOUNDS_BOTTOM - 74;
		public static const ENEMY_ROAD_LANE_4:int = Actor.ACTOR_ROAD_BOUNDS_BOTTOM - 10;
		
		public function Enemy( customCar:Car, lane:int ) {
			super( customCar );	
			changeLane( lane );
		}
		
		public function changeLane( lane:int ):Enemy {
			this.car.setPosition( 100, lane );
			this.zOrder = this.calculateZOrder();
			trace( "Enemy:" + this.zOrder );	
			return this;
		}
		
	}		

}