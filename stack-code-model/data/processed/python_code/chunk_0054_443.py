package org.rapo.games.astro.clips {
	
	import flash.display.MovieClip;

	public class mcDebris extends mcBase {
		
		public var anim:mcDebrisAnim;
		public var hit_target:mcHitTarget;
		
		public function mcDebris()
		{
			hit_target.visible = false;
		}
		
		public function explodeDone():void
		{
			
		}
	}
}