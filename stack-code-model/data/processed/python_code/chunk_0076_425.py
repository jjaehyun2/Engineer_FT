package dom.tidesdk.media
{
	/**
	 * <p>A module for dealing with media.</p>
	 */
	public class TMedia
	{
		//
		// METHODS
		//

		/**
		 * <p>Activate the system bell. Some systems may have
		 * disabled the system bell.</p>
		 */
		public function beep():void {}

		/**
		 * <p>Factory method for Sound objects, created given
		 * a path or a URL to a sound file. The types of
		 * sound files that can be played depend on the
		 * codecs installed on the user's system.</p>
		 * 
		 * @param path  The path or url to the sound file to play. 
		 * 
		 * @return Ti.Media.Sound   
		 */
		public function createSound(path:String):TSound { return null; }

		public function TMedia() {}
	}
}