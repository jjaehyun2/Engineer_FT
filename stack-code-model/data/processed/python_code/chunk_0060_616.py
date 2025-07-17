package zombie
{
	import flash.display.Sprite;
	import flash.events.Event;
	import net.flashpunk.Engine;
	import net.flashpunk.FP;
	import fplib.maping.OgmoMap;
	import zombie.entities.GameManager;
	import zombie.worlds.TitleScreen;
	
	/**
	 * ...
	 * @author Diogo Muller
	 */
	public class Main extends Engine 
	{
		
		public function Main():void 
		{
			super(800, 600, 60, false);
			
			FP.world = new TitleScreen();
		}
		
		override public function init():void
		{
			trace("FlashPunk has started successfully!");
		}
	}
	
}