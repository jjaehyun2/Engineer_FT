﻿package com.codeazur.as3swf.tags
{
	import com.codeazur.as3swf.SWFData;
	
	public class TagRemoveObject extends Tag implements ITag, IDisplayListTag
	{
		public static const TYPE:uint = 5;
		
		public var characterId:uint = 0;
		public var depth:uint;
		
		public function TagRemoveObject() {}
		
		public function parse(data:SWFData, length:uint, version:uint):void {
			characterId = data.readUI16();
			depth = data.readUI16();
		}
		
		public function publish(data:SWFData, version:uint):void {
			data.writeTagHeader(type, 4);
			data.writeUI16(characterId);
			data.writeUI16(depth);
		}
		
		override public function get type():uint { return TYPE; }
		override public function get name():String { return "RemoveObject"; }
		override public function get version():uint { return 1; }
		
		public function toString(indent:uint = 0):String {
			return toStringMain(indent) +
				"CharacterID: " + characterId + ", " +
				"Depth: " + depth;
		}
	}
}