package com.illuzor.spinner.tools {
	
	import com.illuzor.spinner.assets.Keys;
	import com.illuzor.spinner.errors.StorageManagerError;
	import com.illuzor.spinner.utils.decrypt;
	import com.illuzor.spinner.utils.encrypt;
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
		private static var settings:Object;
		
		public static function init():void {
			file = File.applicationStorageDirectory.resolvePath("hh.sav");
			trace("[StorageManager] Native savefile path:", file.nativePath);
			
			if (file.exists) {
				readSettings();
			} else {
				settings = { sound:true, music:true, vibro:true, runs:0 };
				writeSettings();
			}
		}
		
		private static function readSettings():void {
			var stream:FileStream = new FileStream();
			stream.open(file, FileMode.READ);
			var bytes:ByteArray = new ByteArray();
			stream.readBytes(bytes);
			decrypt(bytes, Keys.settingsKey);
			stream.close();
			
			try {
				settings = JSON.parse(bytes.readUTFBytes(bytes.bytesAvailable));
			} catch (e:Error) {
				settings = { sound:true, music:true, vibro:true, runs:0};
				writeSettings();
				trace("savefile is broken");
				//MessageTool.showMessage(ResizeManager.stage, "Savefile is broken. Your progress was reset. \nTap to continue", true);
			}
		}
		
		private static function writeSettings():void {
			var bytes:ByteArray = new ByteArray();
			bytes.writeUTFBytes(JSON.stringify(settings));
			encrypt(bytes, Keys.settingsKey);
			var stream:FileStream = new FileStream();
			stream.open(file, FileMode.WRITE);
			stream.writeBytes(bytes);
			stream.close();
		}
		
		public static function setBool(name:String, value:Boolean):void {
			settings[name] = value;
			writeSettings();
		}
		
		public static function getBool(name:String):Boolean {
			if (settings.hasOwnProperty(name)) {
				return settings[name] as Boolean;
			} else {
				throw new StorageManagerError("Boolean key " + name + " not exists.");
			}
			return false;
		}
		
		public static function setInt(name:String, value:int):void {
			settings[name] = value;
			writeSettings();
		}
		
		public static function getInt(name:String):int {
			if (settings.hasOwnProperty(name)) {
				return settings[name] as int;
			} else {
				throw new StorageManagerError("int key " + name + " not exists.");
			}
			return 0;
		}
		
		public static function increaseRuns():void {
			var runsNum:uint = settings.runs + 1;
			settings.runs = runsNum;
			writeSettings();
		}
		
	}
}