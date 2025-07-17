package com.losttemple.utils
{
	import com.losttemple.cfgs.AppCfg;
	
	import flash.filesystem.File;

	public class AssetsUtil
	{
		public static const FSD_PATH:String = File.applicationStorageDirectory.nativePath;
		
		public function AssetsUtil()
		{
		}
		
		public static function get urlHead():String
		{
			return "assets/" + AppCfg.LOCALE + "/" + AppCfg.RUN_TYPE + "/";
		}
		
		/**
		 * 获取配置的地址，用于判断并获取不同平台的地址
		 * @return 
		 */		
		public static function getCfgsUrlByName(name:String):String
		{
			return urlHead + "cfgs/" + name;
		}
		
		/**
		 * 获取碎图片的地址，用于判断并获取不同平台的地址
		 * @return 
		 */		
		public static function getImgsUrlByName(name:String):String
		{
			return urlHead + "imgs/" + name;
		}
		
		/**
		 * 获取声音文件的地址，用于判断并获取不同平台的地址
		 * @return 
		 */		
		public static function getSndsUrlByName(name:String):String
		{
			return urlHead + "snds/" + name;
		}
		
		/**
		 * 获取声音文件的地址，用于判断并获取不同平台的地址
		 * @return 
		 */		
		public static function getTempsUrlByName(name:String):String
		{
			return urlHead + "temps/" + name;
//			return urlHead + "temps/" + name + getTempsType();
		}
		private static function getTempsType():String
		{
			if(AppCfg.RUN_TYPE == "pc")
				return ".csv";
			return ".temp";
		}
		/**
		 * 获取模板表的列表，由于新增模板，肯定会重新打包App，所以，可以用此方法，得到目前的所有模板文件列表
		 * @return 
		 */		
		public static function get tempsAppDirFile():Array
		{
			var file:File = File.applicationDirectory.resolvePath(urlHead + "temps/");
			return file.getDirectoryListing();
		}
		
		/**
		 * 获取UI的地址，用于判断并获取不同平台的地址
		 * @return 
		 */		
		public static function getUIsUrlByName(name:String):String
		{
			return urlHead + "uis/" + name;
		}
		/**
		 * 获取UI的目录File
		 * @return 
		 */	
		public static function getUIsDirFile():File
		{
			var file:File = File.applicationDirectory.resolvePath(urlHead + "uis/");
			return file;
		}
		
	}
}