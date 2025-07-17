package  {
	
	import flash.display.Sprite;
	import flash.display.Stage;
	import flash.geom.Point;
	
	public class Main extends Sprite {

		public function Main(stage:Stage) {
			// constructor code
			ShiftAndPut.doThis(new Ball(0xFF0000), new Point(200, 100), stage);
		}

	}
	
}