package com.illuzor.otherside.events {
	
	import com.illuzor.otherside.graphics.game.characters.Enemy;
	import starling.events.Event;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class LevelControllerEvent extends Event {
		
		private var _enemy:Enemy;
		
		public static const ADD_ENEMY:String = "addEnemy";
		public static const LEVEL_COMPLETE:String = "levelComplite";
		public static const GROUP_COMPLETE:String = "groupComplete";
		
		public function LevelControllerEvent(type:String, enemy:Enemy = null) { 
			super(type);
			_enemy = enemy;
		} 
		
		public function get enemy():Enemy {
			return _enemy;
		}
		
	}
}