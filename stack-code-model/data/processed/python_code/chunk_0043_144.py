﻿package com.codeazur.as3swf.tags
{
	import com.codeazur.as3swf.SWFData;
	import com.codeazur.as3swf.data.SWFClipActions;
	import com.codeazur.as3swf.data.SWFColorTransform;
	import com.codeazur.as3swf.data.SWFMatrix;
	import com.codeazur.as3swf.data.filters.IFilter;
	
	public class TagPlaceObject extends Tag implements ITag, IDisplayListTag
	{
		public static const TYPE:uint = 4;
		
		public var hasClipActions:Boolean;
		public var hasClipDepth:Boolean;
		public var hasName:Boolean;
		public var hasRatio:Boolean;
		public var hasColorTransform:Boolean;
		public var hasMatrix:Boolean;
		public var hasCharacter:Boolean;
		public var hasMove:Boolean;
		public var hasImage:Boolean;
		public var hasClassName:Boolean;
		public var hasCacheAsBitmap:Boolean;
		public var hasBlendMode:Boolean;
		public var hasFilterList:Boolean;
		
		public var characterId:uint;
		public var depth:uint;
		public var matrix:SWFMatrix;
		public var colorTransform:SWFColorTransform;

		// Forward declarations for TagPlaceObject2
		public var ratio:uint;
		public var objName:String;
		public var clipDepth:uint;
		public var clipActions:SWFClipActions;

		// Forward declarations for TagPlaceObject3
		public var className:String;
		public var blendMode:uint;
		public var bitmapCache:uint;
		
		protected var _surfaceFilterList:Vector.<IFilter>;
		
		public function TagPlaceObject() {
			_surfaceFilterList = new Vector.<IFilter>();
		}
		
		public function get surfaceFilterList():Vector.<IFilter> { return _surfaceFilterList; }
		
		public function parse(data:SWFData, length:uint, version:uint):void {
			var pos:uint = data.position;
			characterId = data.readUI16();
			depth = data.readUI16();
			matrix = data.readMATRIX();
			hasCharacter = true;
			hasMatrix = true;
			if (data.position - pos < length) {
				colorTransform = data.readCXFORM();
				hasColorTransform = true;
			}
		}
		
		public function publish(data:SWFData, version:uint):void {
			var body:SWFData = new SWFData();
			body.writeUI16(characterId);
			body.writeUI16(depth);
			body.writeMATRIX(matrix);
			if (hasColorTransform) {
				body.writeCXFORM(colorTransform);
			}
			data.writeTagHeader(type, body.length);
			data.writeBytes(body);
		}
		
		override public function get type():uint { return TYPE; }
		override public function get name():String { return "PlaceObject"; }
		override public function get version():uint { return 1; }
		
		public function toString(indent:uint = 0):String {
			var str:String = toStringMain(indent) +
				"Depth: " + depth;
			if (hasCharacter) { str += ", CharacterID: " + characterId; }
			if (hasMatrix) { str += ", Matrix: " + matrix; }
			if (hasColorTransform) { str += ", ColorTransform: " + colorTransform; }
			return str;
		}
	}
}