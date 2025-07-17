package de.domigotchi.ui.layout.starling 
{
	import de.domigotchi.ui.layout.AnchorLayout;
	import de.domigotchi.ui.layout.AnchorTypes;
	import de.domigotchi.ui.layout.ILayout;
	import de.domigotchi.ui.layout.ILayoutable;
	import de.domigotchi.ui.layout.ILayoutableTextField;
	import flash.geom.Rectangle;
	import starling.text.TextField;
	
	/**
	 * ...
	 * @author Dominik Saur
	 */
	public class LayoutableTextField extends TextField implements ILayoutableTextField 
	{
		private var _left:Number = 0;
		private var _top:Number = 0;
		private var _right:Number = 0;
		private var _bottom:Number = 0;
		private var _layout:ILayout;
		
		private var _minWidth:Number = 0;
		private var _maxWidth:Number = Number.MAX_VALUE;
		private var _minHeight:Number = 0;
		private var _maxHeight:Number = Number.MAX_VALUE;
		
		public function LayoutableTextField() 
		{
			super(0,0,"");
		}
		
		// not inlineable
		override public function set text(value:String):void 
		{
			super.text = value;
			/*if (layoutParent && "layout" in layoutParent)
			{
				layoutParent["layout"]["doLayout"]();
			}*/
		}
		
	
		
		/* INTERFACE de.domigotchi.ui.layout.ILayoutable */
		
		[Inline]
		final public function get minWidth():Number 
		{
			return _minWidth;
		}
		
		[Inline]
		final public function get maxWidth():Number 
		{
			return _maxWidth;
		}
		
		[Inline]
		final public function set minWidth(value:Number):void 
		{
			_minWidth = value;
		}
		
		[Inline]
		final public function set maxWidth(value:Number):void 
		{
			_maxWidth = value;
		}
		
		[Inline]
		final public function get minHeight():Number 
		{
			return _minHeight;
		}
		
		[Inline]
		final public function get maxHeight():Number 
		{
			return _maxHeight;
		}
		
		[Inline]
		final public function set minHeight(value:Number):void 
		{
			_minHeight = value;
		}
		
		[Inline]
		final public function set maxHeight(value:Number):void 
		{
			_maxHeight = value;
		}
		
		/* INTERFACE de.domigotchi.ui.layout.ILayoutable */
		
		[Inline]
		final public function set layout(value:ILayout):void 
		{
			_layout = value;
		}
		
		/* INTERFACE de.domigotchi.ui.layout.ILayoutable */
		
		[Inline]
		final public function get layout():ILayout 
		{
			return _layout;
		}
		
		/* INTERFACE de.domigotchi.ui.layout.ILayoutable */
		
		[Inline]
		final public function get parentHeight():Number 
		{
			return parent.height;
		}
		
		[Inline]
		final public function get parentWidth():Number 
		{
			return parent.width;
		}
		
		
		/* INTERFACE de.domigotchi.ui.layout.ILayoutable */
		
		[Inline]
		final public function get layoutParent():Object 
		{
			return parent;
		}
		
		[Inline]
		final public function get left():Number 
		{
			return _left;
		}
		
		[Inline]
		final public function get top():Number 
		{
			return _top;
		}
		
		[Inline]
		final public function get right():Number 
		{
			return _right;
		}
		
		[Inline]
		final public function get bottom():Number 
		{
			return _bottom;
		}
		
		[Inline]
		final public function set left(value:Number):void 
		{
			_left = value;
		}
		
		public function set top(value:Number):void 
		{
			_top = value;
		}
		[Inline]
		final public function set right(value:Number):void 
		{
			_right = value;
		}
		
		[Inline]
		final public function set bottom(value:Number):void 
		{
			_bottom = value;
		}
		
		public function setPadding(left:Number, top:Number, right:Number, bottom:Number):void 
		{
			_left = left;
			_top = top;
			_right = right;
			_bottom = bottom;
		}
		
		/* INTERFACE de.domigotchi.ui.layout.ILayoutableTextField */
		
		public function debugDraw(color:uint):void 
		{
			
		}
		
	}

}