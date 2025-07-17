package
// TODO 22/Abr: Criar mapa
{

	import flash.accessibility.Accessibility;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.net.URLLoader;
	import flash.net.URLRequest;
	import flash.utils.ByteArray;
	import org.flixel.*;
	import org.flixel.plugin.photonstorm.FlxButtonPlus;

	public class PlayState extends FlxState

	{
		[Embed(source = 'img/background.png')] private var IMG_BACKGROUND:Class;
		[Embed(source = 'img/idle_16.png')] private var IMG_ABDUCTABLE_01:Class;
		[Embed(source = 'img/TractorBeam.png')] private var IMG_TRACTORBEAM:Class;
		[Embed(source = 'img/tileset_castle_line.png')] private var IMG_TILESET:Class;
		
		[Embed(source = 'img/btn_pause_normal.png')] private const IMG_BTN_PAUSE_NORMAL:Class;
		[Embed(source = 'img/btn_pause_resume.png')] private const IMG_BTN_PAUSE_RESUME:Class;
		
		[Embed(source = 'img/overlaymenu_bg.png')] private const IMG_PAUSE_BG:Class;
		[Embed(source = 'img/btn_menu.png')] private const IMG_PAUSE_BTN_MENU:Class;
		[Embed(source = 'img/btn_next.png')] private const IMG_PAUSE_BTN_NEXT:Class;
		[Embed(source = 'img/btn_restart.png')] private const IMG_PAUSE_BTN_RESTART:Class;
		[Embed(source = 'img/btn_sound.png')] private const IMG_PAUSE_BTN_SOUND:Class;
		
		[Embed(source = 'img/particle.png')] private const IMG_PARTICLE:Class;
		
		private const SPRITE_WIDTH:int = 16;
		private const SPRITE_HEIGHT:int = 16;
		private const TILE_WIDTH:int = 16;
		private const TILE_HEIGHT:int = 16;
		
		private const ANIM_SLEEP_NAME:String = "sleep";
		private const ANIM_SLEEP:Array = [0, 1, 2, 3, 2, 1];
		private const ANIM_FPS:int = 4;
		
		private const IDX_SPRITE_NAME:int = 0;
		private const IDX_SPRITE_X:int = 1;
		private const IDX_SPRITE_Y:int = 2;
		
		private const MENU_X:int = 150;
		private const MENU_Y_INIT:int = -65;
		private const MENU_Y_VISIBLE:int = (240/2) - 30;
		
		private const KEY_IMG_ABD_01:String = "idle_16";
		
		private const STATE_ONGOING:int = 100;
		private const STATE_FINISHED_WIN:int = 101;
		private const STATE_FINISHED_LOSE:int = 102;
		
		private var tractorBeam:FlxSprite = new FlxSprite(0,0);
		private var background:FlxSprite = new FlxSprite(0,0);
		
		private var lastMouseX:int;
		private var mouseDownX:int;
		private var _mapHit:FlxTilemap;
		private var _mapBg:FlxTilemap;
		
		private var abductables:FlxGroup;
		private var layerGameObjects:FlxGroup;
		private var layerLevelCollision:FlxGroup;
		private var layerLevelBG:FlxGroup;
		private var layerHUD:FlxGroup;
		
		private var levelFactory:LevelFactory;
		private var currentLevel:Level;
		private var currentLevelID:int;
		
		private var btnPause:FlxButton;
		private var btnPauseResume:FlxButton;
		
		private var pauseBG:FlxSprite;
		private var pauseBtnMenu:FlxButton;
		private var pauseBtnNext:FlxButton;
		private var pauseBtnRestart:FlxButton;
		private var pauseBtnSound:FlxButton;
		
		private var gamePaused:Boolean = false;
		
		private var abductablesCount:int = 0;
		
		// PauseMenu >>
		private var pauseMenu:FlxGroup;// InGameMenu;
		private var btnNext:FlxButton;
		private var btnBack:FlxButton;
		// << PauseMenu
		
		private var gameState:int;
		
		override public function PlayState(level:int)
		{
			levelFactory = new LevelFactory();
			currentLevel = levelFactory.getLevel(level);
			currentLevelID = level;
		}
		
		override public function create():void
		{
			initGroups();
			
			createBG();
			
			createTractorBeam();
			
			loadLevel();
			
			createHUD();
			
			this.add(layerLevelBG);
			this.add(layerLevelCollision);
			this.add(layerGameObjects);
			this.add(layerHUD);
			
			FlxG.stage.addEventListener(MouseEvent.MOUSE_MOVE, onMouseMove);
			
			FlxG.mouse.show();
			
			this.gameState = STATE_ONGOING;
			
			FlxG.watch(pauseMenu, "alive", "PauseMenu alive?");
			FlxG.watch(FlxG, "paused", "Game Paused?");
		}
		
		override public function destroy():void
		{
			FlxG.stage.removeEventListener(MouseEvent.MOUSE_MOVE, onMouseMove);
			if (FlxG.paused) {
				FlxG.paused = false;
			}
			super.destroy();
		}
		
		private function createHUD():void 
		{
			btnPause = new FlxButton(FlxG.width - 30, 10, null, OnClickPause);
			btnPause.loadGraphic(IMG_BTN_PAUSE_NORMAL);
			layerHUD.add(btnPause);
			
			createPauseMenu();
			layerHUD.add(pauseMenu);
		}
		
		private function createPauseMenu():void 
		{
			pauseMenu.alive = false;
			pauseMenu.exists = false;
			
			var spriteBg:FlxSprite = new FlxSprite(0, 0);
			spriteBg.makeGraphic(FlxG.width, FlxG.height, 0xDD000000);
			pauseMenu.add(spriteBg);
			
			var btnMenu:FlxButton = new FlxButton((FlxG.width / 2) - 40, 20, "Main Menu", OnClickMenu);
			pauseMenu.add(btnMenu);
			
			btnBack = new FlxButton((FlxG.width / 2) - 40, 40, "Back", OnClickPause);
			pauseMenu.add(btnBack);

			btnNext = new FlxButton((FlxG.width / 2) - 40, 60, "Next Level", OnClickNext);
			btnNext.kill();
			pauseMenu.add(btnNext);
			
			pauseMenu.alive = false;
			pauseMenu.exists = false;
		}
		
		// PauseMenu Callbacks >>
		private function OnClickMenu():void
		{
			FlxG.switchState(new LevelSelectState());
		}

		private function OnClickNext():void
		{
			FlxG.switchState(new PlayState(currentLevelID++));
		}
		// << PauseMenu Callbacks
		
		
		private function loadLevel():void 
		{
			var levelSprite:Class = currentLevel.getSpr();
			var ba:ByteArray = new levelSprite();
			var spriteMap:String = ba.readUTFBytes(ba.length);
			LoadLevelAbductables(spriteMap);
			
			var levelBg:Class = currentLevel.getBg();
			_mapBg = new FlxTilemap();
			_mapBg.loadMap(new levelBg, IMG_TILESET, TILE_WIDTH, TILE_HEIGHT);
			layerLevelBG.add(_mapBg);
			
			_mapHit = new FlxTilemap();
			var levelHit:Class = currentLevel.getHit();
			_mapHit.loadMap(new levelHit, IMG_TILESET, TILE_WIDTH, TILE_HEIGHT);
            layerLevelCollision.add(_mapHit);
		}
		
		
		private function initGroups():void 
		{
			abductables = new FlxGroup();
			layerGameObjects = new FlxGroup();
			layerLevelCollision = new FlxGroup();
			layerLevelBG = new FlxGroup();
			layerHUD = new FlxGroup();
			pauseMenu = new FlxGroup();
		}
		
		
		private function createBG():void 
		{
			background.loadGraphic(IMG_BACKGROUND, false, false);
			this.add(background);
		}
		
		
		private function createTractorBeam():void 
		{
			tractorBeam.loadGraphic(IMG_TRACTORBEAM, true, true, 30, 240, true);
			tractorBeam.addAnimation("beaming", [0, 1, 2, 1], 4, true);
			tractorBeam.play("beaming");
			tractorBeam.y = 0;
			tractorBeam.visible = false;
			tractorBeam.solid = true;
			
			layerGameObjects.add(tractorBeam);
		}
		
		private function OnClickPause():void
		{
			trace("OnClickPause");
			FlxG.paused = !FlxG.paused;
			
			if (FlxG.paused) {
				pauseMenu.revive();
				trace("Revive");
			} else {
				pauseMenu.alive = false;
				pauseMenu.exists = false;
				trace("Kill");
			}
		}
		
		private function LoadLevelAbductables(data:String):void 
		{
			var lines:Array = data.split(/\n/);
			for each (var line:String in lines) {
				if (line.length > 0) {
					var abductableLine:Array = line.split(/,/);
					var ab:AbductableObject = new AbductableObject(abductableLine[IDX_SPRITE_X], abductableLine[IDX_SPRITE_Y]);
					ab.loadGraphic(GetSpriteClass(abductableLine[IDX_SPRITE_NAME]), true, true, SPRITE_WIDTH, SPRITE_WIDTH, true);
					ab.addAnimation(ANIM_SLEEP_NAME, ANIM_SLEEP, ANIM_FPS, true);
					ab.play(ANIM_SLEEP_NAME);
					abductables.add(ab);
				}
			}
			
			this.abductablesCount = abductables.countLiving();
			
			trace("Abductables on the Level: " + this.abductablesCount);
			
			layerGameObjects.add(abductables);
		}
		
		private function GetSpriteClass(key:String):Class 
		{
			var result:Class;
			
			switch (key) {
				case KEY_IMG_ABD_01:
					result = IMG_ABDUCTABLE_01;
					break;
				default:
					break;
			}
			
			return result;			
		}
		
		private function LiftAbductables(obj1:FlxObject,obj2:FlxObject):void 
		{
			if (obj1 != null)
			{
				(obj1 as AbductableObject).lift();
			}
		}
		
			
		public function onMouseMove(event:MouseEvent):void
		{
			if (FlxG.mouse.pressed()) {
				var deltaX:int = FlxG.mouse.screenX - this.lastMouseX;
				trace("deltaX: " + deltaX);
				
				if (!this.gamePaused) {
					for each (var ab:AbductableObject in abductables.members) {
						if (deltaX > 0)
						{
							ab.dragRight();
						} else if (deltaX < 0) {
							ab.dragLeft();
						}
					}
				}
				
				this.lastMouseX = FlxG.mouse.screenX;
			}
		}
		
		override public function update():void
		{
			
			if (FlxG.keys.justPressed("P")) {
				OnClickPause();
			}
			
			if (!FlxG.paused) {
				//pauseMenu.kill();
				//switch (gameState) {
					//case STATE_ONGOING:
						checkMouseInteraction();
						checkForTractorBeamCollision();
						checkForAbduction();
						collisionDetection();
						super.update();
					//break;
					//case STATE_FINISHED_WIN:
						//pauseMenu.setMessage(InGameMenu.MESSAGE_WIN);
						//pauseMenu.revive();
						//pauseMenu.showNext();
						//btnNext.revive();
						//pauseMenu.revive();
						//pauseMenu.update();
						//trace("Win!");
					//break;
					//case STATE_FINISHED_LOSE:
						//trace("Lose!");
					//break;
				//}
			} else {
				layerHUD.update();
			}
		}
		
		private function collisionDetection():void 
		{
			FlxG.collide(_mapHit, abductables);
			for each (var ab:AbductableObject in this.abductables.members) {
				var stop:Boolean = false;
				if (ab.x >= (FlxG.width - ab.width) && ab.velocity.x > 0) {
					stop = true;
				}
				if (ab.x <= 1 && ab.velocity.x < 0) {
					stop = true;
				}
				
				if (stop) {
					ab.velocity.x = 0;
					ab.acceleration.x = 0;	
				}
			}
		}
		
		
		private function checkMouseInteraction():void 
		{
			if (FlxG.mouse.pressed() && (!btnPause.overlapsPoint(FlxG.mouse.getScreenPosition()))) {
				tractorBeam.x = FlxG.mouse.screenX - (tractorBeam.width / 2);
				tractorBeam.visible = true;
			} else {
				tractorBeam.visible = false;
			}
			
			if (FlxG.mouse.justReleased()) {
				for each (var ab:AbductableObject in abductables.members) {
					ab.drop();				
				}
			}
		}
		
		
		private function checkForTractorBeamCollision():void 
		{
			if (tractorBeam.visible) {
				FlxG.overlap(abductables, tractorBeam, LiftAbductables);
			}
		}
		
		
		private function checkForAbduction():void 
		{
			for each (var ab:AbductableObject in abductables.members) {
				if (ab != null && ab.alive && ab.y <= (ab.height * -1)) {
					ab.kill();
					this.abductablesCount--;
					trace("Abductables on the Level: " + this.abductablesCount);
				}
			}
			
			if (this.abductablesCount <= 0) {
				this.gameState = STATE_FINISHED_WIN;
			}
		}
		
		
	}

}