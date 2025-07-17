package com.illuzor.otherside.editor.tools {
	
	import com.illuzor.otherside.editor.Settings;
	import deng.fzip.FZip;
	import deng.fzip.FZipFile;
	import flash.events.Event;
	import flash.filesystem.File;
	import flash.filesystem.FileMode;
	import flash.filesystem.FileStream;
	import flash.net.FileFilter;
	import flash.net.FileReference;
	import flash.utils.ByteArray;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class LevelsStorage {
		
		private static var importFileReference:FileReference;
		
		public static function initConfigs():void {
			for (var i:int = 0; i < Settings.TOTAL_ZONES; i++) {
				for (var j:int = 0; j < Settings.TOTAL_LEVELS; j++) {
					writeEmptyFile(i + 1, j + 1);
				}
			}
		}
		
		[Inline]
		private static function writeEmptyFile(zone:uint, level:uint):void {
			var file:File = File.applicationStorageDirectory.resolvePath("levels/zone" + String(zone) + "level" + String(level) + ".osl");
			var stream:FileStream = new FileStream();
			stream.open(file, FileMode.WRITE);
			stream.writeUTFBytes("");
			stream.close();
			stream = null;
		}
		
		public static function getLevel(zone:uint, level:uint):String {
			var file:File = File.applicationStorageDirectory.resolvePath("levels/zone" + String(zone) + "level" + String(level) + ".osl");
			var stream:FileStream = new FileStream();
			stream.open(file, FileMode.READ);
			var string:String = stream.readUTFBytes(stream.bytesAvailable);
			stream.close();
			stream = null;
			return string;
		}
		
		public static function writeLevel(zone:uint, level:uint, levelObj:Object):void {
			var file:File = File.applicationStorageDirectory.resolvePath("levels/zone" + String(zone) + "level" + String(level) + ".osl");
			var stream:FileStream = new FileStream();
			stream.open(file, FileMode.WRITE);
			stream.writeUTFBytes(JSON.stringify(levelObj));
			stream.close();
			stream = null;
		}
		
		public static function exportSettings():void {
			var fzip:FZip = new FZip(); 
			for (var i:int = 0; i < Settings.TOTAL_ZONES; i++) {
				for (var j:int = 0; j < Settings.TOTAL_LEVELS; j++) {
					var file:File = File.applicationStorageDirectory.resolvePath("levels/zone" + String(i+1) + "level" + String(j+1) + ".osl");
					var stream:FileStream = new FileStream();
					stream.open(file, FileMode.READ);
					var fileBytes:ByteArray = new ByteArray();
					stream.readBytes(fileBytes, 0, stream.bytesAvailable);
					stream.close();
					stream = null;
					fzip.addFile(file.name, fileBytes);
				}
			}
			var finalZipBytes:ByteArray = new ByteArray();
			fzip.serialize(finalZipBytes);
			fzip.close();
			finalZipBytes.position = 0;
			
			var exportFileReference:FileReference = new FileReference();
			exportFileReference.save(finalZipBytes, "levels.zip");
		}
		
		public static function importSettings():void {
			importFileReference = new FileReference();
			importFileReference.browse([new FileFilter("Zip (*.zip)", "*.zip")]);
			importFileReference.addEventListener(Event.SELECT, onFileEvent);
			importFileReference.addEventListener(Event.CANCEL, onFileEvent);
		}
		
		private static function onFileEvent(e:Event):void {
			importFileReference.removeEventListener(Event.SELECT, onFileEvent);
			importFileReference.removeEventListener(Event.CANCEL, onFileEvent);
			if (e.type == Event.SELECT) {
				importFileReference.load();
				importFileReference.addEventListener(Event.COMPLETE, onZipLoaded);
			}
		}
		
		private static function onZipLoaded(e:Event):void {
			importFileReference.removeEventListener(Event.COMPLETE, onZipLoaded);
			
			var fzip:FZip = new FZip();
			fzip.loadBytes(importFileReference.data);
			for (var i:int = 0; i < fzip.getFileCount(); i++) {
				var zipFile:FZipFile = fzip.getFileAt(i);
				var file:File = File.applicationStorageDirectory.resolvePath("levels/" + zipFile.filename);
				var stream:FileStream = new FileStream();
				stream.open(file, FileMode.WRITE);
				stream.writeBytes(zipFile.content, 0, zipFile.content.length);
				stream.close();
				stream = null;
			}
		}
		
		public static function openLevelsFolder():void {
			var file:File = File.applicationStorageDirectory.resolvePath("levels");
			file.openWithDefaultApplication();
		}
		
	}
}