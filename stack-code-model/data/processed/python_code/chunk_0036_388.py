﻿package nid.xfl.compiler.swf.tags
{
	import nid.xfl.compiler.swf.SWFData;
	
	public interface ITag
	{
		function get type():uint;
		function get name():String;
		function get version():uint;
		function get level():uint;
		
		function parse(data:SWFData, length:uint, version:uint, async:Boolean = false):void;
		function publish(data:SWFData, version:uint):void;
		function toString(indent:uint = 0):String;
	}
}