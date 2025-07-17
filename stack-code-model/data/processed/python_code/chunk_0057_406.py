package com.illuzor.otherside.tools {
	import flash.utils.ByteArray;
	

	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class Keys {
		
		[Embed(source = "../../../../../assets/key_s.osk", mimeType = "application/octet-stream")]
		private static const SettingsKeyClass:Class;
		
		public static function get settingsKey():ByteArray {
			return new SettingsKeyClass() as ByteArray
		}
		
	}
}