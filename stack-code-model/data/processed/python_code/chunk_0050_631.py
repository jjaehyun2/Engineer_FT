package {
	//import flash.display.Bullet;
	import flash.display.MovieClip;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.KeyboardEvent;
	import flash.events.MouseEvent;
	import flash.events.TimerEvent;
	import flash.geom.Point;
	import flash.media.Sound;
	import flash.media.SoundChannel;
	import flash.net.URLLoader;
	import flash.net.URLRequest;
	import flash.ui.Keyboard;
	import flash.utils.ByteArray;
	import flash.utils.Timer;
	
	import Player;
	//import org.as3wavsound.WavSound;
	//import org.as3wavsound.WavSoundChannel;

	/**
	 * ...
	 * @author
	 */
	public class Main extends Sprite {

		private var startScreen:StartScreen = new StartScreen();
		private var endScreen: EndScreen = new EndScreen();
		private var _bg1: Background = new Background();
		private var _bg2: Background = new Background();
		private var border: Border = new Border();
		private var userInterface:UserInterface = new UserInterface();
		
		
		private var levelSFX:Sound;
		private var bulletSFX:Sound;
		private var tenSFX:Sound;
		private var eatSFX:Sound;
		private var friendSFX:Sound;
		private var biggerSFX:Sound;
		private var soundChannel:SoundChannel;

		private var lives: Lives = new Lives();

		public var enemies:Array;
		private var _enemy:Cowboys;
		
		private var char: Player = new Player();
		
		private var _dObj: DestructObjects = new DestructObjects();
		//private var cross: Crosshair = new Crosshair();

			
		public var vx: int = 1;
		public var vy: int = 0;

		private var _direction: Point = new Point();
		public var speed: int = 7;
				
		//var shootingSound:Sound = new ShootingSound();

		
		public function Main(): void {

			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);

			stage.addEventListener(KeyboardEvent.KEY_DOWN, keyDown);
			stage.addEventListener(KeyboardEvent.KEY_UP, keyUp);
			
			//addEventListener(Event.ENTER_FRAME, aim);
			//stage.addEventListener(MouseEvent.MOUSE_DOWN, shootingPlayer);			
			
		}
		
				
	
		private function init(e: Event = null): void {
			removeEventListener(Event.ADDED_TO_STAGE, init);
		

			addChild(startScreen);
			addChild(border);
			
			enemies = new Array();
			for (var i:int = 0; i < 3; i++)
			{
				_enemy = new Cowboys();
				enemies.push(_enemy);
				
				_enemy.x = -900;
				addChild(_enemy);
				
				this.x += speed;
				this.y = Math.random();
			}
				trace(i);
			
			playMain();
		
		
			this.addEventListener(Event.ENTER_FRAME, loop);
			this.addEventListener(MouseEvent.MOUSE_DOWN, showStartScreen);
			stage.addEventListener(KeyboardEvent.KEY_DOWN, test);
			
			

		}
		
		

		public function startGame(): void {
			
			backgroundCycle();
			addChild(lives);
			
			addPlayer();
			addDesObj();
			playSFX();
			
			
			
			
			addChild(border);
			addChild(userInterface);

			
			
		}
		
		private function onShoot(e:Event):void 
		{
			var missedAll:Boolean = true;		
			if (mouseY != enemies[i].y)
			{	
				var l:int = enemies.length;
				for (var i:int = l - 1; i >= 0; i--)
				{
					if (enemies[i].hitTestPoint(mouseX, mouseY))
					{
						missedAll = false;
						//scoreboard.score += 100;						
						enemies[i].destroy();
						removeChild(enemies[i]);
						enemies.splice(i, 1);
						enemies[i].y = Math.random() * stage.stageHeight;
						if (enemies.length == 0)
						{
							//pauseTimer = new Timer(2000, 1);
							////pauseTimer.addEventListener(TimerEvent.TIMER_COMPLETE, onReload);
							//
							//pauseTimer.start();
							
						}						
						break;						
					}				
				}
				
				trace("hit");
			}
			if (missedAll)
			{
				//scoreboard.score -= 200;
			}
		}
		
	
		
		public function shootingPlayer(e:Event):void{
			//var theBullet:Bullet = new Bullet(new Point(stage.mouseX, stage.mouseY), x, y); //create the bullet
			//shootingSound.play();
			//stage.addChildAt(theBullet, MovieClip(root).getChildIndex(this)); //add it to the screen
		}
		
		

		public function loop(e: Event): void {
			/*
			trace(wDown);
			trace(aDown);
			trace(sDown);
			trace(dDown);
			trace(vx);
			trace(vy);
			trace(_enemy.x);
			trace(_enemyInPosition);
			*/
		
			

			char.y += _direction.y * speed;
			char.x += _direction.x * speed;
			
			
			_enemy.x += speed;
			
			
			char.adjust();
			_enemy.adjust();
			
			var l:int = enemies.length;
			for (var i:int = 0; i < l; i++) 
			{
				enemies[i].x += speed;
				
			}
							
		}
		
		private function removeEnemy(e:Event):void 
		{
			removeEventListener(Event.REMOVED_FROM_STAGE, removeEnemy);
			
		}
		
		/*	Lives	*/

		//Lives Check
		private function checkLives(): void {
			if (lives.live == 0) {
				trace("no lives left");
				
				//removeChild(background);
				removeChild(userInterface);
				
				addChild(endScreen);
				//addChildAt(border, 1);
				
				
				stage.addEventListener(KeyboardEvent.KEY_DOWN, showEndScreen);
				//stage.addEventListener(KeyboardEvent.KEY_DOWN, showBorder);
			}
		}

		//Minus Lives
		private function test(e: KeyboardEvent): void {
			stage.removeEventListener(KeyboardEvent.KEY_DOWN, test);

			if (e.keyCode == Keyboard.SPACE) {
				lives.live -= 1;
			}

			checkLives();
		}

		/*	Add things	*/
		
		public function playMain():void{
			var mainSFX:Sound = new Sound();
			mainSFX.load(new URLRequest("../Music/menu_music.mp3"));
			
			mainSFX.play(0, 10);		
			
		}
		
		public function playSFX():void{
			var levelSFX:Sound = new Sound();
			levelSFX.load(new URLRequest("../Music/gameplay_music.mp3"));
			
			levelSFX.play(0, 10);
			
			var gallopSFX:Sound = new Sound();
			gallopSFX.load(new URLRequest("../audio/gallop_loop.mp3"));
			
			gallopSFX.play(0, 10)
		}
		
		
		public function addBullet(): void
		{
			//bullet.x = 50;
		}
		
		public function addPlayer(): void {
			char.x = stage.stageWidth / 2;
			char.y = stage.stageHeight / 2;
			addChild(char);
		}
		
		
		public function addDesObj(): void {
			_dObj.x = Math.random() * stage.stageWidth;
			_dObj.y = Math.random() * stage.stageHeight + 200;
			
		}

		public function showStartScreen(e: MouseEvent = null): void {
			
			if (startScreen.buttonImage.parent && startScreen.buttonImage.hitTestPoint(mouseX,mouseY)) {
				
				removeEventListener(MouseEvent.MOUSE_DOWN, showStartScreen);
				startGame();
				addChild(_enemy);

				
			}

			this.addEventListener(Event.ENTER_FRAME, loop);
			
			
			
		}
		
		private function backgroundCycle():void {
			addChild(_bg1);
			addChild(_bg2);
			
			_bg1.x = -200;
			_bg2.x = _bg1.width - 400;
			
			stage.addEventListener(Event.ENTER_FRAME, backgroundScroll);
			
			function backgroundScroll(e:Event):void {
				_bg1.x -= speed * 2;
				_bg2.x -= speed * 2;
				
				if(_bg1.x < -_bg1.width){
					_bg1.x = _bg2.width - 100;
				}else if(_bg2.x < -_bg2.width){
					_bg2.x = _bg1.width - 200;
				}
				
			}			
			
		}

		private function showEndScreen(e: Event): void {
			stage.removeEventListener(KeyboardEvent.KEY_DOWN, showEndScreen);
			stage.removeEventListener(Event.ENTER_FRAME, loop);
		}

		private function playerShot():void 
		{
			
		}
		
		/*	Movement + Velocity 	*/
		public function keyDown(e: KeyboardEvent): void {
			if (e.keyCode == Keyboard.W) {
				_direction.y = -1;
			}

			if (e.keyCode == Keyboard.A) {
				_direction.x = -1;
			}

			if (e.keyCode == Keyboard.S) {
				_direction.y = 1;
			}

			if (e.keyCode == Keyboard.D) {
				_direction.x = 1;
			}
		}
		
		private function keyUp(e: KeyboardEvent): void {
			if (e.keyCode == Keyboard.W) {
				_direction.y = 0;
			}

			if (e.keyCode == Keyboard.A) {
				_direction.x = 0;
			}

			if (e.keyCode == Keyboard.S) {
				_direction.y = 0;
			}

			if (e.keyCode == Keyboard.D) {
				_direction.x = 0;
			}

			//Velocity Check
			if (e.keyCode == Keyboard.W && vy != 1) {
				vx = 0;
				vy = -1;
			}

			if (e.keyCode == Keyboard.A && vx != 1) {
				vx = -1;
				vy = 0;
			}

			if (e.keyCode == Keyboard.S && vy != -1) {
				vx = 0;
				vy = 1;
			}

			if (e.keyCode == Keyboard.D && vx != -1) {
				vx = 1;
				vy = 0;
			}	
		}
	}
}