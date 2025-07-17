package utils {
	import vyperlogix.utils.CapabilitiesUtils;
	
	import flash.filesystem.File;
	
	import mx.core.FlexGlobals;
	
	import vyperlogix.utils.StringUtils;

	public class AIRHelper {
		private static var prefixes:Object = {};

		public static var default_prefix:String = 'app:/';
		
		private static var _installable_software_fpaths:Array = [];
		
		private static var __cache__:Object = {};
		
		public static function set_prefix(key:String,value:*):void {
			AIRHelper.prefixes[key] = value;
		}

		private static function get get_prefix():File {
			var prefix:* = AIRHelper.prefixes[AIRHelper.default_prefix];
			return (prefix is File) ? prefix : new File();
		}

		public static function resolve(fpath:String):File {
			function cache_directory_contents(dir:File):Object {
				var ar:Array;
				var files:Object = AIRHelper.__cache__[dir.nativePath];
				var hash:Object = (files) ? files : {};
				if (!files) {
					ar = dir.getDirectoryListing();
					for (var i:String in ar) {
						hash[String(ar[i].name).toLowerCase()] = ar[i];
					}
					AIRHelper.__cache__[dir.nativePath] = hash;
				}
				return hash;
			}
			var aFile:File = AIRHelper.get_prefix.resolvePath(StringUtils.appendSlashIfNecessary(AIRHelper.get_prefix.parent.nativePath)+'data/'+fpath);
			trace('AIRHelper.resolve().1 --> aFile='+aFile.nativePath);
			var isAdjusting:Boolean;
			isAdjusting = (FlexGlobals.topLevelApplication.is_debugging) ? (CapabilitiesUtils.isOSWindows()) : (CapabilitiesUtils.isOSMac() || CapabilitiesUtils.isOSLinux());
			if (isAdjusting) {
				if (!aFile.isDirectory) {
					var sep:String = File.separator;
					var ar:Array = aFile.nativePath.split(sep);
					var n:String = ar.slice(0,ar.length-1).join(sep);
					var aDir:File;
					var fp:String;
					var _is_:Boolean;
					var hash:Object;
					var f:File;
					for (var k:int = (CapabilitiesUtils.isOSWindows()) ? 1 : 3; k < ar.length; k++) {
						fp = ar.slice(0,k).join(sep);
						aDir = new File(fp);
//						_is_ = ((isAdjusting) && (k > 1)) ? false : ( (aDir.exists) && (aDir.isDirectory) );
						_is_ = ( (aDir.exists) && (aDir.isDirectory) );
						if (_is_) {
							hash = cache_directory_contents(aDir);
							f = hash[ar[k]];
							if (f is File) {
								ar[k] = f.name;
							}
						} else {
							f = hash[ar[k]];
							if (f is File) {
								ar[k] = f.name;
							}
						}
					}
					var n2:String = ar.join(sep);
					aFile = new File(n2);
				}
			}
			trace('AIRHelper.resolve().2 --> aFile='+aFile.nativePath);
			return aFile;
		}
	}
}