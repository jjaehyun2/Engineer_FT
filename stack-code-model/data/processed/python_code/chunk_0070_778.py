package 
{
	import flash.display.Sprite;
	import flash.events.Event;
	import net.flashpunk.Engine;
	import net.flashpunk.FP;
	
	/**
	 * ...
	 * @author Martin Copp
	 */
	public class Main extends Engine
	{
		
		public function Main():void 
		{
			super(640, 480); //create game 640 x 480
			FP.world = new Game; //load our world
			FP.console.enable(); //debug - console comment if you don't need it
		}
		
		
		override public function init():void
		{
			trace("cha");
		}
	}
	
}