package {
	import flash.desktop.NativeApplication;
	import flash.events.KeyboardEvent;
	import flash.ui.Keyboard;

	public class backkeyfunction {

		public function backkeyfunction() {
			// constructor code
			NativeApplication.nativeApplication.addEventListener(KeyboardEvent.KEY_DOWN, hdbtpressed);
		}

		function hdbtpressed(e: KeyboardEvent): void {
			if (e.keyCode == Keyboard.BACK) {
				NativeApplication.nativeApplication.exit();
				trace("back pressed");
			}

		}

	}
}