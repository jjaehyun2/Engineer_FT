////////////////////////////////////////////////////////////////////////////////
//
//  Licensed to the Apache Software Foundation (ASF) under one or more
//  contributor license agreements.  See the NOTICE file distributed with
//  this work for additional information regarding copyright ownership.
//  The ASF licenses this file to You under the Apache License, Version 2.0
//  (the "License"); you may not use this file except in compliance with
//  the License.  You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.
//
////////////////////////////////////////////////////////////////////////////////

package mx.charts.renderers
{

import mx.display.Graphics;
import org.apache.royale.geom.Rectangle;
import mx.charts.chartClasses.GraphicsUtilities;
import mx.graphics.IFill;
import mx.graphics.IStroke;
import mx.skins.ProgrammaticSkin;
import mx.core.IDataRenderer;
import mx.charts.ChartItem;
import mx.graphics.SolidColor;
import org.apache.royale.utils.ColorUtil;

/**
 *  A simple chart itemRenderer implementation
 *  that fills a diamond in its assigned area.
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
public class DiamondItemRenderer extends ProgrammaticSkin implements IDataRenderer
{
//    include "../../core/Version.as";

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
	public function DiamondItemRenderer() 
	{
		super();
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

		var cx:Number = unscaledWidth / 2;
		var cy:Number = unscaledHeight / 2;
		
		rcFill.left = rcFill.left - adjustedRadius;
		rcFill.top = rcFill.top - adjustedRadius;
		rcFill.right = unscaledWidth + adjustedRadius;
		rcFill.bottom = unscaledHeight + adjustedRadius;

		var g:Graphics = graphics;
		g.clear();		
		g.moveTo(w, w);
		if (stroke)
			stroke.apply(g,null,null);
		g.moveTo(cx, w - adjustedRadius);
		if (fill)
			fill.begin(g, rcFill, null);
		g.lineTo(unscaledWidth - w + adjustedRadius, cy);
		g.lineTo(cx, unscaledHeight - w + adjustedRadius);
		g.lineTo(w - adjustedRadius, cy);
		g.lineTo(cx, w - adjustedRadius);
		if (fill)
			fill.end(g);
	}
}

}