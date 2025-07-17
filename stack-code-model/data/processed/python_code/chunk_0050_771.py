package transform {
	
	import flash.filesystem.File;
	import flash.filesystem.FileStream;
	import flash.filesystem.FileMode;
	
	public class StringToFile {

		public function StringToFile() {
			// constructor code
		}
		
		public static function make(data:String, path:File):File {
			var writer:FileStream = new FileStream();
			writer.open(path, FileMode.WRITE);
			writer.writeUTFBytes(data);
			writer.close();
			return path;
		}

	}
	
}