package
{
	import net.flashpunk.Entity;
	
	public class Exit extends Entity
	{
		public function Exit(generator:MazeGenerator)
		{
			type = "exit";
			mask = generator.getExit();
		}
	}
}