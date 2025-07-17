package com.illuzor.otherside.graphics.screens {
	
	import com.illuzor.otherside.constants.MovableType;
	import com.illuzor.otherside.constants.WeaponType;
	import com.illuzor.otherside.controllers.ControlManager;
	import com.illuzor.otherside.controllers.WeaponsController;
	import com.illuzor.otherside.events.ControlManagerEvent;
	import com.illuzor.otherside.events.LevelControllerEvent;
	import com.illuzor.otherside.events.WeaponEvent;
	import com.illuzor.otherside.graphics.bullets.player.BulletBase;
	import com.illuzor.otherside.graphics.bullets.player.GunBullet;
	import com.illuzor.otherside.graphics.characters.Asteroid;
	import com.illuzor.otherside.graphics.characters.MovableObject;
	import com.illuzor.otherside.graphics.characters.Ship1;
	import com.illuzor.otherside.graphics.screens.elements.Background;
	import com.illuzor.otherside.interfaces.ILevelController;
	import com.illuzor.otherside.utils.intRandom;
	import flash.geom.Rectangle;
	import starling.display.DisplayObjectContainer;
	import starling.events.Event;
	import starling.textures.Texture;
	import starling.textures.TextureAtlas;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class GameScreen extends ScreenBase {
		
		private const FRAMES_BEFORE_CLEAN:uint = 250;
		
		private var framesCounter:uint;
		private var atlas:TextureAtlas;
		private var background:Background;
		private var currentPlayerSpeed:int;
		private var playerShip:Ship1;
		private var gunTexture:Texture;
		private var controller:ILevelController;
		private var weaponsController:WeaponsController;
		private var controlManager:ControlManager;
		
		// lists
		private var movables:Vector.<MovableObject>;
		private var bullets:Vector.<BulletBase>;
		private var asteroids:Vector.<Asteroid>;
		
		public function GameScreen(atlas:TextureAtlas, controller:ILevelController) {
			this.controller = controller;
			this.atlas = atlas;
			movables = new Vector.<MovableObject>();
			bullets = new Vector.<BulletBase>();
			asteroids = new Vector.<Asteroid>();
			currentPlayerSpeed = 0;
		}
		
		override protected function start():void {
			var starsTextures:Vector.<Texture> = new Vector.<Texture>();
			for (var i:int = 0; i < 5; i++) {
				starsTextures.push(atlas.getTexture("star" + String(i + 1)));
			}
			
			background = new Background(stageWidth, stageHeight, starsTextures);
			addChild(background);
			
			playerShip = new Ship1(atlas.getTexture("ship_one_center"));
			setScale(playerShip);
			playerShip.y = stageHeight - playerShip.height - 20;
			playerShip.x = stageWidth >> 1;
			addChild(playerShip);
			//playerShip.scaleX = playerShip.scaleY = scale;
			
			controlManager = new ControlManager(playerShip);
			weaponsController = new WeaponsController();
			weaponsController.addEventListener(WeaponEvent.SHOOT, onShoot);
			controller.addEventListener(LevelControllerEvent.ADD_ASTEROID, onControllerEvent)
		}
		
		private function onControllerEvent(e:LevelControllerEvent):void {
			switch (e.type) {
				case LevelControllerEvent.ADD_ASTEROID:
					var asteroid:Asteroid = e.asteroid;
					asteroid.x = intRandom(0, stageWidth);
					asteroid.y = -asteroid.height>>1;
					addChild(asteroid);
					movables.push(asteroid);
					asteroids.push(asteroid);
				break;
			}
		}
		
		private function onShoot(e:WeaponEvent):void {
			switch (e.weaponType) {
				case WeaponType.GUN:
					if (!gunTexture) gunTexture = atlas.getTexture("weapon_minigun");
					var bullet:GunBullet = new GunBullet(gunTexture);
					bullet.x = playerShip.x;
					bullet.y = playerShip.y;
					addChild(bullet);
					movables.push(bullet);
					bullets.push(bullet);
				break;
			}
		}
		
		private function onPlayerMove(e:ControlManagerEvent):void {
			currentPlayerSpeed = e.playerMove;
		}
		
		public function play():void {
			controlManager.addEventListener(ControlManagerEvent.MOVE_PLAYER, onPlayerMove);
			addEventListener(Event.ENTER_FRAME, onUpdate);
			weaponsController.play();
			controller.play();
		}
		
		public function pause():void {
			controlManager.removeEventListener(ControlManagerEvent.MOVE_PLAYER, onPlayerMove);
			removeEventListener(Event.ENTER_FRAME, onUpdate);
			weaponsController.pause();
			controller.pause();
		}
		
		private function onUpdate(e:Event):void {
			background.move();
			if (currentPlayerSpeed != 0) {
				var playerMoveTo:int = playerShip.x + currentPlayerSpeed;
				if (playerMoveTo < 0) playerMoveTo = 0;
				if (playerMoveTo > stageWidth) playerMoveTo = stageWidth;
				if (playerShip.x != playerMoveTo) playerShip.x = playerMoveTo;
			}
			
			// move asteroids and bullets
			if (movables.length) {
				for (var i:int = 0; i < movables.length; i++) {
					if(movables[i]!= null){
						var movable:MovableObject = movables[i];
						movable.move();
						
						// check bullets stage-off
						if (movable.type == MovableType.BULLET && movable.y <= 0) {
							var bulletIndex:int = bullets.indexOf(movable as BulletBase);
							bullets[bulletIndex] = null;
							removeChild(movable);
							movables[i].dispose();
							movables[i] = null;
						}
						
						// check asteroids stage-off
						if (movable.type == MovableType.ASTEROID && movable.y >= stageHeight + movable.bounds.height) {
							var asteroidIndex:int = asteroids.indexOf(movable as Asteroid);
							asteroids[asteroidIndex] = null;
							removeChild(movable);
							movables[i].dispose();
							movables[i] = null;
						}
					}
				}
			}
			
			// check collisions
			for (var j:int = 0; j < bullets.length; j++) {
				var bullet:BulletBase = bullets[j];
				if(bullet != null){
					for (var k:int = 0; k < asteroids.length; k++) {
						var asteroid:Asteroid = asteroids[k];
						if (asteroid != null) {
							if (bullet.bounds.intersects(asteroid.bounds)) {
								asteroid.hit(bullet.damage);
								movables[movables.indexOf(bullet)] = null;
								removeChild(bullet);
								bullets[j] = null;
								bullet.dispose();
							}
						}
					}
				}
			}
			
			// remove null`s from lists
			framesCounter++;
			if (framesCounter == FRAMES_BEFORE_CLEAN) {
				framesCounter = 0;
				
				for (var l:int = movables.length - 1; l >=0 ; l--) {
					if (movables[l] == null) movables.splice(l, 1);
				}
				
				for (var m:int = bullets.length-1; m >=0 ; m--) {
					if (bullets[m] == null) bullets.splice(m, 1);
				}
				
				for (var n:int = asteroids.length-1; n >=0 ; n--) {
					if (asteroids[n] == null) asteroids.splice(n, 1);
				}
			}
			
		}
		
		[Inline]
		private final function setScale(obj:DisplayObjectContainer):void {
			//if (scale != 1) obj.scaleX = obj.scaleY = scale;
		}
		
		override public function dispose():void {
			removeEventListener(Event.ENTER_FRAME, onUpdate);
			weaponsController.removeEventListener(WeaponEvent.SHOOT, onShoot);
			controlManager.removeEventListener(ControlManagerEvent.MOVE_PLAYER, onPlayerMove);
			controlManager.dispose()
			background.dispose();
			controller.dispose();
			super.dispose();
		}
	}
}