package  
{
	import org.flixel.*;
	import org.flixel.plugin.photonstorm.*;
	
	import Entities.Enemies.*;
	
	/**
	 * Wave of enemies.
	 * 
	 * @author Artem Gurevich / RadicalEd
	 */
	public class Wave {
		private var m_count:int;
		private var m_spawnTimer:FlxTimer;
		
		public function Wave(count:int) {
			m_count      = count;
			m_spawnTimer = new FlxTimer();
			
			m_spawnTimer.start(0.6, 0, spawn);
		}
		
		public function get count():int { return m_count; }
		
		public function isComplete():Boolean {
			if (FlxG.state is GameState) {
				var gameState:GameState = FlxG.state as GameState;
				return m_count < 1 && gameState.enemies.countLiving() < 1;
			}
			
			return true;
		}
		
		private function spawn(timer:FlxTimer):void {
			if (--m_count < 1)
				timer.stop();
			
			if (FlxG.state is GameState) {
				var gameState:GameState = FlxG.state as GameState;
				gameState.enemies.add(new TinyEnemy(FlxG.width, FlxMath.randFloat(0, FlxG.height)));
			}
		}
	}

}