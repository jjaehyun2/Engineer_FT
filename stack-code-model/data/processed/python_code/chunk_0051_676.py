package Entities 
{
	import org.flixel.*;
	
	/**
	 * Single cloud particle
	 * 
	 * @author Artem Gurevich / RadicalEd
	 */
	public class Cloud extends FlxParticle {
		public function Cloud() {
			loadGraphic(Assets.CLOUDS, true, false, 64, 32);
		}
		
		override public function onEmit():void  {
			randomFrame();
		}
		
		override public function update():void  {
			if (x < -width)
				kill();
			
			super.update();
		}
	}
}