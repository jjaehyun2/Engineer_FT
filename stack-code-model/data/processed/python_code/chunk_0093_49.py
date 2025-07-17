package application.utils {
	
	import flash.filesystem.File;
	import flash.filesystem.FileMode;
	import flash.filesystem.FileStream;

	public class UserPrefs extends Object {
		
		public static function _read():Object {
			var f:File = File.applicationStorageDirectory.resolvePath("prefs.conf");
			var fs:FileStream = new FileStream();
			fs.open(f, FileMode.READ);
			var obj2:Object = fs.readObject();
			fs.close();
			
			fs = null;
			f = null;
			return obj2;
		}
		
		public static function _write():void {
			
			var obj:Object = {lang:Settings._lang, user:Settings._userID}; 
			
			var f:File = File.applicationStorageDirectory.resolvePath("prefs.conf");
			var fs:FileStream = new FileStream();
			fs.open(f, FileMode.WRITE);
			fs.writeObject(obj);
			fs.close();
			fs = null;
			f = null;
		}
		
	}

}