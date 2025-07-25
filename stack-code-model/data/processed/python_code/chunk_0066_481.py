﻿package com.codeazur.as3swf.tags
{
	import com.codeazur.as3swf.SWFData;
	
	import flash.utils.ByteArray;
	
	public class TagProtect extends Tag implements ITag
	{
		public static const TYPE:uint = 24;
		
		protected var _password:ByteArray;
		
		public function TagProtect() {
			_password = new ByteArray();
		}
		
		public function get password():ByteArray { return _password; }
		
		public function parse(data:SWFData, length:uint, version:uint):void {
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
		
		override public function get type():uint { return TYPE; }
		override public function get name():String { return "Protect"; }
		override public function get version():uint { return 2; }
		
		public function toString(indent:uint = 0):String {
			return toStringMain(indent);
		}
	}
}