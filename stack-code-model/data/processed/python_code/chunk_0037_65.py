package ro.ciacob.desktop.io {
	import flash.errors.IllegalOperationError;
	import flash.events.ErrorEvent;
	import flash.events.Event;
	import flash.events.EventDispatcher;
	import flash.events.OutputProgressEvent;
	import flash.filesystem.File;
	import flash.filesystem.FileMode;
	import flash.filesystem.FileStream;
	import flash.utils.ByteArray;

	public class AbstractDiskWritter extends EventDispatcher {

		private static const ABSTRACT_CLASS_ERROR:String = 'AbstractDiskWritter is an abstract class. Please subclass it, invoking super (this) from your subclass\' constructor.';
		private static const ABSTRACT_METHOD_ERROR:String = 'Method %s of class AbstractDiskWritter is abstract. Please override it in your subclass.';

		public function AbstractDiskWritter(self:AbstractDiskWritter) {
			if (self == null) {
				throw(new IllegalOperationError(ABSTRACT_CLASS_ERROR));
			}
		}

		private var _stream:FileStream;

		public function write(source:Object, destination:File, append:Boolean = false):int {
			var error:Error;
			var content:ByteArray = serializeSource(source);
			_stream = new FileStream;
			try {
				// We merely dispatch this event for legacy reasons. Shall be properly addressed in a bright future...
				dispatchEvent(new OutputProgressEvent(OutputProgressEvent.OUTPUT_PROGRESS,
					false, false, 0, 0));
				var mode:String = (append ? FileMode.APPEND : FileMode.WRITE);
				if (!destination.exists) {
					mode = FileMode.WRITE;
				}
				_stream.open(destination, mode);
				_stream.writeBytes(content);
				_stream.close();
			} catch (writeError:Error) {
				error = writeError;
			} finally {
				_stream.close();
			}
			if (error != null) {
				var message:String = error.message + ' File: ' + destination.nativePath;
				dispatchEvent(new ErrorEvent(ErrorEvent.ERROR, false, false, message,
					error.errorID));
				return -1;
			}
			dispatchEvent(new DiskWritterEvent(DiskWritterEvent.WRITE_COMPLETED,
				destination));
			return destination.size;
		}

		protected function serializeSource(source:Object):ByteArray {
			throw(new IllegalOperationError(ABSTRACT_METHOD_ERROR.replace('%s', 'serializeSource')));
			return null;
		}

	}
}