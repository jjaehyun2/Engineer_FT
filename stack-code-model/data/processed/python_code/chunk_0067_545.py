package utils {
	import com.CapabilitiesUtils;
	import com.StringUtils;
	
	import core.SWFHelper;
	
	import flash.desktop.NativeApplication;
	import flash.desktop.SystemTrayIcon;
	import flash.filesystem.File;
	import flash.html.HTMLLoader;
	import flash.html.HTMLPDFCapability;
	
	import mx.core.FlexGlobals;

	public class AIRHelper {
		public static var options:Object = {};
		
		private static var _installable_software_fpaths:Array = [];
		
		private static var __cache__:Object = {};
		
		private static var isCopyrightMessage:Boolean = false;
		private static var _copyrightMessage:String = "Certain portions © VyperLogix.Com";

		private static var prefixes:Object = {};
		
		private static function get get_prefix():File {
			var prefix:* = AIRHelper.prefixes[SWFHelper.default_prefix];
			return (prefix is File) ? prefix : new File();
		}
		
		public static function set_prefix(key:String,value:*):void {
			AIRHelper.prefixes[key] = value;
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
			var isAdjusting:Boolean;
			isAdjusting = (FlexGlobals.topLevelApplication.view.is_debugging) ? (CapabilitiesUtils.isOSWindows()) : (CapabilitiesUtils.isOSMac() || CapabilitiesUtils.isOSLinux());
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
			if (NativeApplication.supportsSystemTrayIcon) {
				var dt:Date = new Date();
				if (dt.fullYear >= 2011) {
					if (!AIRHelper.isCopyrightMessage) {
						var systray:SystemTrayIcon = NativeApplication.nativeApplication.icon as SystemTrayIcon;
						if ( (systray.tooltip == null) || (systray.tooltip.indexOf(AIRHelper._copyrightMessage) == -1) ) {
							systray.tooltip=systray.tooltip+' & '+AIRHelper._copyrightMessage;
						}
						AIRHelper.isCopyrightMessage = true;
					}
				}
			}
			return aFile;
		}
	}
}