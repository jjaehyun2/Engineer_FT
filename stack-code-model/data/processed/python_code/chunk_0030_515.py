package devoron.file 
{
	import flash.utils.ByteArray;
	/**
	 * ...
	 * @author ...
	 */
	public class FileInfoPoint 
	{
		private var _nativePath:String;
		private var _bytes:ByteArray;
		private var _modificationDate:Date;
		
		public function FileInfoPoint(/*path:String*/modificationDate:Date, bytes:ByteArray) 
		{
			this.modificationDate = modificationDate;
			this.data = bytes;
			//this.nativePath = path;
			
		}
		
		public function get data():ByteArray {
			return _bytes;
		}
		
		public function set data(value:ByteArray):void {
			_bytes = value;
		}
		
		public function get modificationDate():Date 
		{
			return _modificationDate;
		}
		
		public function set modificationDate(value:Date):void 
		{
			_modificationDate = value;
		}
		
		public function get nativePath():String
		{
			return _nativePath;
		}
		
		public function set nativePath(value:String):void 
		{
			_nativePath = value;
		}
		
	}

}