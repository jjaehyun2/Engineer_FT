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
	import flash.ui.Keyboard;
	import flash.utils.Timer;
	import flash.net.URLRequest;
	import flash.net.URLLoader;
	import Player;
	import flash.utils.ByteArray;
	//import org.as3wavsound.WavSound;
	//import org.as3wavsound.WavSoundChannel;

	/**
	 * ...
	 * @author
	 */
	public class Main extends Sprite {

		private var startScreen: StartScreen = new StartScreen();
		private var endScreen: EndScreen = new EndScreen();
		private var _bg1: Background = new Background();
		private var _bg2: Background = new Background();
		private var border: Border = new Border();
		private var userInterface:UserInterface = new UserInterface();
		public var BulletArray:Array;
		public var EnemyArray:Array;
		
		private var levelSFX:Sound;
		private var bulletSFX:Sound;
		private var tenSFX:Sound;
		private var eatSFX:Sound;
		private var friendSFX:Sound;
		private var biggerSFX:Sound;
		private var soundChannel:SoundChannel;

		private var lives: Lives = new Lives();
		

		private var cam: MovieClip = new MovieClip();

		private var char: Player = new Player();
		private var _enemy: Cowboys = new Cowboys();
		private var _dObj: DestructObjects = new DestructObjects();
		//private var cross: Crosshair = new Crosshair();

		public var vx: int = 1;
		public var vy: int = 0;

		private var _direction: Point = new Point();
		private var _enemyInPosition:Boolean = false;

		public var speed: int = 7;
		
		//var shootingSound:Sound = new ShootingSound();

		public function Main(): void {

			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);

			stage.addEventListener(KeyboardEvent.KEY_DOWN, keyDown);
			stage.addEventListener(KeyboardEvent.KEY_UP, keyUp);
			//addEventListener(Event.ENTER_FRAME, aim);
			//stage.addEventListener(MouseEvent.MOUSE_DOWN, shootingPlayer);
			
			BulletArray= new Array;EnemyArray= new Array;
			

		}
		
		public function playMain():void{
			var mainSFX:Sound = new Sound();
			mainSFX.load(new URLRequest("../Music/menu_music.mp3"));
			
			mainSFX.play(0, 10);
		}
		
		public function playSFX():void{
			var levelSFX:Sound = new Sound();
			levelSFX.load(new URLRequest("../Music/gameplay_music.mp3"));
			
			levelSFX.play(0, 10);
		}
		
		//var loader:URLLoader = new URLLoader();
		//loader.dataFormat = 'binary';
		//loader.addEventListener(Event.COMPLETE, completeHandler);
		//loader.load(new URLRequest("gallop_loop.wav"));
		//
		//
		//function completeHandler(e:Event):void{
			//var sound:WavSound = new WavSound(e.target.data as ByteArray);
			//sound.play();
		//}

		private function init(e: Event = null): void {
			removeEventListener(Event.ADDED_TO_STAGE, init);
			// entry point

			addChild(startScreen);
			addChild(border);
			stage.addEventListener(MouseEvent.MOUSE_DOWN, showStartScreen);
			//stage.addEventListener(KeyboardEvent.KEY_DOWN, showBorder);
			playMain();
		

			this.addEventListener(Event.ENTER_FRAME, loop);
			
			

		}
		
		

		public function startGame(): void {
			
			//addChild(background);
			backgroundCycle();
			addChild(lives);
			
			//addEnemies();
			addPlayer();
			addDesObj();
			playSFX();
			//Gallop();
			//playMain.stop();
			
			addChild(border);
			addChild(userInterface);

			addChild(cam);
			
		}
		
		//public function clearStage(): void
		//{
			//removeChild(backgroundCycle);
			//removeChild(lives);
			//removeChild(addEnemies);
			//removeChild(addPlayer);
			//removeChild(addDesObj);
		//}
		
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
			trace();

			char.y += _direction.y * speed;
			char.x += _direction.x * speed;
			
			//_enemy.y += Math.random() * speed;
			_enemy.x += speed;
			
			if(_enemy.y >= 10 || _enemy.y <= 1210){
				_enemy.y = speed * -1;
			}
			
			if (_enemy.x > 0){
				_enemyInPosition = true;
			}
			
			
			char.adjust();
			_enemy.adjust();

			stage.addEventListener(KeyboardEvent.KEY_DOWN, test);

			//background.x -= speed * 2;
			
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
		public function addBullet(): void
		{
			//bullet.x = 50;
		}
		
		public function addPlayer(): void {
			char.x = stage.stageWidth / 2;
			char.y = stage.stageHeight / 2;
			addChild(char);
		}

		/*public function addEnemies(): void {
			_enemy.x = -800;
			//_enemy.y = Math.random() * stage.stageHeight;
			addChild(_enemy);			
		}*/
		
		private function createaddEnemies(amount:int):void
		{
			for (var i:int = 0; i < amount; i++)
			{
				EnemyArray.push(new Cowboys);//0			
				addChildAt(_enemy[i], i+1);
			}
		}

		public function addDesObj(): void {
			_dObj.x = Math.random() * stage.stageWidth;
			_dObj.y = Math.random() * stage.stageHeight + 200;
			cam.addChild(_dObj);
		}

		public function showStartScreen(e: Event): void {
			
			if (startScreen.buttonImage.parent && startScreen.buttonImage.hitTestPoint(mouseX,mouseY)) {
				
				removeEventListener(MouseEvent.MOUSE_DOWN, showStartScreen);
				removeChild(startScreen);
				trace("Event removed");
					
			
				
			}

			this.addEventListener(Event.ENTER_FRAME, loop);
			startGame();		
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