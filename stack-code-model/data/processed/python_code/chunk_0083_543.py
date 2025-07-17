package com.illuzor.thegame.editor.tools {
	
	import flash.filesystem.File;
	import flash.filesystem.FileStream;
	import flash.filesystem.FileMode;
	import by.blooddy.crypto.serialization.JSON;
	import flash.net.FileFilter;
	import flash.net.FileReference;
	import flash.events.Event;
	
	/**
	 * ...
	 * @author illuzor // illuzor.com // illuzor@gmail.com
	 */
	public class StorageManager {
		
		private static var file:File;
		private static var levels:Object;
		static private var importFR:FileReference;
		
		public static function init():void {
			file = File.applicationStorageDirectory.resolvePath("levels.pgc"); // portal game config
			//levels = { levels:[] };
			if (!file.exists) {
				levels = { levels:[] };
			} else {
				levels = readFile();
			}
		}
		
		private static function readFile():Object {
			var obj:Object;
			
			var stream:FileStream = new FileStream();
			stream.open(file, FileMode.READ);
			var fileString:String = stream.readUTF()
			obj = by.blooddy.crypto.serialization.JSON.decode(fileString);
			trace(by.blooddy.crypto.serialization.JSON.encode(obj));
			stream.close();
			stream = null;
			return obj;
		}
		
		private static function writeFile():void {
			var stream:FileStream = new FileStream();
			stream.open(file, FileMode.WRITE);
			trace(by.blooddy.crypto.serialization.JSON.encode(levels))
			stream.writeUTF(by.blooddy.crypto.serialization.JSON.encode(levels));
			stream.close();
			stream = null;
		}
		
		public static function writeLevel(level:Object):void {
			var levelExists:Boolean
			
			for (var i:int = 0; i < levels.levels.length ; i++) {
				if (levels.levels[i].name == level.name) {
					levelExists = true;
					break;
				}
			}
			
			if (levelExists) {
				levels.levels[i] = level;
			} else {
				level.num = levels.levels.length;
				levels.levels.push(level);
			}

			writeFile();
		}
		
		public static function getAllLevels():Array {
			return levels.levels;
		}
		
		public static function getCurrentLevel(levelNum:uint):Object {
			return levels.levels[levelNum];
		}
		
		public static function getCurrentLevelNum():uint {
			return levels.levels.length;
		}
		
		public static function checkNameSimulation(name:String):Boolean {
			for (var i:int = 0; i < levels.levels.length; i++) {
				if (levels.levels[i].name == name) {
					return false;
					break;
				}
			}
			return true;
		}
		
		public static function exportConfig():void {
			var exportFR:FileReference = new FileReference();
			exportFR.save(by.blooddy.crypto.serialization.JSON.encode(levels), "levels.pgc");
		}
		
		public static function importConfig():void {
			var fileType:FileFilter = new FileFilter("Portal Game Config (*.pgc,)", "*.pgc;*");
			importFR = new FileReference();
			importFR.addEventListener(Event.SELECT, fileSelected);
			importFR.browse([fileType]);
		}
		
		static private function fileSelected(e:Event):void {
			importFR.removeEventListener(Event.SELECT, fileSelected);
			importFR.addEventListener(Event.COMPLETE, fileLoaded);
			importFR.load();
		}
		
		static private function fileLoaded(e:Event):void {
			importFR.removeEventListener(Event.COMPLETE, fileLoaded);
			var loadedObj:Object;
			try {
				loadedObj = by.blooddy.crypto.serialization.JSON.decode(String(importFR.data));
				trace("PARCING CORRECT")
			} catch (e:Error) {
				trace("PARCING ERROR")
			}
		}
		
	}
}