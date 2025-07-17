package Base {
	
	import flash.display.MovieClip;
	import flash.display.Stage;
	
	
	public class Base extends MovieClip {
		
		
		public function Base() {
			var mc:MovieClip = new MovieClip();
			mc.graphics.beginFill(0xff0000, 1);
			mc.graphics.drawRect(0, 0, 100, 100);
			mc.graphics.endFill();
			// constructor code
			
			///mc.graphics.beginGradientFill();
			//Stage.w
		}
	}
	
}