package com.illuzor.circles.tools {
	
	import com.hurlant.crypto.prng.ARC4;
	import com.illuzor.circles.utils.decrypt;
	import com.illuzor.circles.utils.encrypt;
	import flash.filesystem.File;
	import flash.filesystem.FileMode;
	import flash.filesystem.FileStream;
	import flash.utils.ByteArray;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class StorageManager {
		
		private static var file:File;
		private static var settings:Object = { };
		private static var key:ByteArray = Assets.key;
		
		public static function init():void {
			file = File.applicationStorageDirectory.resolvePath("game.data");
			if (file.exists) {
				readSettings();
			} else {
				settings["sound"] = true;
				settings["vibro"] = true;
				settings["timeScores"] = 0;
				settings["sizeScores"] = 0;
				settings["completeScores"] = 0;
				settings["runs"] = 0;
				settings["plays"] = 0;
				writeSettings();
			}
		}
		
		private static function readSettings():void {
			var stream:FileStream = new FileStream();
			stream.open(file, FileMode.READ);
			var bytes:ByteArray = new ByteArray();
			stream.readBytes(bytes);
			decrypt(bytes, Assets.key);
			settings = JSON.parse(bytes.readUTFBytes(bytes.bytesAvailable));
			stream.close();
			stream = null;
		}
		
		private static function writeSettings():void {
			var bytes:ByteArray = new ByteArray();
			bytes.writeUTFBytes(JSON.stringify(settings));
			encrypt(bytes, Assets.key);
			var stream:FileStream = new FileStream();
			stream.open(file, FileMode.WRITE);
			stream.writeBytes(bytes);
			stream.close();
			stream = null;
		}
		
		public static function setBool(name:String, value:Boolean):void {
			settings[name] = value;
			writeSettings();
		}
		
		public static function getBool(name:String):Boolean {
			return settings[name] as Boolean;
		}
		
		public static function setInt(name:String, value:int):void {
			settings[name] = value;
			writeSettings();
		}
		
		public static function getInt(name:String):int {
			return settings[name] as int;
		}
		
		public static function increaseRuns():void {
			var runs:uint = settings["runs"];
			settings["runs"] = runs + 1;
			writeSettings();
		}
		
		public static function increasePlays():void {
			var runs:uint = settings["plays"];
			settings["plays"] = runs + 1;
			writeSettings();
		}
		
	}
}