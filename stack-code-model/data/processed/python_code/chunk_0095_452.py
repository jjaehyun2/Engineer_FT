////////////////////////////////////////////////////////////////////////////////
//
//  ADOBE SYSTEMS INCORPORATED
//  Copyright 2003-2007 Adobe Systems Incorporated
//  All Rights Reserved.
//
//  NOTICE: Adobe permits you to use, modify, and distribute this file
//  in accordance with the terms of the license agreement accompanying it.
//
////////////////////////////////////////////////////////////////////////////////

package org.lala.components.skins
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
	//  Overridden methods
	//
	//--------------------------------------------------------------------------

	/**
	 *  @private
	 */
	override protected function updateDisplayList(w:Number, h:Number):void
	{
		//super.updateDisplayList(w, h);

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
					0, 0, w, h, 0, //X,Y,Width,Height,圆角
					0xDDDDDD, 1);

				// fill 
				drawRoundRect(
					1, 1,w - 2, h - 2, 0,
					0xFFFFFF, 1);
				/***				
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
***/				
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
					 0xDDDDDD, 1);
				
				// fill
				drawRoundRect(
					1, 1, w - 2, h - 2, 0,
					0xEEEEEE, 1);
/***
				// top highlight
				drawRoundRect(
					1, 1, w - 2, (h - 2) / 2, 0,
					[ 0xFFFFFF, 0xFFFFFF ], highlightAlphas,
					verticalGradientMatrix(1, 1, w - 2, (h - 2) / 2)); 

				// bottom edge bevel shadow
				drawRoundRect(
					1, h - 2, w - 2, 1, 0,
					borderColor, 0.1);
***/				
				break;
			}
						
			case "downSkin":
			{
				// edge 
				drawRoundRect(
					0, 0, w, h, 0,
					0xDDDDDD, 1);
				
				// fill
				drawRoundRect(
					1, 1, w - 2, h - 2, 0,
					0x0099FF, 1);
/***				
				// top highlight
				drawRoundRect(
					1, 1, w - 2, (h - 2) / 2, 0,
					[ 0xFFFFFF, 0xFFFFFF ], highlightAlphas,
					verticalGradientMatrix(1, 1, w - 2, (h - 2) / 2));
***/
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
					0xDDDDDD, 1);
				
				// fill
				drawRoundRect(
					1, 1, w - 2, h - 2, 0,
					 0XFFFFFF, 1);
/***
				// top highlight
				drawRoundRect(
					1, 1, w - 2, (h - 2) / 2, 0,
					[ 0xFFFFFF, 0xFFFFFF ], highlightAlphas,
					verticalGradientMatrix(1, 1, w - 2, (h - 2) / 2)); 

				// bottom edge highlight
				drawRoundRect(
					1, h - 2, w - 2, 1, 0,
					borderColor, 0.05);
***/
				break;
			}
		}
	}
}

}