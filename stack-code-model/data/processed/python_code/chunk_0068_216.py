package aerys.minko.example.effects.blur
{
	import aerys.minko.example.core.primitives.PrimitivesExample;
	import aerys.minko.render.effect.blur.BlurEffect;
	import aerys.minko.render.effect.blur.BlurQuality;
	
	public class BlurExample extends PrimitivesExample
	{
		override protected function initializeScene() : void
		{
			super.initializeScene();
			
			scene.postProcessingEffect = new BlurEffect(BlurQuality.NORMAL, 4);
		}
	}
}