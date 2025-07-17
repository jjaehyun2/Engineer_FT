package utils {
	import flash.events.Event;
	import flash.filesystem.File;
	import flash.filesystem.FileMode;
	import flash.filesystem.FileStream;
	
	import mx.events.CloseEvent;
	
	import controls.Alert.AlertPopUp;
	
	public class FileHelper {
		private static const Alert_YES:uint = 0x0001;
		
		public static function readFile(aFile:File):String {
			var aStream:FileStream = new FileStream();
			var str:String = '';
			try {
				if (aFile.exists) { 
					aStream.open(aFile, FileMode.READ); 
					str = aStream.readUTFBytes(aStream.bytesAvailable); 
					aStream.close();
				}
			} catch (err:Error) {str = null;}
			return str;
		}

		public static function writeFile(aFile:File,contents:String):String {
			var aStream:FileStream = new FileStream();
			var status:String = 'WARNING - NON SPECIFIED';
			try {
				aStream.open(aFile, FileMode.WRITE); 
				aStream.writeUTFBytes(contents); 
				aStream.close();
				status = null;
			} catch (err:Error) {status = err.toString();}
			return status;
		}
		
		public static function selectSaveAsDestination(callback:Function):void {
			var desktop:File = File.desktopDirectory
			try {
				desktop.browseForDirectory("Select a directory");
				desktop.addEventListener(Event.SELECT, callback);
			} catch (err:Error) {
				///AlertPopUp.surpriseNoOkay(err.message,'ERROR.FileHelper.1');
			}
		}

		public static function copyFile(fileOrig:File, fileDest:File, callback:Function):void {
			fileOrig.addEventListener(Event.COMPLETE, callback);
			
			if (!fileDest.exists) {
				fileOrig.copyToAsync(fileDest);
			}
			else {
				/*
				AlertPopUp.confirm("Are you sure you want to replace the existing file ?","Replace with new file ?", 
				function(event:CloseEvent):void {
				if (event.detail == Alert_YES) {
				fileOrig.copyToAsync(fileDest, true);
				}
				else {
				if (callback is Function) {
				try {
				callback(new Event(Event.COMPLETE));
				} catch (err:Error) {
				AlertPopUp.surpriseNoOkay(err.message,'ERROR.FileHelper.2');
				}
				}
				}
				} 
				);
				*/
			}
		}

		public static function deleteFile(aFile:File, callback:Function):void {
			/*
			AlertPopUp.confirm("Do you really want to delete this file ?","Delete Confirmation", 
			function(event:CloseEvent):void {
			if (event.detail==Alert_YES) {
			if (aFile.isDirectory) {
			aFile.deleteDirectory(false);
			} else {
			aFile.deleteFile();
			}
			if (callback is Function) {
			try {
			callback(new Event(Event.COMPLETE));
			} catch (err:Error) {
			AlertPopUp.surpriseNoOkay(err.message,'ERROR.FileHelper.3');
			}
			}
			}
			} 
			);
			*/
		}
		
		public static function moveFile(fileOrig:File, fileDest:File, callback:Function):void {
			fileOrig.addEventListener(Event.COMPLETE, callback);
			if (!fileDest.exists) {
				fileOrig.moveToAsync(fileDest);
			}
			else {
				/*
				AlertPopUp.confirm("Are you sure you want to replace the existing file ?","Replace with new file ?", 
				function(event:CloseEvent):void {
				if (event.detail== Alert_YES) {
				fileOrig.moveToAsync(fileDest, true);
				}
				else {
				if (callback is Function) {
				try {
				callback(new Event(Event.COMPLETE));
				} catch (err:Error) {
				AlertPopUp.surpriseNoOkay(err.message,'ERROR.FileHelper.4');
				}
				}
				}
				} 
				);
				*/
			}
			
		}		
	}
}