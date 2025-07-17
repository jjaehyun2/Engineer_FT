/*
** Source code Copyright 2006, Andrew Rapo
** May be used in non-commercial and commercial applications
** as long as the author is credited
*/

package org.rapo.games.astro {
	
	import flash.display.MovieClip;
	
	import org.rapo.games.astro.MathTables;
	import org.rapo.games.astro.GameTimer;
	import org.rapo.games.astro.BaseObject;
	import org.rapo.games.astro.Bullet;
	import org.rapo.games.astro.AudioController;
	import org.rapo.games.astro.VectorMath;
	import org.rapo.games.astro.managers.FrameTimeManager;
	import org.rapo.games.astro.managers.ObjectManager;
	import org.rapo.games.astro.managers.BGManager;
	
	import org.rapo.games.astro.clips.mcShip;
	
	import org.rapo.games.astro.sounds.sndShoot;
	import org.rapo.games.astro.sounds.sndThrust;
	
	public class Ship extends BaseObject {
		
		public var over:Boolean;
		public var anim:String;
		public var animPrev:String;
		public var shooting:Boolean = false;
		public var hit:Boolean = false;
		public var animDone:Boolean = true;
		
		public var shieldOn:Boolean = false;
		public var thrustOn:Boolean = false;
		public var shieldPlaying:Boolean = false;
		public var thrustPlaying:Boolean = false;
		
		public var multiShot:Boolean = false;
		public var tailGun:Boolean = false;
		public var readyTimer:GameTimer;
		
		public var shipAudio:AudioController;
		public var soundShoot:sndShoot;
		public var soundThrust:sndThrust;
		
		public var screenCoords:Object;
		
		public function Ship(x:Number, y:Number, movie_clip:mcShip, name:String) {
			super(x, y, movie_clip, name);
			
			//mc.visible = false;
			mc.gotoAndStop(1);
			mc.ship_anim.owner = this;
			
			screenCoords = VectorMath.newVector(BGManager.SCREEN_ORIGIN.x, BGManager.SCREEN_ORIGIN.y);		
			mc.x = screenCoords.x;
			mc.y = screenCoords.y;
			reset();
			
			shipAudio = new AudioController();
			soundShoot = new sndShoot();
			soundThrust = new sndThrust();
			shipAudio.registerSound("thrust", soundThrust);
			shipAudio.registerSound("shoot", soundShoot);
			velocity = {x:0, y:-10};
		}
		
		public function setShielded(state:Boolean):void {
			shieldOn = state;
			readyTimer = undefined;
		}
	
		public override function move():void {
			
			friction();
			updateCoords();
			mc.visible = true;
			setAnimation();
			mc.x = screenCoords.x;
			mc.y = screenCoords.y;
			
			if (readyTimer != undefined && readyTimer.milliseconds() > 3000) {
				setShielded(false);
				readyTimer = undefined;
			}
		}
		
		public function friction():void {
			
			var frictionVector:Object = {x:0, y:0};
			var frictionCoefficient:Number = -.05;
			VectorMath.copyVector(frictionVector, velocity);
			VectorMath.scaleVector(frictionVector, frictionCoefficient);
			VectorMath.addVectors(velocity, frictionVector);
		}
			
		public function updateCoords():void {

			VectorMath.addVectors(coords, velocity);
			VectorMath.inBounds(coords, BGManager.shipBounds);
			
			VectorMath.addVectors(screenCoords, velocity);
			VectorMath.inBounds(screenCoords, BGManager.shipScreenBounds);
		}
		
		public function setAnimation():void {
	
			if (animDone){
				
				//set animation state
				if (over) {
					anim = "over";
					animDone = false;
					shieldOn = false;
					thrustOn = false;
				} else if (hit) {
					anim = "hit";
					animDone = false;
				} else if (shooting) {
					anim = "shoot";
					animDone = false;
				} else {
					anim = "idle";
				}
		
				//set thrust visibility
				if (thrustOn) {
					mc.ship_thrust.visible = true;
					if (!thrustPlaying) {
						mc.ship_thrust.gotoAndPlay("on");
						shipAudio.playSound("thrust", true);
						thrustPlaying = true;
					}
				} else {
					mc.ship_thrust.visible = false;
					shipAudio.stopSoundNow("thrust");
					thrustPlaying = false;
				}
		
				//set shield visibility
				if (shieldOn) {
					if (!shieldPlaying) {
						mc.ship_shield.visible = true;
						mc.ship_shield.gotoAndPlay("on");
						shieldPlaying = true;
					}
				} else {
					mc.ship_shield.visible = false;
					shieldPlaying = false;
				}
		
				if (anim != animPrev) {
		
					mc.ship_anim.gotoAndPlay(anim);
					animPrev = anim;
				}
			}
		}
		
		public function doneShooting():void {
	
			animDone = true;
			shooting = false;
			hit = false;
			anim = "idle";
			animPrev = "";
		}
		
		public function reset():void {
			over = false;
			anim = "idle";
			animPrev = "";
			shooting = false;
			hit = false;
			animDone = true;
			alive = true;
			shieldOn = true;
			thrustOn = false;
			shieldPlaying = false;
			thrustPlaying = false;
			mc.visible = false;
			mc.ship_shield.visible = false;
			mc.ship_thrust.visible = false;
			coords.x = 0;
			coords.y = 0;
			angleIndex = 0;
			rotate("right");
			multiShot = false;
			tailGun = false;
			readyTimer = new GameTimer();
		}
		
		public function thrust(direction:Number):void {
	
			var acceleration:Object = {x:0, y:0};
			var accelerationScalar = 50 * direction;
			accelerationScalar *= FrameTimeManager.getFrameSeconds();
			MathTables.setVelocity(angleIndex, accelerationScalar, acceleration)
			VectorMath.addVectors(velocity, acceleration);
			thrustOn = true;
		}
	
		public function thrustOff():void  {
			thrustOn = false
		}
		
		public function rotate(direction:String):void  {
			
			if (direction == "right") {
				if (angleIndex == 32) {
					angleIndex = 1;	
				} else {
					angleIndex += 1;
				}
			} else if (direction == "left") {
				if (angleIndex == 1) {
					angleIndex = 32;
				} else {
					angleIndex -= 1;
				}
			}
			mc.gotoAndStop(angleIndex);
		}
		
		public function shoot():void  {
			
			var tempBullet:Bullet
			
			if (alive && !shooting) {
				shipAudio.playSound("shoot", false);
				shooting = true;
				tempBullet = ObjectManager.createBullet(coords.x, coords.y, 600, angleIndex);
				ObjectManager.addObject(tempBullet, "bullets");
				if (multiShot) {
					tempBullet = ObjectManager.createBullet(coords.x, coords.y, 400, angleIndex - 1);
					ObjectManager.addObject(tempBullet, "bullets");
					tempBullet = ObjectManager.createBullet(coords.x, coords.y, 400, angleIndex + 1);
					ObjectManager.addObject(tempBullet, "bullets");
				} else if (tailGun) {
					var tempAngleIndex:Number = angleIndex - 16;
					if (tempAngleIndex <= 0) tempAngleIndex += MathTables.angleDivisions;
					tempBullet = ObjectManager.createBullet(coords.x, coords.y, 400, tempAngleIndex);
					ObjectManager.addObject(tempBullet, "bullets");
				}
			}
		}
		
		public function bounce(object:BaseObject):void
		{
			//reflect in direction of object
			hit = true;
			VectorMath.copyVector(velocity, object.velocity);
		}
		
		public function die():void  {
			alive = false;
		}
	}
}