/*
** Source code Copyright 2006, Andrew Rapo
** May be used in non-commercial and commercial applications
** as long as the author is credited
*/

package org.rapo.games.astro {
	
	import flash.display.MovieClip;
	
	import org.rapo.games.astro.BaseObject;
	import org.rapo.games.astro.MathTables;
	import org.rapo.games.astro.VectorMath;
	import org.rapo.games.astro.managers.FrameTimeManager;
	import org.rapo.games.astro.managers.BGManager;
	
	public class Debris extends BaseObject {
	
		public var size:Number;
	
		public function Debris(x:Number, y:Number, debris_size:Number,
								debris_speed:Number, angle_index:Number,
								movie_clip:MovieClip, name:String) {
	
			super(x, y, movie_clip, name);
			setAngleIndex(angle_index);
			speed = debris_speed;
			setSize(debris_size);
			mc.owner = this;
		}
	
		public override function move():void {
	
			MathTables.setVelocity(angleIndex, speed, velocity);
			VectorMath.scaleVector(velocity, FrameTimeManager.getFrameSeconds());
			VectorMath.addVectors(coords, velocity);
			mc.x = coords.x + BGManager.mc.x;
			mc.y = coords.y + BGManager.mc.y;
			
			if (!VectorMath.inBounds(coords, BGManager.worldBounds)) {
				alive = false;
			}
		}
		
		public function setSize(size:Number):void {
			this.size = size;
			mc.width = size;
			mc.height = size * (53/60); // aspect ratio of the Debris symbol
		}
		
		public function die():void
		{
			
		}
	}
}