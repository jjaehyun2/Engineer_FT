﻿package com.codeazur.as3swf.data.filters
{
	import com.codeazur.as3swf.SWFData;
	
	public class FilterBevel extends Filter implements IFilter
	{
		public var shadowColor:uint;
		public var highlightColor:uint;
		public var blurX:Number;
		public var blurY:Number;
		public var angle:Number;
		public var distance:Number;
		public var strength:Number;
		public var innerShadow:Boolean;
		public var knockout:Boolean;
		public var compositeSource:Boolean;
		public var onTop:Boolean;
		public var passes:uint;
		
		public function FilterBevel(id:uint) {
			super(id);
		}
		
		override public function parse(data:SWFData):void {
			shadowColor = data.readRGBA();
			highlightColor = data.readRGBA();
			blurX = data.readFIXED();
			blurY = data.readFIXED();
			angle = data.readFIXED();
			distance = data.readFIXED();
			strength = data.readFIXED8();
			var flags:uint = data.readUI8();
			innerShadow = ((flags & 0x80) != 0);
			knockout = ((flags & 0x40) != 0);
			compositeSource = ((flags & 0x20) != 0);
			onTop = ((flags & 0x10) != 0);
			passes = flags & 0x0f;
		}
		
		override public function publish(data:SWFData):void {
			data.writeRGBA(shadowColor);
			data.writeRGBA(highlightColor);
			data.writeFIXED(blurX);
			data.writeFIXED(blurY);
			data.writeFIXED(angle);
			data.writeFIXED(distance);
			data.writeFIXED8(strength);
			var flags:uint = (passes & 0x0f);
			if(innerShadow) { flags |= 0x80; }
			if(knockout) { flags |= 0x40; }
			if(compositeSource) { flags |= 0x20; }
			if(onTop) { flags |= 0x10; }
			data.writeUI8(flags);
		}
	}
}