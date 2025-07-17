package com.illuzor.otherside.controllers.storage {
	
	import com.illuzor.otherside.debug.log;
	import com.illuzor.otherside.errors.StorageControllerError;
	import com.illuzor.otherside.interfaces.IStorageController;
	import com.illuzor.otherside.tools.Keys;
	import com.illuzor.otherside.utils.decrypt;
	import com.illuzor.otherside.utils.encrypt;
	import flash.filesystem.File;
	import flash.filesystem.FileMode;
	import flash.filesystem.FileStream;
	import flash.utils.ByteArray;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	internal final class StorageControllerMobile implements IStorageController {
		
		private var file:File;
		private var settings:Object;
		
		public function init():void {
			file = File.applicationStorageDirectory.resolvePath("os.sav");
			log("[StorageManager] Native savefile path:", file.nativePath);
			if (file.exists) {
				readSettings();
			} else {
				settings = { sound:true, music:true, vibro:true, runs:0 };
				writeSettings();
			}
		}
		
		private function readSettings():void {
			var stream:FileStream = new FileStream();
			stream.open(file, FileMode.READ);
			var bytes:ByteArray = new ByteArray();
			stream.readBytes(bytes);
			decrypt(bytes, Keys.saveKey);
			stream.close();
			
			try {
				settings = JSON.parse(bytes.readUTFBytes(bytes.bytesAvailable));
			} catch (e:Error) {
				settings = { sound:true, music:true, vibro:true, runs:0 };
				writeSettings();
				// TODO вывод сообщения об ошибке чтения настроек
			}
		}
		
		private function writeSettings():void {
			var bytes:ByteArray = new ByteArray();
			bytes.writeUTFBytes(JSON.stringify(settings));
			encrypt(bytes, Keys.saveKey);
			var stream:FileStream = new FileStream();
			stream.open(file, FileMode.WRITE);
			stream.writeBytes(bytes);
			stream.close();
		}
		
		public function increaseRuns():void {
			var runsNum:uint = settings.runs + 1;
			settings.runs = runsNum;
			writeSettings();
		}
		
		public function setBool(name:String, value:Boolean):void {
			settings[name] = value;
			writeSettings();
		}
		
		public function getBool(name:String):Boolean {
			if (settings.hasOwnProperty(name)) {
				return settings[name] as Boolean;
			} else {
				throw new StorageControllerError("Boolean key " + name + " not exists.");
			}
			return false;
		}
		
		public function setInt(name:String, value:int):void {
			settings[name] = value;
			writeSettings();
		}
		
		public function getInt(name:String):int {
			if (settings.hasOwnProperty(name)) {
				return settings[name] as int;
			} else {
				throw new StorageControllerError("int key " + name + " not exists.");
			}
			return 0;
		}
		
		public function setObj(name:String, value:Object):void {
			settings[name] = value;
			writeSettings();
		}
		
		public function getObj(name:String):Object {
			if (settings.hasOwnProperty(name)) {
				return settings[name] as Object;
			} else {
				throw new StorageControllerError("Object key " + name + " not exists.");
			}
			return null;
		}
		
	}
}