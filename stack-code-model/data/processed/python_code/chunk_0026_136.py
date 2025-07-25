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

package mx.skins.halo
{

import flash.display.GradientType;
import mx.core.EdgeMetrics;
import mx.skins.Border;
import mx.styles.StyleManager;
import mx.utils.ColorUtil;

/**
 *  The skin for all the states of an AccordionHeader in an Accordion.
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public class AccordionHeaderSkin extends Border
{
	include "../../core/Version.as";

	//--------------------------------------------------------------------------
	//
	//  Class variables
	//
	//--------------------------------------------------------------------------

	/**
	 *  @private
	 */
	private static var cache:Object = {};
	
	//--------------------------------------------------------------------------
	//
	//  Class methods
	//
	//--------------------------------------------------------------------------

	/**
	 *  @private
	 *  Several colors used for drawing are calculated from the base colors
	 *  of the component (themeColor, borderColor and fillColors).
	 *  Since these calculations can be a bit expensive,
	 *  we calculate once per color set and cache the results.
	 */
	private static function calcDerivedStyles(themeColor:uint,
											  borderColor:uint,
											  falseFillColor0:uint,
											  falseFillColor1:uint,
											  fillColor0:uint,
											  fillColor1:uint):Object
	{
		var key:String = HaloColors.getCacheKey(themeColor, borderColor,
												falseFillColor0,
												falseFillColor1,
												fillColor0, fillColor1);
		
		if (!cache[key])
		{
			var o:Object = cache[key] = {};
			
			// Cross-component styles.
			HaloColors.addHaloColors(o, themeColor, fillColor0, fillColor1);
			
		}
		
		return cache[key];
	}

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
	public function AccordionHeaderSkin()
	{
		super();
	}
	
	//--------------------------------------------------------------------------
	//
	//  Overridden properties
	//
	//--------------------------------------------------------------------------

	//----------------------------------
	//  measuredWidth
	//----------------------------------
	
	/**
	 *  @private
	 */
	override public function get measuredWidth():Number
	{
		return 10;
	}
	
	//----------------------------------
	//  measuredHeight
	//----------------------------------

	/**
	 *  @private
	 */
	override public function get measuredHeight():Number
	{
		return 22;
	}

	//--------------------------------------------------------------------------
	//
	//  Overridden methods
	//
	//--------------------------------------------------------------------------

	/**
	 *  @private
	 */
	override protected function updateDisplayList(w:Number, h:Number):void
	{
		super.updateDisplayList(w, h);

		// User-defined styles.
		var borderColor:uint = getStyle("borderColor");
		var fillAlphas:Array = getStyle("fillAlphas");
		var fillColors:Array = getStyle("fillColors");
        styleManager.getColorNames(fillColors);
		var highlightAlphas:Array = getStyle("highlightAlphas");		
		var selectedFillColors:Array = getStyle("selectedFillColors");
		var themeColor:uint = getStyle("themeColor");
		
		// Placehold styles stub.
		var falseFillColors:Array /* of Color */ = []; // added style prop
		falseFillColors[0] = ColorUtil.adjustBrightness2(fillColors[0], -8);
		falseFillColors[1] = ColorUtil.adjustBrightness2(fillColors[1], -10);	
		
		var borderColorDrk1:Number =
			ColorUtil.adjustBrightness2(borderColor, -15);
			
		var overFillColor1:Number =
				ColorUtil.adjustBrightness2(fillColors[0], -4);
		var overFillColor2:Number =
				ColorUtil.adjustBrightness2(fillColors[1], -6);
		
		if (!selectedFillColors)
		{
			selectedFillColors = []; // So we don't clobber the original...
			selectedFillColors[0] =
				ColorUtil.adjustBrightness2(fillColors[0], 5);
			selectedFillColors[1] =
				ColorUtil.adjustBrightness2(fillColors[1], 15);
		}
		
		// Derivative styles.
		var derStyles:Object = calcDerivedStyles(themeColor, borderColor,
												 falseFillColors[0],
												 falseFillColors[1],
												 fillColors[0], fillColors[1]);
		
		graphics.clear();

		switch (name)
		{
			case "upSkin":
			case "disabledSkin":
			case "selectedDisabledSkin":
			{
   				var upFillColors:Array =
					[ falseFillColors[0], falseFillColors[1] ];
   				var upFillAlphas:Array = [ fillAlphas[0], fillAlphas[1] ];

				// edge 
				drawRoundRect(
					0, 0, w, h, 0,
					[ borderColor, borderColorDrk1 ], 1,
					verticalGradientMatrix(0, 0, w, h),
					GradientType.LINEAR, null,
                    { x: 1, y: 1, w: w - 2, h: h - 2, r: 0 });

				// fill 
				drawRoundRect(
					1, 1,w - 2, h - 2, 0,
					upFillColors, upFillAlphas,
					verticalGradientMatrix(1, 1, w - 2, h - 2));
				
				// top highlight
				drawRoundRect(
					1, 1, w - 2, (h - 2) / 2, 0,
					[ 0xFFFFFF, 0xFFFFFF ], highlightAlphas,
					verticalGradientMatrix(1, 1, w - 2, (h - 2) / 2)); 

				// bottom edge bevel shadow
				drawRoundRect(
					1, h - 2, w - 2, 1, 0,
					borderColor, 0.1);
				
				break;
			}
						
			case "overSkin":
			{
				var overFillColors:Array;
				if (fillColors.length > 2)
				{
					overFillColors =
					[
						ColorUtil.adjustBrightness2(fillColors[2], -4), 
						ColorUtil.adjustBrightness2(fillColors[3], -6)
					];
				}
				else
				{
					overFillColors = [ overFillColor1, overFillColor2 ];
				}

				var overFillAlphas:Array;
				if (fillAlphas.length > 2)
					overFillAlphas = [ fillAlphas[2], fillAlphas[3] ];
  				else
					overFillAlphas = [ fillAlphas[0], fillAlphas[1] ];

				// edge
				drawRoundRect(
					0, 0, w, h, 0,
					[ themeColor, derStyles.themeColDrk1 ], 1,
					verticalGradientMatrix(0, 0, w, h),
					GradientType.LINEAR, null,
					{ x: 1, y: 1, w: w - 2, h: h - 2, r: 0 });
				
				// fill
				drawRoundRect(
					1, 1, w - 2, h - 2, 0,
					overFillColors, overFillAlphas,
					verticalGradientMatrix(1, 1, w - 2, h - 2));

				// top highlight
				drawRoundRect(
					1, 1, w - 2, (h - 2) / 2, 0,
					[ 0xFFFFFF, 0xFFFFFF ], highlightAlphas,
					verticalGradientMatrix(1, 1, w - 2, (h - 2) / 2)); 

				// bottom edge bevel shadow
				drawRoundRect(
					1, h - 2, w - 2, 1, 0,
					borderColor, 0.1);
				
				break;
			}
						
			case "downSkin":
			{
				// edge 
				drawRoundRect(
					0, 0, w, h, 0,
					[ themeColor, derStyles.themeColDrk1 ], 1,
					verticalGradientMatrix(0, 0, w, h));
				
				// fill
				drawRoundRect(
					1, 1, w - 2, h - 2, 0,
					[ derStyles.fillColorPress1, derStyles.fillColorPress2 ], 1,
					verticalGradientMatrix(1, 1, w - 2, h - 2));
				
				// top highlight
				drawRoundRect(
					1, 1, w - 2, (h - 2) / 2, 0,
					[ 0xFFFFFF, 0xFFFFFF ], highlightAlphas,
					verticalGradientMatrix(1, 1, w - 2, (h - 2) / 2));

				break;
			}
						
			case "selectedUpSkin":
			case "selectedOverSkin":
			case "selectedDownSkin":
			{
   				var selectedFillAlphas:Array = [ fillAlphas[0], fillAlphas[1] ];

				// edge 
				drawRoundRect(
					0, 0, w, h, 0, 
					[ borderColor, borderColorDrk1 ], 1,
					verticalGradientMatrix(0, 0, w, h),
					GradientType.LINEAR, null,
                    { x: 1, y: 1, w: w - 2, h: h - 2, r: 0 })
				
				// fill
				drawRoundRect(
					1, 1, w - 2, h - 2, 0,
					[ selectedFillColors[0],
					  selectedFillColors[1] ], selectedFillAlphas,
					verticalGradientMatrix(1, 1, w - 2, h - 2));

				// top highlight
				drawRoundRect(
					1, 1, w - 2, (h - 2) / 2, 0,
					[ 0xFFFFFF, 0xFFFFFF ], highlightAlphas,
					verticalGradientMatrix(1, 1, w - 2, (h - 2) / 2)); 

				// bottom edge highlight
				drawRoundRect(
					1, h - 2, w - 2, 1, 0,
					borderColor, 0.05);

				break;
			}
		}
	}
}

}