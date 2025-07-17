package nativeclasses {
	public class NativePlayer {
		public function NativePlayer() {
		}

		[ElipsPlatformExtension(platforms="iPhone OS 3.0,Android 1.6")]
		public function music_playback():Boolean {
			trace ("Play Music from Native Library");
			return false;
		}
	}
}