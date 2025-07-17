package ro.ciacob.desktop.io {
	import flash.errors.EOFError;
	import flash.errors.IOError;
	import flash.errors.IllegalOperationError;
	import flash.events.ErrorEvent;
	import flash.events.EventDispatcher;
	import flash.filesystem.File;
	import flash.filesystem.FileMode;
	import flash.filesystem.FileStream;
	import flash.utils.ByteArray;

	/**
	 * Reads files on disk into data structures.
	 */
	public class AbstractDiskReader extends EventDispatcher {


		public function AbstractDiskReader(self:AbstractDiskReader) {
			if (self == null) {
				throw(new IllegalOperationError('AbstractDiskReader is an abstract class. Please subclass it, invoking super (this) from your subclass\' constructor.'));
			}
		}

		private var _lastReadFile:File;

		/**
		 * @return
		 * 		The last file successfully read form disk.
		 */
		public function get lastReadFile():File {
			return lastReadFile;
		}

		public function readContent(fromFile:File):Object {
			var ret:Object;
			if (!fromFile.exists) {
				_lastReadFile = null;
				dispatchEvent(new ErrorEvent(ErrorEvent.ERROR, false, false, 'File "' + fromFile.nativePath + '" cannot be read. Please ensure the file exists and has proper permissions.'));
			} else {
				var s:FileStream = new FileStream();
				try {
					s.open(fromFile, FileMode.READ);

					var content:ByteArray = new ByteArray;
					var atEndOfFile:Boolean = false;
					while (!atEndOfFile) {
						try {
							content.writeByte(s.readByte());
						} catch (eof:EOFError) {
							atEndOfFile = true;
						}
					}
					_lastReadFile = fromFile;
					s.close();
					ret = deserializeSource(content);
				} catch (ioError:IOError) {
					dispatchEvent(new ErrorEvent(ErrorEvent.ERROR, false, false, 'Encountered an IOError while reading file ' +
						fromFile.nativePath + '.'));
				} catch (securityError:SecurityError) {
					dispatchEvent(new ErrorEvent(ErrorEvent.ERROR, false, false, 'Encountered a SecurityError while reading file ' +
						fromFile.nativePath +
						'.'));
				}
			}
			return ret;
		}

		/**
		 * Subclasses must override this.
		 * @param source
		 * 		A string holding the content of the file, as read from disk.
		 * @return
		 * 		A data structure, obtained by parsing the provided content.
		 * @throws (newIllegalOperationError(ABSTRACT_METHOD_ERROR.replace('%s','deserializeSource')))
		 */
		protected function deserializeSource(source:ByteArray):Object {
			throw(new IllegalOperationError('Method "deserializeSource" of class AbstractDiskReader is abstract. Please override it in your subclass.'));
			return null;
		}
	}
}