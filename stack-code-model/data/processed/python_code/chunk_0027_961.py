/*
** Source code Copyright 2006, Andrew Rapo
** May be used in non-commercial and commercial applications
** as long as the author is credited
*/

package org.rapo.games.astro.managers  {
	
	import flash.display.MovieClip;
	
	import org.rapo.games.astro.GameTimer;
	import org.rapo.games.astro.Powerup;
	import org.rapo.games.astro.managers.ObjectManager;
	import org.rapo.games.astro.managers.ScoreManager;
	
	public class PowerupManager {
	
		public static var TOTAL_FRAMES:Number = 107;
		public static var POWERUP_LIFESPAN:Number = 10000;
		public static var POWERUP_DURATION:Number = 15000;
		
		public static var mc:MovieClip;
		public static var currentFrame:Number;
		public static var elapsedTime:Number;
		public static var powerupTimer:GameTimer;
		public static var activePowerup:Powerup;
			
		public static function initialize(movie_clip:flash.display.MovieClip) {
			mc = movie_clip;
			currentFrame = 1;
			mc.gotoAndStop(currentFrame);
			powerupTimer = new GameTimer();
		}
	
		public static function reset():void {
			activePowerup = null;
			mc.powerUpList.gotoAndPlay("none");
			mc.gotoAndStop(1);
		}
	
		public static function update():void {
	
			if (activePowerup != null) {
				elapsedTime = powerupTimer.milliseconds();
				currentFrame = TOTAL_FRAMES * (elapsedTime / POWERUP_DURATION);
				currentFrame = Math.floor(currentFrame);
				
				if (currentFrame > TOTAL_FRAMES) currentFrame = TOTAL_FRAMES;
		
				if (mc.currentFrame != currentFrame) {
					mc.gotoAndStop(currentFrame);
				}
				if (elapsedTime > POWERUP_DURATION) {
					deactivatePowerup();
				}
			}
		}
	
		public static function activatePowerup(powerup:Powerup):void {
			activePowerup = powerup;
			invoke(activePowerup.type);
			powerupTimer.restartTimer();
			mc.powerUpList.gotoAndPlay(activePowerup.type);
		}
			
		public static function deactivatePowerup():void {
			revoke(activePowerup.type);
			activePowerup = null;
			mc.powerUpList.gotoAndPlay("none");
			mc.gotoAndStop(1);
		}
		
		public static function invoke(type:String):void {
			switch (type) {
				case ("pu_energy_type"):
					ScoreManager.lives = ScoreManager.MAX_LIVES;
					break;
				case ("pu_multishot_type"):
					ObjectManager.ship.multiShot = true;
					break;
				case ("pu_shield_type"):
					ObjectManager.ship.setShielded(true);
					break;
				case ("pu_tailgun_type"):
					ObjectManager.ship.tailGun = true;
					break;
				default:
					break;
			}
		}
	
		public static function revoke(type:String):void {
			switch (type) {
				case ("pu_energy_type"):
					ScoreManager.lives = ScoreManager.MAX_LIVES;
					break;
				case ("pu_multishot_type"):
					ObjectManager.ship.multiShot = false;
					break;
				case ("pu_shield_type"):
					ObjectManager.ship.setShielded(false);
					break;
				case ("pu_tailgun_type"):
					ObjectManager.ship.tailGun = false;
					break;
				default:
					break;
			}
		}
	}
}