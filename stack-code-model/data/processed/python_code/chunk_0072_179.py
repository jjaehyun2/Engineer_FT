﻿package net.flashpunk.graphics 
{
	import flash.display.BitmapData;
	import flash.geom.Point;
	import flash.geom.Rectangle;

	import net.flashpunk.*;

	/**
	 * A simple non-transformed, non-animated graphic.
	 */
	public class Stamp extends Graphic
	{
		/**
		 * Constructor.
		 * @param	source		Source image.
		 * @param	x			X offset.
		 * @param	y			Y offset.
		 */
		public function Stamp(source:*, x:int = 0, y:int = 0) 
		{
			// set the origin
			this.x = x;
			this.y = y;
			
			// set the graphic
			if (!source) return;
			if (source is Class) _source = FP.getBitmap(source);
			else if (source is BitmapData) _source = source;
			if (_source) _sourceRect = _source.rect;
		}
		
		/** @private Renders the Graphic. */
		override public function render(target:BitmapData, point:Point, camera:Point):void 
		{
			if (!_source) return;
			_point.x = point.x + x - camera.x * scrollX;
			_point.y = point.y + y - camera.y * scrollY;
			target.copyPixels(_source, _sourceRect, _point, null, null, true);
		}
		
		/**
		 * Source BitmapData image.
		 */
		public function get source():BitmapData { return _source; }
		public function set source(value:BitmapData):void
		{
			_source = value;
			if (_source) _sourceRect = _source.rect;
		}
		
		/**
		 * Width of the stamp.
		 */
		public function get width():uint { return _source.width; }
		
		/**
		 * Height of the stamp.
		 */
		public function get height():uint { return _source.height; }
		
		/**
		 * Creates a new rectangle Stamp.
		 * @param	width		Width of the rectangle.
		 * @param	height		Height of the rectangle.
		 * @param	color		Color of the rectangle.
		 * @param	alpha		Alpha of the rectangle.
		 * @return	A new Stamp object.
		 */
		public static function createRect(width:uint, height:uint, color:uint = 0xFFFFFF, alpha:Number = 1):Stamp
		{
			color = (0xFFFFFF & color) | (alpha * 255) << 24;
			
			var source:BitmapData = new BitmapData(width, height, true, color);
			
			return new Stamp(source);
		}
		
		// Stamp information.
		/** @private */ private var _source:BitmapData;
		/** @private */ private var _sourceRect:Rectangle;
	}
}