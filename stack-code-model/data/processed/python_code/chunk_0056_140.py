﻿package com.codeazur.as3swf.tags
{
	import com.codeazur.as3swf.SWFData;
	import com.codeazur.as3swf.data.SWFSoundInfo;
	
	public class TagStartSound extends Tag implements ITag
	{
		public static const TYPE:uint = 15;
		
		public var soundId:uint;
		public var soundInfo:SWFSoundInfo;
		
		public function TagStartSound() {}
		
		public function parse(data:SWFData, length:uint, version:uint):void {
			soundId = data.readUI16();
			soundInfo = data.readSOUNDINFO();
		}
		
		public function publish(data:SWFData, version:uint):void {
			var body:SWFData = new SWFData();
			body.writeUI16(soundId);
			body.writeSOUNDINFO(soundInfo);
			data.writeTagHeader(type, body.length);
			data.writeBytes(body);
		}
		
		override public function get type():uint { return TYPE; }
		override public function get name():String { return "StartSound"; }
		override public function get version():uint { return 1; }
		
		public function toString(indent:uint = 0):String {
			var str:String = toStringMain(indent) +
				"SoundID: " + soundId + ", " +
				"SoundInfo: " + soundInfo;
			return str;
		}
	}
}