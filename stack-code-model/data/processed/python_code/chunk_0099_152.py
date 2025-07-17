package ro.ciacob.desktop.filebrowser {
	import flash.events.Event;
	import flash.filesystem.File;

	public class FileSelectionEvent extends Event {
		public static const FILE_CANCELLED:String = 'fileCancelled';

		public static const FILE_SELECTED:String = 'fileSelected';

		public function FileSelectionEvent(type:String, file:File = null) {
			super(type, false, false);
			_file = file;
		}

		private var _file:File;

		override public function clone():Event {
			return new FileSelectionEvent(type, _file);
		}

		public function get file():File {
			return _file;
		}
	}
}