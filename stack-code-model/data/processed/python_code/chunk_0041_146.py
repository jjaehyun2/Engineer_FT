package {
	
	/**
	 * ...
	 * @author Michael M
	 */
	public class ExampleBody extends Body {
		
		private var spd:Number;
		
		public function ExampleBody() {
			super();
			spd = 1 + Math.random() * 9;
			drawDebug();
			
			x = 482
			y = 77;
			alpha = 0.05;
		}
		
		public function myCustomJumpFunction():void {
			velocity.y -= 25;
		}
		
		public function myCustomMoveFunction():void {
			velocity.x += stage.mouseX < x ? -spd : spd;
		}
	}

}