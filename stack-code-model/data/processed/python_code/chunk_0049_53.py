﻿package nid.xfl.compiler.swf.tags
{
	import nid.xfl.compiler.swf.SWFData;
	
	import flash.utils.ByteArray;
	
	public class TagProtect implements ITag
	{
		public static const TYPE:uint = 24;
		
		protected var _password:ByteArray;
		
		public function TagProtect() {
			_password = new ByteArray();
		}
		
		public function get password():ByteArray { return _password; }
		
		public function parse(data:SWFData, length:uint, version:uint, async:Boolean = false):void {
			if (length > 0) {
				data.readBytes(_password, 0, length);
			}
		}
		
		public function publish(data:SWFData, version:uint):void {
			data.writeTagHeader(type, _password.length);
			if (_password.length > 0) {
				data.writeBytes(_password);
			}
		}
		
		public function get type():uint { return TYPE; }
		public function get name():String { return "Protect"; }
		public function get version():uint { return 2; }
		public function get level():uint { return 1; }

		public function toString(indent:uint = 0):String {
			return Tag.toStringCommon(type, name, indent);
		}
	}
}