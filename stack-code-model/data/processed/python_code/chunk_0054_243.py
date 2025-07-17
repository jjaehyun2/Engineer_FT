/**
 *
 * Blackhole/Repulsor
 *
 * https://github.com/AbsolutRenal
 *
 * Copyright (c) 2012 AbsolutRenal (Renaud Cousin). All rights reserved.
 * 
 * This ActionScript source code is free.
 * You can redistribute and/or modify it in accordance with the
 * terms of the accompanying Simplified BSD License Agreement.
**/

package com.game.data.manager {
	import com.game.constant.GameInit;
	import BO.BulletBO;
	import flash.display.DisplayObject;
	import BO.BaseBO;
	import BO.GameBO;
	import BO.MapBO;
	import BO.PlayerBulletsBO;

	import com.game.view.Bullet;

	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.EventDispatcher;
	import flash.geom.Point;
	/**
	 * @author renaud.cousin
	 */
	public class BulletManager extends Sprite{
		private static var _instance:BulletManager;
		
		private var bulletContainer:Sprite;
		private var bulletsByPlayer:Vector.<PlayerBulletsBO>;
		private var isFiring:Boolean;
		
		
		public function BulletManager(singleton:SingletonEnforcer){
			if(singleton ==  null){
				throw new Error("WallManager should be created using WallManager.getInstance() method");
			} else {
				init();
			}
		}
		
		
		//----------------------------------------------------------------------
		// E V E N T S
		//----------------------------------------------------------------------

		private function onFire(event:Event):void {
			if(isFiring){
				for each (var playerBullets:PlayerBulletsBO in bulletsByPlayer) {
					for each (var bullet:Bullet in playerBullets.bullets) {
						moveBullet(bullet);
					}
					
					playerBullets.fireTick ++;
					if(playerBullets.fireTick == playerBullets.base.firingRate){
						playerBullets.fireTick = 0;
						fireBullet(playerBullets);
					}
				}
			}
		}
		
		
		//----------------------------------------------------------------------
		// P R I V A T E
		//----------------------------------------------------------------------

		private function init():void {
			bulletContainer = GameBO.getInstance().map.bulletContainer;
			
			var bases:Vector.<BaseBO> = MapBO.getInstance().mapElements.bases;
			bulletsByPlayer = new Vector.<PlayerBulletsBO>();
			var playerBulletsBo:PlayerBulletsBO;
			
			for each (var base:BaseBO in bases) {
				playerBulletsBo = new PlayerBulletsBO();
				playerBulletsBo.base = base;
				playerBulletsBo.bullets = new Vector.<Bullet>();
				
				bulletsByPlayer.push(playerBulletsBo);
			}
		}
		
		private function fireBullet(playerBullets:PlayerBulletsBO):void{
			// TODO
			if(playerBullets.base.globalPosition == null){
				var p:Point = playerBullets.base.parentHexagon.hexagonBO.position;
				playerBullets.base.globalPosition = playerBullets.base.animationSprite.localToGlobal(new Point());
			}
			
			var bullet:Bullet = new Bullet();
			var bulletBo:BulletBO = new BulletBO();
			bulletBo.remainingDuration = GameInit.BULLET_DURATION;
//			bulletBo.
			
			bullet.bulletBo = bulletBo;
			bulletContainer.addChild(bullet);
			
			playerBullets.bullets.push(bullet);
		}
		
		private function moveBullet(bullet:Bullet):void{
//			checkWallCollision(bullet);
//			checkBonusCollision(bullet);
// 			checkBaseCollision(bullet);
			
			// TODO
			
		}
		
		
		//----------------------------------------------------------------------
		// P U B L I C
		//----------------------------------------------------------------------
		
		public static function getInstance():BulletManager{
			if(_instance == null){
				_instance = new BulletManager(new SingletonEnforcer());
			}
			return _instance;
		}
		
		public function startFiring():void{
			isFiring = true;
			addEventListener(Event.ENTER_FRAME, onFire);
		}
		
		public function stopFiring():void{
			isFiring = false;
			removeEventListener(Event.ENTER_FRAME, onFire);
		}
	}
}


internal class SingletonEnforcer{
	public function SingletonEnforcer(){}
}