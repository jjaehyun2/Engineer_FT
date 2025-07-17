package  
{
	import net.flashpunk.graphics.Backdrop;
	
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class Background extends Backdrop 
	{
		[Embed(source = "Assets/Graphics/Backgrounds/bg_noise_0.png")]private const BG_1:Class;
		[Embed(source="Assets/Graphics/Backgrounds/bg_noise_1.png")]private const BG_2:Class;
		public function Background() 
		{
			super(BG_1, true, true);
			color = 0xCCCCFF;
			
			scrollX = 0.2;
			scrollY = 0.2;
		}
		
	}

}