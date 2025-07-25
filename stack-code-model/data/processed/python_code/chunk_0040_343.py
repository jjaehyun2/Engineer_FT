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
import flash.display.Graphics;
import mx.skins.Border;
import mx.styles.StyleManager;
import mx.utils.ColorUtil;

/**
 *  The skin for all the states of the down button in a NumericStepper.
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public class NumericStepperDownSkin extends Border
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
											  fillColor0:uint,
											  fillColor1:uint):Object
	{
		var key:String = HaloColors.getCacheKey(themeColor, borderColor,
												fillColor0, fillColor1);
		
		if (!cache[key])
		{
			var o:Object = cache[key] = {};
			
			// Cross-component styles.
			HaloColors.addHaloColors(o, themeColor, fillColor0, fillColor1);
			
			// NumericStepper-specific styles.
			o.borderColorDrk1 = ColorUtil.adjustBrightness2(borderColor, -50);
			o.borderColorDrk2 = ColorUtil.adjustBrightness2(borderColor, -25);			
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
	public function NumericStepperDownSkin()
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
		return 19;
	}

	//----------------------------------
	//  measuredHeight
	//----------------------------------

	/**
	 *  @private
	 */
	override public function get measuredHeight():Number
	{
		return 11;
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
		var arrowColor:uint = getStyle("iconColor");
		var borderColor:uint = getStyle("borderColor");
		var cornerRadius:Number = getStyle("cornerRadius");
		var fillAlphas:Array = getStyle("fillAlphas");
		var fillColors:Array = getStyle("fillColors");
        styleManager.getColorNames(fillColors);
		var themeColor:uint = getStyle("themeColor");		
		
		// Derivative styles.
		var derStyles:Object = calcDerivedStyles(themeColor, borderColor,
												 fillColors[0], fillColors[1]);
		
		var cr:Object = { tl: 0, tr: 0, bl: 0, br: cornerRadius };
		var cr1:Object = { tl: 0, tr: 0,
						   bl: 0, br: Math.max(cornerRadius - 1, 0) };

		// Draw the background and border.
		var g:Graphics = graphics;
		
		g.clear();
		
		switch (name)
		{
			case "downArrowUpSkin":
			{
   				var upFillColors:Array = [ fillColors[0], fillColors[1] ];

   				var upFillAlphas:Array = [ fillAlphas[0], fillAlphas[1] ];

				// border
				drawRoundRect(
					0, 0, w, h, cr,
					[ derStyles.borderColorDrk2,
					  derStyles.borderColorDrk1 ], 1,
					verticalGradientMatrix(0, 0, w, h),
					GradientType.LINEAR, null, 
					{ x: 1, y: 0, w: w - 2, h: h - 1, r: cr1 });

				// fill
				drawRoundRect(
					1, 0, w - 2, h - 1, cr1,
					upFillColors, upFillAlphas,
					verticalGradientMatrix(1, 1 - h, w - 2, 2 * h - 2));
				
				break;
			}
			
			case "downArrowOverSkin":
			{
				var overFillColors:Array;
				if (fillColors.length > 2)
					overFillColors = [ fillColors[2], fillColors[3] ];
				else
					overFillColors = [ fillColors[0], fillColors[1] ];

				var overFillAlphas:Array;
				if (fillAlphas.length > 2)
					overFillAlphas = [ fillAlphas[2], fillAlphas[3] ];
  				else
					overFillAlphas = [ fillAlphas[0], fillAlphas[1] ];

				// border
				drawRoundRect(
					0, 0, w, h, cr,
					[ derStyles.themeColDrk2, derStyles.themeColDrk1 ], 1,
					verticalGradientMatrix(0, 0, w, h),
					GradientType.LINEAR, null, 
                    { x: 1, y: 0, w: w - 2, h: h - 1, r: cr1 }); 
					
				// fill
				drawRoundRect(
					1, 0, w - 2, h - 1, cr1,
					overFillColors, overFillAlphas,
					verticalGradientMatrix(1, 1 - h, w - 2, 2 * h - 2)); 
				
				break;
			}
			
			case "downArrowDownSkin":
			{
				// border
				drawRoundRect(
					0, 0, w, h, cr,
					[ derStyles.themeColDrk2, derStyles.themeColDrk1 ], 1,
					verticalGradientMatrix(0, 0, w, h)); 
				
				// fill
				drawRoundRect(
					1, 0, w - 2, h - 1, cr1,
					[ derStyles.fillColorPress1, derStyles.fillColorPress2 ], 1,
					verticalGradientMatrix(1, 1 - h, w - 2, 2 * h - 2));
				
				break;
			}
			
			case "downArrowDisabledSkin":
			{
   				var disFillColors:Array = [ fillColors[0], fillColors[1] ];
   				
				var disFillAlphas:Array =
					[ Math.max( 0, fillAlphas[0] - 0.15),
					  Math.max( 0, fillAlphas[1] - 0.15) ];

				// border
				drawRoundRect(
					0, 0, w, h, cr,
					[ derStyles.borderColorDrk2,
					  derStyles.borderColorDrk1 ], 0.5,
					verticalGradientMatrix(0, 0, w, h),
					GradientType.LINEAR, null, 
					{ x: 1, y: 0, w: w - 2, h: h - 1, r: cr1 }); 

				// fill
				drawRoundRect(
					1, 0, w - 2, h - 1, cr1,
					disFillColors, disFillAlphas,
					verticalGradientMatrix(1, 1 - h, w - 2, 2 * h - 2)); 
				
				arrowColor = getStyle("disabledIconColor");
				break;
			}
		}

		// Draw the arrow.
		g.beginFill(arrowColor);
		g.moveTo(w / 2, h / 2 + 1.5);
		g.lineTo(w / 2 - 3.5, h / 2 - 2.5);
		g.lineTo(w / 2 + 3.5, h / 2 - 2.5);
		g.lineTo(w / 2, h / 2 + 1.5);
		g.endFill();
	}
}

}