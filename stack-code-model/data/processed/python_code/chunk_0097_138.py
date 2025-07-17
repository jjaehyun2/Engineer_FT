package
{
	import net.flashpunk.Engine;
	import net.flashpunk.FP;

	public class Main extends Engine
	{
		public function Main()
		{
			super(640, 640);
		}

		override public function init():void
		{
			
			FP.world = new GameWorld;
		}
	
	}
}