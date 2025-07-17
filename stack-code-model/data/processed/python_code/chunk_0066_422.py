package vyperlogix.utils {
	import flash.filesystem.File;

	public class FileUtils {
		public static function exists(url:String):Boolean {
			var aFile:File = new File(url);
			return aFile.exists;
		}

		public static function makeFileSpecIntoFolderSpec(fileSpec:String):String {
			var toks:Array = fileSpec.split(File.separator);
			toks.pop();
			return toks.join(File.separator);
		}
		
		public static function correctFolderSpec(folderSpec:String):String {
			var file:File;
			try {
				file = new File(folderSpec);
				if (file.isDirectory == false) {
					return makeFileSpecIntoFolderSpec(folderSpec);
				}
			} 
			catch (err:Error) {
				return makeFileSpecIntoFolderSpec(folderSpec);
			}
			return folderSpec;
		}
	}
}