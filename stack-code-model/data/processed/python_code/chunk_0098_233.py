package code {

	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.events.MouseEvent;


	public class Triangle extends MovieClip {

		public var isDead: Boolean = false;

		public function Triangle() {
			x = Math.random() * 550;
			y = Math.random() * 400;

			addEventListener(MouseEvent.CLICK, handleClick);
		}

		public function dispose(): void {
			removeEventListener(MouseEvent.CLICK, handleClick);

		}

		public function update(): void {

			x += 20;

			if (x > 550) {
				isDead = true;
			}
		} // ends update()

		private function handleClick(e: MouseEvent): void {
			isDead = true;

		}

	} // ends Triangle class

} // ends package