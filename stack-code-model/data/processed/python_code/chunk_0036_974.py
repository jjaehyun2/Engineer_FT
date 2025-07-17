package 
{
	import flash.__native.WebGLRenderer;
	/**
	 * ...
	 * @author lizhi
	 */
	public class TestHungryHeroGPU extends TestHungryHero
	{
		
		public function TestHungryHeroGPU() 
		{
			COMPILE::JS{
				SpriteFlexjs.renderer = new WebGLRenderer;
				SpriteFlexjs.wmode = "gpu batch";
			}
			
		}
		
	}

}