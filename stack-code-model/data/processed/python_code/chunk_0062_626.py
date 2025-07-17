package
{
	import net.flashpunk.Engine;
	import net.flashpunk.FP;
	
	import worlds.GameWorld;
	import worlds.MainMenuWorld;
	
	
	
	[SWF(width="960", height="720")]
	public class platform extends Engine
	{
		public function platform()
		{
			super(640, 480, 60);
		}
		
		public override function init():void
		{
			
			//FP.console.enable();
			trace("FlashPunk " + FP.VERSION + " started!");
			FP.screen.scale = 1.5;
			
			
			FP.world = new MainMenuWorld(1,0,0);
				
			
		//	FP.world = new GameWorld();
				
		}
		
		
		
		
	}
}