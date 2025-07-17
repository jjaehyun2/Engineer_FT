package org.aswing.skinbuilder
{
	import starling.display.DisplayObject;
	import org.aswing.GroundDecorator;
	import org.aswing.geom.IntRectangle;
	import org.aswing.graphics.Graphics2D;
	import org.aswing.lookandfeel.plaf.UIResource;
	import org.aswing.Component;
	
	/**
	 * blank bg.
	 */
	public class SkinFrameTitleBarBG implements GroundDecorator, UIResource
	{
		public function SkinFrameTitleBarBG()
		{
			super();
		}
		
		public function getDisplay(c:Component):DisplayObject
		{
			return null;
		}
		
		public function updateDecorator(com:Component, g:Graphics2D, bounds:IntRectangle):void
		{
		}
	
	}
}