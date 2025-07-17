package {
	import net.flashpunk.Engine;
	import net.flashpunk.FP;
	import worlds.World1;
	
	public class Main extends Engine {
		public function Main() {
			super(800, 640, 100, false);
		}
		
		override public function init():void {
			FP.screen.color = 0xffffff;
			FP.world = new World1;

		}
	}
}