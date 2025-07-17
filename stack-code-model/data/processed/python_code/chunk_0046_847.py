package utils {
	import com.CapabilitiesUtils;
	import com.StringUtils;
	
	import flash.filesystem.File;
	import flash.html.HTMLLoader;
	import flash.html.HTMLPDFCapability;
	import flash.net.URLRequest;
	import flash.net.navigateToURL;
	
	import mx.core.FlexGlobals;

	public class AIRHelper {
		private static var prefixes:Object = {};

		public static var default_prefix:String = 'app:/';

		public static var file_prefix:String = 'file://';
		
		public static var options:Object = {};
		
		private static var _installable_software_fpaths:Array = [];
		
		private static var __cache__:Object = {};
		
		public static function set_prefix(key:String,value:*):void {
			AIRHelper.prefixes[key] = value;
		}

		public static function navigate_to_url(url:String,target:String):void {
			var request:URLRequest = new URLRequest(url); 
			trace('AIRHelper.navigateToUrl.1 --> url='+url);
			navigateToURL(request,target); 				
		}
		
		public static function get_html_loader_capability():String {
			if (HTMLLoader.pdfCapability == HTMLPDFCapability.ERROR_CANNOT_LOAD_READER) {
				return 'ERROR_CANNOT_LOAD_READER';
			} else if (HTMLLoader.pdfCapability == HTMLPDFCapability.ERROR_INSTALLED_READER_NOT_FOUND) {
				return 'ERROR_INSTALLED_READER_NOT_FOUND';
			} else if (HTMLLoader.pdfCapability == HTMLPDFCapability.ERROR_INSTALLED_READER_TOO_OLD) {
				return 'ERROR_INSTALLED_READER_TOO_OLD';
			} else if (HTMLLoader.pdfCapability == HTMLPDFCapability.ERROR_PREFERRED_READER_TOO_OLD) {
				return 'ERROR_PREFERRED_READER_TOO_OLD';
			}
			return 'STATUS_OK';
		}
		
		private static function get get_prefix():File {
			var prefix:* = AIRHelper.prefixes[AIRHelper.default_prefix];
			return (prefix is File) ? prefix : new File();
		}
		
		public static function normalize_url(fpath:String):String {
			return (fpath is String) ? ((fpath.indexOf(AIRHelper.file_prefix) > -1) ? fpath : AIRHelper.file_prefix+fpath) : fpath;
		}
		
		public static function get_directory_from(aFileOrDirectory:File):File {
			if (aFileOrDirectory.isDirectory) {
				return aFileOrDirectory;
			}
			var aFileName:String = aFileOrDirectory.nativePath;
			var sep:String = File.separator;
			var ar:Array = aFileName.split(sep);
			var fpath:String = ar.slice(0,ar.length-1).join(sep);
			var aFile:File = File.desktopDirectory.resolvePath(fpath);
			return aFile;
		}
		
		public static function walk_folder_paths(aFileString:*,callback:Function):void {
			var aFileName:String = (aFileString is File) ? aFileString.nativePath : aFileString;
			var sep:String = File.separator;
			var ar:Array = aFileName.split(sep);
			var fp:String;
			var aDir:File;
			for (var i:int = (CapabilitiesUtils.isOSWindows()) ? 2 : 3; i < ar.length; i++) {
				if (callback is Function) {
					fp = ar.slice(1,i).join(sep);
					aDir = File.applicationStorageDirectory.resolvePath(fp);
					callback(aDir,i);
				}
			}
		} 

		public static function resolve(fpath:String,nocache:Boolean=false):File {
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