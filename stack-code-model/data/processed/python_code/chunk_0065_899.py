////////////////////////////////////////////////////////////////////////////////
//
//  ADOBE SYSTEMS INCORPORATED
//  Copyright 2009 Adobe Systems Incorporated
//  All Rights Reserved.
//
//  NOTICE: Adobe permits you to use, modify, and distribute this file
//  in accordance with the terms of the license agreement accompanying it.
//
////////////////////////////////////////////////////////////////////////////////

package mx.charts.renderers
{

import flash.display.Graphics;
import flash.filters.DropShadowFilter;
import flash.geom.Rectangle;
import mx.charts.chartClasses.GraphicsUtilities;
import mx.graphics.IFill;
import mx.graphics.IStroke;
import mx.skins.ProgrammaticSkin;
import mx.core.IDataRenderer;
import mx.graphics.SolidColor;
import mx.utils.ColorUtil;
import mx.charts.ChartItem;

/**
 *  A simple chart itemRenderer implementation
 *  that fills a rectangular area and surrounds it with a drop shadow.
 *  This class can be used as an itemRenderer for ColumnSeries, BarSeries, AreaSeries, LineSeries,
 *  PlotSeries, and BubbleSeries objects.
 *  It renders its area on screen using the <code>fill</code> and <code>stroke</code> styles
 *  of its associated series.
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public class ShadowBoxItemRenderer extends ProgrammaticSkin implements IDataRenderer
{
    include "../../core/Version.as";

    //--------------------------------------------------------------------------
    //
    //  Class constants
    //
    //--------------------------------------------------------------------------

	/**
	 *  @private
	 */
	private static var FILTERS:Array /* of BitMapFilter */ =
		[ new DropShadowFilter(2, 45, 0.2 * 0xFFFFFF) ];
	
    //--------------------------------------------------------------------------
    //
    //  Class variables
    //
    //--------------------------------------------------------------------------

	/**
	 *  @private
	 */
	private static var rcFill:Rectangle = new Rectangle();
	
    //--------------------------------------------------------------------------
    //
    //  Constructor
    //
    //--------------------------------------------------------------------------

	/**
	 *  Constructor.
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function ShadowBoxItemRenderer() 
	{
		super();

		filters = FILTERS;
	}

    //--------------------------------------------------------------------------
    //
    //  Properties
    //
    //--------------------------------------------------------------------------

    //----------------------------------
	//  data
    //----------------------------------

	/**
	 *  @private
	 *  Storage for the data property.
	 */
	private var _data:Object;

	[Inspectable(environment="none")]

	/**
	 *  The chartItem that this itemRenderer is displaying.
	 *  This value is assigned by the owning series
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function get data():Object
	{
		return _data;
	}

	/**
	 *  @private
	 */
	public function set data(value:Object):void
	{
		if (_data == value)
			return;
		_data = value;
	}

	//--------------------------------------------------------------------------
    //
    //  Overridden methods
    //
    //--------------------------------------------------------------------------

	/**
	 *  @private
	 */
	override protected function updateDisplayList(unscaledWidth:Number,
												   unscaledHeight:Number):void
	{
		super.updateDisplayList(unscaledWidth, unscaledHeight);

		var fill:IFill;
		var state:String = "";
		
		if (_data is ChartItem && _data.hasOwnProperty('fill'))
		{
		 	fill = _data.fill;
		 	state = _data.currentState;
		}
		else
		 	fill = GraphicsUtilities.fillFromStyle(getStyle('fill'));
        
        var color:uint;
		var adjustedRadius:Number = 0;
		
		switch (state)
		{
			case ChartItem.FOCUSED:
			case ChartItem.ROLLOVER:
				if (styleManager.isValidStyleValue(getStyle('itemRollOverColor')))
					color = getStyle('itemRollOverColor');
				else
					color = ColorUtil.adjustBrightness2(GraphicsUtilities.colorFromFill(fill),-20);
				fill = new SolidColor(color);
				adjustedRadius = getStyle('adjustedRadius');
				if (!adjustedRadius)
					adjustedRadius = 0;
				break;
			case ChartItem.DISABLED:
				if (styleManager.isValidStyleValue(getStyle('itemDisabledColor')))
					color = getStyle('itemDisabledColor');
				else	
					color = ColorUtil.adjustBrightness2(GraphicsUtilities.colorFromFill(fill),20);
				fill = new SolidColor(GraphicsUtilities.colorFromFill(color));
				break;
			case ChartItem.FOCUSEDSELECTED:
			case ChartItem.SELECTED:
				if (styleManager.isValidStyleValue(getStyle('itemSelectionColor')))
					color = getStyle('itemSelectionColor');
				else
					color = ColorUtil.adjustBrightness2(GraphicsUtilities.colorFromFill(fill),-30);
				fill = new SolidColor(color);
				adjustedRadius = getStyle('adjustedRadius');
				if (!adjustedRadius)
					adjustedRadius = 0;
				break;
		}
		   
		var stroke:IStroke = getStyle("stroke");
				
		var w:Number = stroke ? stroke.weight / 2 : 0;

		rcFill.left = rcFill.left - adjustedRadius;
		rcFill.top = rcFill.top - adjustedRadius;
		rcFill.right = unscaledWidth;
		rcFill.bottom = unscaledHeight;

		var g:Graphics = graphics;
		g.clear();		
		g.moveTo(w - adjustedRadius, w - adjustedRadius);
		if (stroke)
			stroke.apply(g,null,null);
		if (fill)
			fill.begin(g, rcFill,null);
		g.lineTo(unscaledWidth - w + 2 * adjustedRadius, w - adjustedRadius);
		g.lineTo(unscaledWidth - w + 2 * adjustedRadius, unscaledHeight + 2 * adjustedRadius - w);
		g.lineTo(w - adjustedRadius, unscaledHeight + 2 * adjustedRadius - w);
		g.lineTo(w - adjustedRadius, w - adjustedRadius);
		if (fill)
			fill.end(g);
	}
}

}