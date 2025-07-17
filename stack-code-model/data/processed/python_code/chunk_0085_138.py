package org.aswing.plaf.basic.border
{
	import org.aswing.Insets;
	import org.aswing.lookandfeel.plaf.UIResource;
	import starling.display.DisplayObject;
	import starling.display.Graphics;
	import flash.filters.BevelFilter;
	import flash.filters.BitmapFilterType;
	import devoron.aswing3d.*;
	import org.aswing.geom.*;
	import org.aswing.graphics.*;
	import org.aswing.plaf.*;
	import org.aswing.plaf.basic.BasicGraphicsUtils;
	import starling.display.Shape;
	import starling.filters.BlurFilter;
	
	/**
	 * @private
	 */
	public class PopupMenuBorder implements Border, UIResource
	{
		
		protected var shape:Shape;
		
		public function PopupMenuBorder()
		{
			shape = new Shape();
		}
		
		public function updateBorder(c:Component, g:Graphics2D, b:IntRectangle):void
		{
			//shape.graphics.clear();
			if (c.isOpaque())
			{
				b = b.clone();
				b.height -= 4;
				b.width -= 4;
				g = new Graphics2D(new Graphics(shape));
				var tune:StyleTune = c.getStyleTune();
				var cl:ASColor = c.getBackground();
				var style:StyleResult = new StyleResult(cl.changeAlpha(1), tune);
				
				BasicGraphicsUtils.fillGradientRoundRect(g, b, style, Math.PI / 2);
				BasicGraphicsUtils.drawGradientRoundRectLine(g, b, 1, style, Math.PI / 2);
				shape.filter = BlurFilter.createDropShadow(1, 45, 0x0, style.shadow, 4, 0.6);
				
				shape.alpha = cl.getAlpha();
			}
			shape.visible = c.isOpaque();
		}
		
		public function getBorderInsets(com:Component, bounds:IntRectangle):Insets
		{
			return new Insets(2, 2, 6, 6);
		}
		
		public function getDisplay(c:Component):DisplayObject
		{
			return shape;
		}
	
	}
}