/**
 * Copyright (c) 2014-present, ErZhuan(coco) Xie
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
package coco.util
{
	
	import flash.system.Capabilities;
	import flash.utils.getDefinitionByName;
	
	/**
	 *  The Platform utility class contains several static methods to check what
	 *  desktop or mobile platform the application is running on.
	 *  
	 */
	public class Platform
	{
		private static var _instance: Platform;
		
		protected static var _initialized:Boolean;
		protected static var _isAndroid:Boolean;
		protected static var _isIOS:Boolean;
		protected static var _isIPad:Boolean;
		protected static var _isBlackBerry:Boolean;
		protected static var _isMobile:Boolean;
		protected static var _isMac:Boolean;
		protected static var _isWindows:Boolean;
		protected static var _isLinux:Boolean;
		protected static var _isDesktop:Boolean;
		protected static var _isBrowser:Boolean;
		protected static var _isAir:Boolean;
		private static var _osVersion: String = null;
		private static var _os:String = null;
		private static var _version:String = null;
		private static var _playerType:String = null;
		
		public static function get os():String
		{
			getPlatforms();
			
			return _os;
		}
		
		public static function get version():String
		{
			getPlatforms();
			
			return _version;
		}
		
		public static function get playerType():String
		{
			getPlatforms();
			
			return _playerType;
		}
		
		/**
		 *  Returns true if the application is running on IOS.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10
		 *  @playerversion AIR 2.0
		 *  @productversion Flex 4.12
		 */
		public static function get isIOS():Boolean
		{
			getPlatforms();
			
			return _isIOS;
		}
		
		/**
		 *  Returns true if the application is running on an iPad.
		 *  Note this returns false in the AIR mobile device simulator.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10
		 *  @playerversion AIR 2.0
		 *  @productversion Flex 4.12
		 */
		public static function get isIPad():Boolean
		{
			getPlatforms();
			
			return _isIPad;
		}
		
		/**
		 *  Returns true if the application is running on a BlackBerry.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10
		 *  @playerversion AIR 2.0
		 *  @productversion Flex 4.12
		 */
		public static function get isBlackBerry():Boolean
		{
			getPlatforms();
			
			return _isBlackBerry;
		}
		
		/**
		 *  Returns true if the application is running on Android.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10
		 *  @playerversion AIR 2.0
		 *  @productversion Flex 4.12
		 */
		public static function get isAndroid():Boolean
		{
			getPlatforms();
			
			return _isAndroid;
		}
		
		/**
		 *  Returns true if the application is running on Windows.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10
		 *  @playerversion AIR 2.0
		 *  @productversion Flex 4.12
		 */
		public static function get isWindows():Boolean
		{
			getPlatforms();
			
			return _isWindows;
		}
		
		/**
		 *  Returns true if the application is running on a Mac.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10
		 *  @playerversion AIR 2.0
		 *  @productversion Flex 4.12
		 */
		public static function get isMac():Boolean
		{
			getPlatforms();
			
			return _isMac;
		}
		
		/**
		 *  Returns true if the application is running on Linux.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10
		 *  @playerversion AIR 2.0
		 *  @productversion Flex 4.12
		 */
		public static function get isLinux():Boolean
		{
			getPlatforms();
			
			return _isLinux;
		}
		
		/**
		 *  Returns true if the application is running on a Desktop OS.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10
		 *  @playerversion AIR 2.0
		 *  @productversion Flex 4.12
		 */
		public static function get isDesktop():Boolean
		{
			getPlatforms();
			
			return _isDesktop;
		}
		
		/**
		 *  Returns true if the application is running on a Mobile device.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10
		 *  @playerversion AIR 2.0
		 *  @productversion Flex 4.12
		 */
		public static function get isMobile():Boolean
		{
			getPlatforms();
			
			return _isMobile;
		}
		
		/**
		 *  Returns true if the application is running on a desktop AIR.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10
		 *  @playerversion AIR 2.0
		 *  @productversion Flex 4.12
		 */
		public static function get isAir():Boolean
		{
			getPlatforms();
			
			return _isAir;
		}
		
		/**
		 *  Returns true if the application is running in a browser.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10
		 *  @playerversion AIR 2.0
		 *  @productversion Flex 4.12
		 */
		public static function get isBrowser():Boolean
		{
			getPlatforms();
			
			return _isBrowser;
		}
		
		/**
		 *  Returns the version of the OS the application  is running on
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10
		 *  @playerversion AIR 2.0
		 *  @productversion Flex 4.13
		 */
		public static function get osVersion(): String
		{
			//We needed to compute _osVersion later than getPlatforms, because it relies on resources that  ready later
			if (_osVersion == null){
				_osVersion = computeOSVersionString();
			}
			return _osVersion;
		}
		
		/* Notes on Capabilities.os for mobile apps:
		- on ADL => returns the OS where the ADL is running ( eg. Windows 7, or Mac OS )
		- on device => returns the OS of the device (eg.  iPhone OS ...  for iOS devices  )
		* */
		protected static function getPlatforms():void {
			if (!_initialized)
			{
				var cap: Class = Capabilities;
				_version = Capabilities.version;
				_os = Capabilities.os;
				_playerType = Capabilities.playerType;
				
				_isAndroid = _version.indexOf("AND") > -1;
				_isIOS = _version.indexOf('IOS') > -1;
				_isBlackBerry = _version.indexOf('QNX') > -1;
				_isMobile = _isAndroid || _isIOS || _isBlackBerry;
				
				_isMac = _os.indexOf("Mac OS") != -1;
				_isWindows = _os.indexOf("Windows") != -1;
				_isLinux = _os.indexOf("Linux") != -1; // note that Android is also Linux
				_isIPad = _os.indexOf('iPad') > -1;
				_isDesktop = !_isMobile;
				
				_isAir = _playerType == "Desktop";
				_isBrowser = (_playerType == "Plugin" || _playerType == "ActiveX");
				
				_initialized = true;
			}
		}
		
		/** @private
		 * extract OS version information from Capabilities.os
		 * os is typically a non-numeric string (such as Windows,  iPhone OS, Android, etc...)  followed by a number sequence.
		 * if no number is found, OS version is set to 0.
		 * os on ADL will return the host OS and not the device OS.
		 *
		 * That's why we need to check for a specific sequence for iOS and Android.
		 * On Android, os  is the Linux kernel version (such as Linux 3.4.34-1790463).
		 * So the version information must be  retrieved from an internal file.
		 * Since reading files API is only available on AIR, it's delegated to PlatformMobileHelper  in mobilecomponents.swc
		 * @see   spark.utils.PlatformMobileHelper
		 *
		 * @return version number string, or empty string if could not retrieve the version.
		 * */
		private static function computeOSVersionString(): String
		{
			var os: String = Capabilities.os;
			var osVersionMatch: Array;
			var version: String = "";
			
			if (isIOS) {
				osVersionMatch = os.match(/iPhone OS\s([\d\.]+)/);
				if (osVersionMatch && osVersionMatch.length == 2)
					version = osVersionMatch[1];
			}
			else if (isAndroid) {
				try {
					var mobileHelperClass: Class = Class(getDefinitionByName("spark.utils::PlatformMobileHelper"));
					if (mobileHelperClass != null) {
						version = mobileHelperClass["computeOSVersionForAndroid"]();
					}
				}
				catch (e: Error) {
					debug("Error: " + e.message);
				}
			}
			else {
				//on  other OS, extract version
				osVersionMatch = os.match(/[A-Za-z\s]+([\d\.]+)/);
				if (osVersionMatch && osVersionMatch.length == 2)
					version = osVersionMatch[1];
			}
			return version;
		}
		
	}
}