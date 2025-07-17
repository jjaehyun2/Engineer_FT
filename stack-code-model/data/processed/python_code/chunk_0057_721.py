package vyperlogix.FileIO.serializer {
	import flash.events.Event;
	import flash.events.IOErrorEvent;
	import flash.filesystem.File;
	import flash.filesystem.FileMode;
	import flash.filesystem.FileStream;
	
	/**
	 *
	 * All static class which provides a mechanism for both synchronous
	 * and asynchronous File creation on a local File system
	 *
	 */
	public final class FileWriter {
		/**
		 *
		 * Synchronously creates a new File to the local filesystem
		 * and returns an open FileStream object. If the File exists
		 * then the file is opened for update
		 *
		 * @param  the name of the file to create
		 * @param  the path in which to create the file
		 * @return an open FileStream intance referencing the File
		 * @throws flash.errors.IOError
		 *
		 */
		public static function createSync(path:String, name:String, append:Boolean=false) : FileStream {
			var file:File = new File();
			file.nativePath = path + ((name is String) ? File.separator + name : '') ;
			
			var stream:FileStream = new FileStream();
			
			if ( (!append) && (!file.exists) ) {
				stream.open(file, FileMode.WRITE);
			} else {
				stream.open(file, FileMode.APPEND);
			}
			return stream;
		}
		
		/**
		 *
		 * Asynchronously creates a new File to the local filesystem
		 * and returns an open FileStream object. If the File exists
		 * then the file is opened for update
		 *
		 * @param  the name of the file to create
		 * @param  the path in which to create the file
		 * @param  method in which to invoke upon file complete
		 * @param  method in which to invoke upon file IOError
		 * @return an open FileStream intance referencing the File
		 * @throws flash.errors.IOError
		 *
		 */
		public static function createAsync(path:String, name:String, complete:Function, exception:Function) : FileStream {
			var file:File = new File();
			file.nativePath = path + ((name is String) ? File.separator + name : '') ;
			
			var stream:FileStream = new FileStream();
			stream.addEventListener(Event.COMPLETE, complete);
			stream.addEventListener(IOErrorEvent.IO_ERROR, exception);
			
			if (!file.exists) {
				stream.open(file, FileMode.WRITE);
			} else {
				stream.open(file, FileMode.UPDATE);
			}
			return stream
		}
		
		/**
		 *
		 * Determines if the current file exists
		 *
		 * @param  the name of the file
		 * @param  the path in which the file resides
		 * @return if the file being references currently exists
		 *
		 */
		public static function exists(path:String, name:String) : Boolean {
			var file:File = new File();
			file.nativePath = path + ((name is String) ? File.separator + name : '') ;
			
			return file.exists;
		}
	}
}