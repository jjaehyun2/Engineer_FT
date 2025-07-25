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

import flash.display.DisplayObject;
import flash.display.Graphics;
import flash.display.InteractiveObject;
import flash.display.Shape;
import flash.display.Sprite;
import flash.events.Event;
import mx.core.FlexShape;
import mx.core.FlexSprite;
import mx.styles.CSSStyleDeclaration;
import mx.styles.IStyleManager2;
import mx.styles.StyleManager;

/**
 *  Defines the appearance of the cursor that appears while an operation is taking place. For example, 
 *  while the SWFLoader class loads an asset.
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public class BusyCursor extends FlexSprite
{
	include "../../core/Version.as";

	//--------------------------------------------------------------------------
	//
	//  Constructor
	//
	//--------------------------------------------------------------------------

	/**
	 *  Constructor.
	 *  
     *  @param styleManager - The style manager associated with the object creating
     *  the cursor. The style manager is used to get the style declaration of the 
     *  cursor manager which determines the class used for the busy cursor. 
     *  If styleManager is null, the top-level style manager will be used.
     * 
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function BusyCursor(styleManager:IStyleManager2 = null)
	{
		super();
		
        if (!styleManager)
            styleManager = StyleManager.getStyleManager(null);
        
		var cursorManagerStyleDeclaration:CSSStyleDeclaration =
			styleManager.getMergedStyleDeclaration("mx.managers.CursorManager");
		
		var cursorClass:Class =
			cursorManagerStyleDeclaration.getStyle("busyCursorBackground");
		
		var cursorHolder:DisplayObject = new cursorClass();
		if (cursorHolder is InteractiveObject)
			InteractiveObject(cursorHolder).mouseEnabled = false;
		addChild(cursorHolder);
		
		var xOff:Number = -0.5;
		var yOff:Number = -0.5;

		var g:Graphics;
		
		// Create the minute hand.
		minuteHand = new FlexShape();
		minuteHand.name = "minuteHand";
		g = minuteHand.graphics;
		g.beginFill(0x000000);
		g.moveTo(xOff, yOff);
		g.lineTo(1 + xOff, 0 + yOff);
		g.lineTo(1 + xOff, 5 + yOff);
		g.lineTo(0 + xOff, 5 + yOff);
		g.lineTo(0 + xOff, 0 + yOff);
		g.endFill();
		addChild(minuteHand);
		
		// Create the hour hand.
		hourHand = new FlexShape();
		hourHand.name = "hourHand";
		g = hourHand.graphics;
		g.beginFill(0x000000);
		g.moveTo(xOff, yOff);
		g.lineTo(4 + xOff, 0 + yOff);
		g.lineTo(4 + xOff, 1 + yOff);
		g.lineTo(0 + xOff, 1 + yOff);
		g.lineTo(0 + xOff, 0 + yOff);
		g.endFill();
		addChild(hourHand);
		
		addEventListener(Event.ADDED, handleAdded);
		addEventListener(Event.REMOVED, handleRemoved);
	}

	//--------------------------------------------------------------------------
	//
	//  Variables
	//
	//--------------------------------------------------------------------------

	/**
	 *  @private
	 */
	private var minuteHand:Shape;

	/**
	 *  @private
	 */
	private var hourHand:Shape;
	
	//--------------------------------------------------------------------------
	//
	//  Event Handlers
	//
	//--------------------------------------------------------------------------
	private function handleAdded(event:Event):void
	{
		addEventListener(Event.ENTER_FRAME, enterFrameHandler);
	}

	private function handleRemoved(event:Event):void
	{
		removeEventListener(Event.ENTER_FRAME, enterFrameHandler);
	}

	/**
	 *  @private
	 */
	private function enterFrameHandler(event:Event):void
	{
		minuteHand.rotation += 12;
		hourHand.rotation += 1;
	}
}

}