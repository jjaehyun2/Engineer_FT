package de.domigotchi.ui.layout 
{
	import flash.geom.Rectangle;
	
	/**
	 * ...
	 * @author Dominik Saur
	 */
	public interface ILayoutable 
	{
		function get layoutParent():Object;
		function get parentHeight():Number;
		function get parentWidth():Number;
		
		function get x():Number;
		function get y():Number;
		function get left():Number;
		function get top():Number;
		function get right():Number;
		function get bottom():Number;		
		
		function get width():Number;
		function get minWidth():Number;
		function get maxWidth():Number;
		
		function set width(value:Number):void;
		function set minWidth(value:Number):void;
		function set maxWidth(value:Number):void;
		
		function get height():Number;
		function get minHeight():Number;
		function get maxHeight():Number;
		
		function set height(value:Number):void;
		function set minHeight(value:Number):void;
		function set maxHeight(value:Number):void;
		
		function set x(value:Number):void;
		function set y(value:Number):void;
		function set left(value:Number):void;
		function set top(value:Number):void;
		function set right(value:Number):void;
		function set bottom(value:Number):void;
		
		function setPadding(left:Number, top:Number, right:Number, bottom:Number):void

		
		function get layout():ILayout;
		function set layout(value:ILayout):void;
		
		function debugDraw(color:uint):void
		
		function get visible():Boolean;
		function set visible(value:Boolean):void;
		
	}
	
}