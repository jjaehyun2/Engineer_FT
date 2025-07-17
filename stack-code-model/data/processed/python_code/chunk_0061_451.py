﻿package dagd.myles {

	import flash.display.MovieClip;
	import flash.events.MouseEvent;

	public class BlueStar extends MovieClip {

		public var isDead: Boolean = false;
		
		public var points:Number = 0;
		
		public var health:Number = 0;

		public function BlueStar() {
			// constructor code
			x = 0;
			y = Math.random() * 500;

			addEventListener(MouseEvent.MOUSE_DOWN, handleClick);
		}
		//this function's job is to perform any cleanup 
		//before an object is removed from the games.
		public function dispose(): void {
			removeEventListener(MouseEvent.MOUSE_DOWN, handleClick);
		}
		// this function should run every game tick.
		// it dictates the behavior of an object.
		public function update(): void {
			
			x += 5; // move to the right 1 pixel
			
			if (x > 800) { // checks if off right side of screen
				isDead = true;
				

			}
			


		} // ends update()

		private function handleClick(e: MouseEvent): void {
			isDead = true;
			points = 10;
			health = 1;
		}

	} // ends BlueStar class

} // ends package