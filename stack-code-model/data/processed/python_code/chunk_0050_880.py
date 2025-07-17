package

{

	import org.flixel.*;

	[SWF(width="640", height="480", backgroundColor="#000000")]

	[Frame(factoryClass="Preloader")]

	public class FreewayArcade extends FlxGame {

		public function FreewayArcade() {
			Tile.initCache();
			super(640, 480, PlayState, 1, 60, 60, true );
			//forceDebugger = false;
			
		}
		
		

	}

}