﻿package dagd.powers {

	import dagd.core.Game;
	import dagd.core.App;
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.text.TextFieldAutoSize;
	import dagd.powers.scripts.*;
	import flash.display3D.IndexBuffer3D;

	public class GamePowers extends Game {

		private var buzzsaws: Array = new Array(); // make an empty array for buzzsaws
		private var spears: Array = new Array(); // make an empty array for spears
		private var katanas: Array = new Array(); // make an empty array for katanas

		private var countdownTimerE1: int = 0; //this timer is used for the buzzsaw object spawn rate
		private var countdownTimerE2: int = 0; //this timer is used for the spear object spawn rate
		private var countdownTimerE3: int = 0; //this timer is used for the buzzsaw object spawn rate

		private var mutes: Array = new Array(); // make an empty array for mutes
		private var multis: Array = new Array(); // make an empty array for multis
		private var hearts: Array = new Array(); // make an empty array for hearts	

		private var countdownTimerH1: int = 0; //this timer is used for the heart object spawn rate
		private var countdownTimerH2: int = 0; //this timer is used for the multi object spawn rate
		private var countdownTimerH3: int = 0; //this timer is used for the heart object spawn rate

		private var introTimer: int = 800; //this timer is used to slowly introduce elements
		private var healingTimer: int = 200; //this timer is used to determine how long since last hit for the healing feature
		private var stageTimer: int = 600; //this timer determines when the next stage starts

		private var playerTimer: int = 0; //tracks overall time

		private var hud: PowersHUD;
		private var background: PowersBack;
		private var oob: OOB;
		private var damageEffect: DamageEffect;
		private var gameOver: GameOver;

		private var seeCulling: Boolean = false; //debug variable to see out of bounds

		private var health: Number = 100; //this tracks the player's current health
		private var score: Number = 0; //this tracks the player's current score
		private var level: Number = 1; //the stage number determines spawn rates
		private var isDead: Boolean = false; //this tracks if the player has died

		public function GamePowers() {
			gameTitle = "Click...of DOOOOOOOM!"
			creatorName = "Aaron Powers"
		}

		override public function onStart(): void {
			hud = new PowersHUD();
			damageEffect = new DamageEffect();
			background = new PowersBack();
			if (!seeCulling) oob = new OOB();

			addChild(background);
			addChild(damageEffect);
			if (!seeCulling) addChild(oob);
			addChild(hud);

			hud.scoreText.autoSize = TextFieldAutoSize.RIGHT;
			hud.stageText.autoSize = TextFieldAutoSize.CENTER;

			addEventListener(Event.ENTER_FRAME, gameLoop);
		}

		private function gameLoop(e: Event): void {
			if (App.main.isPaused) return;
			if (!isDead) {
				//1. track the passage of time

				playerTimer++;

				countdownTimerE1--;
				countdownTimerE2--;
				countdownTimerE3--;
				countdownTimerH1--;
				countdownTimerH2--;
				countdownTimerH3--;

				introTimer--;
				healingTimer--;
				stageTimer--;

				if (introTimer < 0) introTimer = 0; //clamp the intro timer to ensure no floating point errors
				if (healingTimer < 0) healingTimer = 0; //clamp the intro timer to ensure no floating point errors

				//2. create new objects

				if (countdownTimerE1 <= 0 && introTimer < 700) {
					spawnObject(Buzzsaw, buzzsaws);
					countdownTimerE1 = (Math.random() * 40 + 40) - (level / 5);
				}

				if (countdownTimerE2 <= 0 && introTimer < 400) {
					spawnObject(Spear, spears);
					countdownTimerE2 = (Math.random() * 30 + 90) - (level / 5);
				}

				if (countdownTimerE3 <= 0 && introTimer < 1) {
					spawnObject(Katana, katanas);
					countdownTimerE3 = (Math.random() * 60 + 160) - (level / 5);
				}

				if (countdownTimerH1 <= 0 && introTimer < 700) {
					spawnObject(Mute, mutes);
					countdownTimerH1 = (Math.random() * 30 + 30) + (level / 10);
				}

				if (countdownTimerH2 <= 0 && introTimer < 400) {
					spawnObject(Multi, multis);
					countdownTimerH2 = (Math.random() * 60 + 60) + (level / 10);
				}

				if (countdownTimerH3 <= 0 && introTimer < 1) {
					spawnObject(Heart, hearts);
					countdownTimerH3 = (Math.random() * 120 + 120) + (level / 10);
				}

				//3. update objects

				objectUpdate(buzzsaws);
				objectUpdate(spears);
				objectUpdate(katanas);

				objectUpdate(hearts);
				objectUpdate(multis);
				objectUpdate(mutes);

				//4. update hud

				if (healingTimer == 0) health += 0.01666; //heal player over time if they avoid getting hit for a while

				if (health < 0) health = 0; //clamp health to min of 0
				if (health > 100) health = 100; //clamp health to min of 100

				if (health == 0) {
					isDead = true;
					gameOver = new GameOver();
					addChild(gameOver);
					gameOver.finalScore.text = "FINAL SCORE: " + score;
					gameOver.finalStage.text = "FINAL STAGE: " + level;
				}

				if (health < 30) damageEffect.healthLow = true;
				else damageEffect.healthLow = false;
				damageEffect.update();

				var h: Number = (health / 100);
				hud.healthBar.scaleX = h;

				var l: Number = (stageTimer / 600);
				hud.levelBar.scaleX = l;

				if (stageTimer == 0) {
					level += 1;
					stageTimer = 600;
				}

				hud.stageText.text = "STAGE " + level;
				hud.scoreText.text = "SCORE: " + score;

			}

		}

		override public function onEnd(): void {
			removeEventListener(Event.ENTER_FRAME, gameLoop);
		}

		//this function is used to update objects and check if they're dead;
		private function objectUpdate(objects: Array): void {
			for (var i: int = objects.length - 1; i >= 0; i--) {
				objects[i].update();
				if (objects[i].isDead == true) {
					score += objects[i].points; //check objects for points
					health -= objects[i].damage; //check objects for damage
					if (objects[i].damage > 0) {
						damageEffect.alpha = 0.60;
						healingTimer = 200;
					}
					removeChild(objects[i]); //stop drawing object
					objects.splice(i, 1); //removes #i from array
					i--;
				}
			}
		}

		//this function spawns a object and, if allowed, adds it to an array
		private function spawnObject(object: Class, objects: Array): void {
			var o = new object(); // spawns the object
			objects.push(o); // adds the object to array
			var index: int = getChildIndex(damageEffect); //checks index to ensure hud is above
			addChildAt(o, index); //set the object to render below the hud
		}
	}
}