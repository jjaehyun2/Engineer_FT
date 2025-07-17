/*
** Source code Copyright 2006, Andrew Rapo
** May be used in non-commercial and commercial applications
** as long as the author is credited
*/

package org.rapo.games.astro {
	
	import flash.display.MovieClip;
	import flash.display.Stage;
		
	import org.rapo.games.astro.managers.ObjectManager;
	import org.rapo.games.astro.managers.InputManager;
	import org.rapo.games.astro.managers.ScoreManager;
	import org.rapo.games.astro.managers.PowerupManager;
	import org.rapo.games.astro.managers.HudManager;
	import org.rapo.games.astro.managers.FrameTimeManager;
	import org.rapo.games.astro.managers.BGManager;
	import org.rapo.games.astro.managers.LevelManager;

	
	import org.rapo.games.astro.clips.mcShip;
	import org.rapo.games.astro.clips.mcCrystal;
	import org.rapo.games.astro.clips.mcDebris;
	import org.rapo.games.astro.clips.mcBullet;
	import org.rapo.games.astro.clips.mcPUBurst;
	import org.rapo.games.astro.clips.mcPUMultishot;
	import org.rapo.games.astro.clips.mcPUShield;
	import org.rapo.games.astro.clips.mcPUTbd;
	import org.rapo.games.astro.clips.mcHUD;
	import org.rapo.games.astro.clips.mcHUDPowerupTimer;
	import org.rapo.games.astro.clips.mcHUDRadar;
	import org.rapo.games.astro.clips.mcHUDStats;
	
	import org.rapo.games.astro.sounds.sndHit;
	import org.rapo.games.astro.sounds.sndExplode;
	import org.rapo.games.astro.sounds.sndPowerup;
	import org.rapo.games.astro.sounds.sndPowerupDie;

	public class GameController extends MovieClip {
	
		private var gameTimeline:MovieClip;
		private var soundtrackAudio:SoundtrackController;
		private var effectsAudio:AudioController;
		private var ship:Ship;
		private var pause:Boolean;
		private var levelPauseTimer:GameTimer;
		private var powerupTimer:GameTimer;
		private var debrisTimer:GameTimer;
		private var crystalTimer:GameTimer;
		private var inputTimer:GameTimer;
		
		public var crystal:mcCrystal;
		public var debris:mcDebris;
		public var bullet:mcBullet;
		public var puBurst:mcPUBurst;
		public var puMultishot:mcPUMultishot;
		public var puShield:mcPUShield;
		public var puTbd:mcPUTbd;
		public var hud:mcHUD;
		public var hudPowerupTimer:mcHUDPowerupTimer;
		public var hudRadar:mcHUDRadar;
		public var hudShield:mcHUDStats;
		
		public var soundHit:sndHit;
		public var soundExplode:sndExplode;
		public var soundPowerup:sndPowerup;
		public var soundPowerupDie:sndPowerupDie;
		
		public var test:MovieClip;
		public var bg:MovieClip;
	
		public function GameController() {
		
			trace("GC:Constructor");
			gameTimeline = this;
			
			effectsAudio = new AudioController();
			soundtrackAudio = new SoundtrackController("soundtrack.xml");
			soundHit = new sndHit();
			soundExplode = new sndExplode();
			soundPowerup = new sndPowerup();
			soundPowerupDie = new sndPowerupDie();
			
			effectsAudio.registerSound("explode", soundExplode);
			effectsAudio.registerSound("hit", soundHit);
			effectsAudio.registerSound("powerup", soundPowerup);
			effectsAudio.registerSound("powerupDie", soundPowerupDie);
			
			levelPauseTimer = new GameTimer();
			powerupTimer = new GameTimer();
			debrisTimer = new GameTimer();
			crystalTimer = new GameTimer();
			inputTimer = new GameTimer();
			
			ObjectManager.init(gameTimeline);
			InputManager.init(stage);
	
		}

		public function start():void  {
			
			trace("start");
			
			BGManager.initialize(gameTimeline.bg);
			ship = ObjectManager.createShip(300, 340);
			trace("start:ShipObj: " + ship);
			ship.reset();
			
			HudManager.initialize(gameTimeline);
			HudManager.setHudVisibility(true);
			
			soundtrackAudio.playTrack("main_loop", true);
			
			addEventListener ( 'enterFrame', mainLoop);
		}
		
	/*
		public function title():void  {
			
			soundtrackAudio.playTrack("title_loop", true);
		}
		
		public function play():void  {
			
			ScoreManager.reset();
		}
		
		public function nextLevel():void  {
				
			soundtrackAudio.playTrack("main_loop", true);
			ship.reset();
			ScoreManager.resetLevelTimer();
			ScoreManager.resetLevelScore();
			debrisTimer.restartTimer();
			crystalTimer.restartTimer();
			PowerupManager.reset();
			HudManager.setHudVisibility(true);
		}	
*/

		public function mainLoop(arg:Object):void  {
			
			FrameTimeManager.calculateFrameTime();
			InputManager.processKeyboardInput();
			handleInput();
			
			if (!pause) {
		
				if (checkGameOver()) {
					//gameTimeline.gotoAndPlay("gameOver");
				} else if (checkLevelComplete() && !ship.over) {
					//gameTimeline.gotoAndPlay("levelComplete");
				
				} else {
					moveObjects("objects");
					moveObjects("bullets");
					ship.move();
					checkCollision("objects", "bullets");
					checkShipCollision("objects");
					BGManager.sync(ship);
				}
				HudManager.update();
				spawnPowerups();
				spawnDebris();
				spawnCrystals();
			}
		}

		public function checkLevelComplete():Boolean {
			
			if (ScoreManager.hits >= LevelManager.getTargetHits()) return true;
			
			return false;
		}
		
		public function checkGameOver():Boolean {
			
			if (ScoreManager.lives <= 0) {
				ship.over = true;
			}
			return !ship.alive;
		}
	
/*		
		public function levelComplete():void  {
			levelPauseTimer.restartTimer();
			soundtrackAudio.playTrack("level_loop", true);
			destroyObjects("bullets");
			destroyObjects("objects");
			ship.reset();
			ScoreManager.updateScore();
			gameTimeline.screen_level_complete.level_score_txt.text = ScoreManager.levelScore;
			gameTimeline.screen_level_complete.level_bonus_txt.text = ScoreManager.levelBonus;
			gameTimeline.screen_level_complete.total_score_txt.text = ScoreManager.totalScore;
			HudManager.setHudVisibility(false);
		}
		
		public function win():void  {
			levelPauseTimer.restartTimer();
			soundtrackAudio.playTrack("level_loop", true);
			destroyObjects("bullets");
			destroyObjects("objects");
			ship.reset();
			ScoreManager.updateScore();
			gameTimeline.screen_win.score_txt.text = ScoreManager.score;
			gameTimeline.screen_win.bonus_txt.text = ScoreManager.bonus;
			gameTimeline.screen_win.total_score_txt.text = ScoreManager.totalScore;
			HudManager.setHudVisibility(false);
		}
		
		public function gameOver():void  {
			levelPauseTimer.restartTimer();
			soundtrackAudio.playTrack("level_loop", true);
			destroyObjects("bullets");
			destroyObjects("objects");
			ship.reset();
			ScoreManager.updateScore();
			gameTimeline.screen_game_over.score_txt.text = ScoreManager.score;
			gameTimeline.screen_game_over.bonus_txt.text = ScoreManager.bonus;
			gameTimeline.screen_game_over.total_score_txt.text = ScoreManager.totalScore;
			HudManager.setHudVisibility(false);	
		}
*/
		public function handleInput():void  {
			
			if (InputManager.inputState[InputManager.QUIT]) {
				gameTimeline.gotoAndPlay("gameOver");
			}
			
			if (InputManager.inputState[InputManager.ROTATE_LEFT]) {
				ship.rotate("left");
			}
			
			if (InputManager.inputState[InputManager.ROTATE_RIGHT]) {
				ship.rotate("right");
			}
			
			if (InputManager.inputState[InputManager.FORWARD]) {
				ship.thrust(1);
			} else if (InputManager.inputState[InputManager.BACK]) {
				ship.thrust(-1);
			} else {
				ship.thrustOff();
			}
				
			if (InputManager.inputState[InputManager.SHOOT]) {
				ship.shoot();
			}
			
			if (InputManager.inputState[InputManager.USE_POWERUP]) {
				PowerupManager.deactivatePowerup();
			}
			
			if (InputManager.inputState[InputManager.XTRA]) {
				if (inputTimer.milliseconds() > 250) {
					pause = !pause;
					FrameTimeManager.frameTimeTimer.restartTimer();
					inputTimer.restartTimer();
					ScoreManager.lives = ScoreManager.MAX_LIVES;
				}
			}
		}

		public function moveObjects(array_id:String):void {
			
			var thisArray:Array = ObjectManager.arrays[array_id];
			for (var i:Number=0; i < thisArray.length; i++) {
				
				var thisObject:BaseObject = BaseObject(thisArray[i]);
				if (thisObject.alive) {
					thisObject.move();
				} else {
					thisObject.destroy();
					thisObject = null;
					ObjectManager.removeObject(array_id, i);
				}
			}
		}
	
		public function checkShipCollision(object_array_id:String):void {
			
			var objectArray:Array = ObjectManager.arrays[object_array_id];
			
			for (var i:Number=0; i < objectArray.length; i++) {
	
				var object:BaseObject = BaseObject(objectArray[i]);
				if (object.alive) {
					if (ship.mc.hit_target.hitTestObject(object.mc)) {
						if (object is Powerup){
							if (PowerupManager.activePowerup == null) {
								PowerupManager.activatePowerup(Powerup(object));
								object.alive = false;
								object.hit(object);
								effectsAudio.playSound("powerup", false);
							}
						} else {
							if (!ship.shieldOn) {
								ScoreManager.lives -= 1;
								object.alive = false;
								ship.bounce(object);
								effectsAudio.playSound("hit", false);
							}
						}
					}
				}
			}
		}
			
		public function checkCollision(	object_array_id:String,
										projectile_array_id:String):void {
			
			var objectArray:Array = ObjectManager.arrays[object_array_id];
			var projectileArray:Array = ObjectManager.arrays[projectile_array_id];
			
			for (var i:Number=0; i < objectArray.length; i++) {
				for (var j:Number=0; j < projectileArray.length; j++) {
					
					var object:BaseObject = BaseObject(objectArray[i]);
					var projectile:BaseObject = BaseObject(projectileArray[j]);
					
					if (projectile.alive) {
						if (projectile.mc.hit_target.hitTestObject(object.mc.hit_target)) {
							ScoreManager.updateLevelScore(100);
							object.alive = false;
							projectile.alive = false;
							if (object is Powerup){
								object.die();
								effectsAudio.playSound("powerupDie", false);
							} else if (object is Debris) {
								ObjectManager.splitDebris(Debris(object), object_array_id);
								ScoreManager.hits +=1;
								effectsAudio.playSound("explode", false);
							} else {
								effectsAudio.playSound("explode", false);
							}
						}
					}
				}
			}
		}
		
		public function destroyObjects(array_id:String):void {
			
			var thisArray:Array = ObjectManager.arrays[array_id];
			for (var i:Number=0; i < thisArray.length; i++) {
				
				var thisObject:BaseObject = BaseObject(thisArray[i]);
				thisObject.destroy();
				thisObject = null;
			}
			ObjectManager.resetArray(array_id);
		}
		
		public function spawnPowerups():void {
			
			if (powerupTimer.milliseconds() > LevelManager.getPowerupInterval()) {
				
				var coords:Object = new Object;
				LevelManager.setSpawnInfo(coords);
				var tempPowerup:Powerup = ObjectManager.createPowerup(coords.x,coords.y,coords.type);
				ObjectManager.addObject(tempPowerup, "objects");
				tempPowerup.move();
				powerupTimer.restartTimer();
			}
		}
		
		public function spawnDebris():void {
			
			if (debrisTimer.milliseconds() > LevelManager.getDebrisInterval()) {
				
				var info:Object = new Object;
				LevelManager.setSpawnInfo(info);
				var tempDebris:Debris = ObjectManager.createDebris(info.x,info.y,info.angle);
				ObjectManager.addObject(tempDebris, "objects");
				tempDebris.move();
				debrisTimer.restartTimer();
			}
		}
		
		public function spawnCrystals():void {
			
			if (crystalTimer.milliseconds() > LevelManager.getCrystalInterval()) {
				
				var info:Object = new Object;
				LevelManager.setSpawnInfo(info);
				var tempCrystal:Crystal = ObjectManager.createCrystal(info.x,info.y,info.angle);
				ObjectManager.addObject(tempCrystal, "objects");
				tempCrystal.move();
				crystalTimer.restartTimer();
			}
		}
	}
}