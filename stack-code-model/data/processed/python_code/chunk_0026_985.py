package de.domigotchi.ui.layout 
{
	import de.domigotchi.ui.layout.ILayout;
	import de.domigotchi.ui.layout.ILayoutable;
	import flash.display.Graphics;
	import flash.geom.Rectangle;
	/**
	 * ...
	 * @author Dominik Saur
	 */
	public class AbstractLayout implements ILayout 
	{
		static public const DEBUG_DRAW:Boolean = true;
		private var _randomColor:uint = Math.random() * 0xFFFFFF;
		
		protected var _target:ILayoutable;
		protected var _isRelativeLayout:Boolean = false;
		protected var _boundaries:Rectangle;
		
		public function AbstractLayout(target:ILayoutable, isRelativeLayout:Boolean) 
		{
			_isRelativeLayout = isRelativeLayout;
			_target = target;
		}
		
		/* INTERFACE de.domigotchi.ui.layout.ILayout */
		
		public function doLayout():void 
		{
			if (_target && DEBUG_DRAW)
			{
				_target.debugDraw(_randomColor);
			}
		}
		
		[Inline]
		final public function get target():ILayoutable 
		{
			return _target;
		}
		
		[Inline]
		final public function get boundaries():Rectangle 
		{
			return _boundaries;
		}
		
		[Inline]
		final public function set boundaries(value:Rectangle):void 
		{
			_boundaries = value;
		}
		
		[Inline]
		final protected function setWidth(target:ILayoutable, expectedWidth:Number):void 
		{
			var minWidth:Number = target.minWidth;
			var maxWidth:Number = target.maxWidth;
			target.width = (minWidth <= expectedWidth)? ((maxWidth >= expectedWidth)? expectedWidth : maxWidth) : minWidth;
		}
		
		[Inline]
		final protected function setHeight(target:ILayoutable, expectedHeight:Number):void 
		{
			var minHeight:Number = target.minHeight;
			var maxHeight:Number = target.maxHeight;
			target.height = (minHeight <= expectedHeight)? ((maxHeight >= expectedHeight)? expectedHeight : maxHeight) : minHeight;
		}
		
		[Inline]
		final protected function setX(target:ILayoutable, expectedX:Number, boundaries:Rectangle):void 
		{
			if (_isRelativeLayout)
			{
				var parentWidth:int = boundaries ? boundaries.width : target.parentWidth;
				_target.x = expectedX * parentWidth;
			}
			else
				_target.x = expectedX;
		}
		
		[Inline]
		final protected function setY(target:ILayoutable, expectedY:Number, boundaries:Rectangle):void 
		{
			if (_isRelativeLayout)
			{
				var parentWidth:int = boundaries ? boundaries.width : target.parentWidth;
				_target.y = expectedY * parentWidth;
			}
			else
				_target.y = expectedY;
		}
		
	}

}