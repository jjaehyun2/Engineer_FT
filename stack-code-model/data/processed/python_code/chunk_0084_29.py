/*
** Source code Copyright 2006, Andrew Rapo
** May be used in non-commercial and commercial applications
** as long as the author is credited
*/

package org.rapo.games.astro {
	
	import flash.display.MovieClip;
	
	import org.rapo.games.astro.GameTimer;
	import org.rapo.games.astro.BaseObject;
	import org.rapo.games.astro.VectorMath;
	import org.rapo.games.astro.managers.ObjectManager;
	import org.rapo.games.astro.managers.PowerupManager;
	import org.rapo.games.astro.managers.FrameTimeManager;
	import org.rapo.games.astro.managers.AIManager;
	import org.rapo.games.astro.managers.BGManager;
	
	public class Powerup extends BaseObject {
	
		public var type:String;
		public var autoPilotTimer:GameTimer;
		public var durationTimer:GameTimer;

	
		public function Powerup (pu_type:String, x:Number, y:Number, movie_clip:MovieClip, name:String) {
	
			super(x, y, movie_clip, name);
			type = pu_type;
			
			autoPilotTimer = new GameTimer();
			durationTimer = new GameTimer();
		}
	
		public override function move():void {
			
			autoPilot();
			friction();
			updateCoords();
			mc.visible = true;
			mc.x = coords.x + BGManager.mc.x;
			mc.y = coords.y + BGManager.mc.y;
			if (durationTimer.milliseconds() > PowerupManager.POWERUP_DURATION) {
				alive = false;
			}
			//trace("powerup: " + mc.x + ", " + durationTimer.milliseconds());
		}
		
		public function friction():void {
			
			var frictionVector:Object = {x:0, y:0};
			var frictionCoefficient:Number = -.01;
			VectorMath.copyVector(frictionVector, velocity);
			VectorMath.scaleVector(frictionVector, frictionCoefficient);
			VectorMath.addVectors(velocity, frictionVector);
		}
		
		public function updateCoords():void {
			
			var newLocation:Object = new Object();
			
			VectorMath.copyVector(newLocation, coords);
			VectorMath.addVectors(newLocation, velocity);
			//VectorMath.addVectors(newLocation, CurrentTables.getCurrent(coords));
			coords = newLocation;
		}
	
		public function autoPilot() {		
			if (autoPilotTimer.milliseconds() > AIManager.PU_AI_INTERVAL) {
				var acceleration:Object = {x:0, y:0};
				var accelerationScalar = 
					50 * AIManager.PU_AI_AGGRESSION * FrameTimeManager.getFrameSeconds();
				VectorMath.copyVector(acceleration, ObjectManager.ship.coords);
				VectorMath.subtractVectors(acceleration, coords);
				VectorMath.normalizeVector(acceleration);
				VectorMath.scaleVector(acceleration, accelerationScalar);
	
				VectorMath.addVectors(velocity, acceleration);
	
				autoPilotTimer.restartTimer();
			}
		}
		
		public function hit(object:BaseObject):void
		{
			
		}
		
		public function die():void
		{
			
		}
	}
}