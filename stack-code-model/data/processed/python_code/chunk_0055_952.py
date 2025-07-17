package devoron.file
{
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.filesystem.File;
	import flash.filesystem.FileMode;
	import flash.filesystem.FileStream;
	import flash.utils.ByteArray;
	
	/**
	 * FileInfo (only for Air-application)
	 * @author Devoron
	 */
	public class FileInfo
	{
		
		public var name:String;
		public var extension:String;
		protected var _icons:Array;
		public var creationDate:Date;
		public var creator:String;
		public var isDirectory:Boolean;
		public var isHidden:Boolean;
		public var modificationDate:Date;
		public var nativePath:String;
		public var type:String;
		public var data:ByteArray;
		public var size:Number;
		public var exists:Boolean;
		public var directoryListing:Array;
		public var parentPath:String;
		
		public function FileInfo()
		{
			modificationDate = new Date();
		}
		
		public static function fileInfoFromFile(file:File, emdedData:Boolean = false):FileInfo
		{
			var fileInfo:FileInfo = new FileInfo();
			fileInfo.name = file.name;
			fileInfo.extension = file.extension;
			fileInfo.icons = [];
			fileInfo.exists = file.exists;
			fileInfo.parentPath = file.parent ? file.parent.nativePath : "";
			
			for each (var bd:BitmapData in file.icon.bitmaps)
				//fileInfo.icons.push(bd.getPixels(bd.rect));
				
				fileInfo.icons.push(bd.clone());
			fileInfo.isDirectory = file.isDirectory;
			fileInfo.isHidden = file.isHidden;
			fileInfo.nativePath = file.nativePath;
			fileInfo.exists = file.exists;
			fileInfo.type = file.type;
			if (file.exists)
			{
				fileInfo.size = file.size;
				fileInfo.modificationDate = file.modificationDate;
				fileInfo.creator = file.creator;
				fileInfo.creationDate = file.creationDate;
			}
			
			// если данные должны быть встроены, то прочесть их потоком
			if (emdedData)
			{
				var dataStream:FileStream = new FileStream();
				dataStream.open(file, FileMode.READ);
				var fileData:ByteArray = new ByteArray();
				dataStream.readBytes(fileData);
				dataStream.close();
				fileInfo.data = fileData;
			}
			
			return fileInfo;
		}
		
		public function set icons(value:Array):void
		{
			_icons = value;
		
			// if icons is array of ByteArray convert each BA to BitmapData
		/*if (value is Array)
		   {
		   if (value[0] is ByteArray)
		   {
		   var item:*;
		   var size:uint;
		   var bd:BitmapData;
		   for (var i:int = 0; i < value.length; i++)
		   {
		   item = value[i];
		   if (item is ByteArray)
		   {
		   size = Math.sqrt((item as ByteArray).length) / 2;
		   bd = new BitmapData(size, size, true);
		   bd.setPixels(bd.rect, (item as ByteArray));
		   _icons[i] = bd;
		   }
		   else
		   {
		   _icons[i] = item;
		   }
		   }
		   }
		   }*/
		}
		
		public function get icons():Array
		{
			return _icons;
		}
	
	}
}