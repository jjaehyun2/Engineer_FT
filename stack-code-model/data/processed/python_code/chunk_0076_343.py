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

package mx.controls.sliderClasses
{

import flash.events.KeyboardEvent;
import flash.events.MouseEvent;
import flash.geom.Point;
import flash.ui.Keyboard;
import mx.controls.Button;
import mx.controls.ButtonPhase;
import mx.core.FlexVersion;
import mx.core.mx_internal;
import mx.events.SliderEvent;
import mx.managers.ISystemManager;

use namespace mx_internal;

/**
 *  The SliderThumb class represents a thumb of a Slider control.
 *  The SliderThumb class can only be used within the context
 *  of a Slider control.
 *  You can create a subclass of the SliderThumb class,
 *  and use it with a Slider control by setting the 
 *  <code>sliderThumbClass</code>
 *  property of the Slider control to your subclass. 
 *  		
 *  @see mx.controls.HSlider
 *  @see mx.controls.VSlider
 *  @see mx.controls.sliderClasses.Slider
 *  @see mx.controls.sliderClasses.SliderDataTip
 *  @see mx.controls.sliderClasses.SliderLabel
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public class SliderThumb extends Button
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
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function SliderThumb()
	{
		super();

		stickyHighlighting = true;
	}
	
	//--------------------------------------------------------------------------
	//
	//  Variables
	//
	//--------------------------------------------------------------------------

	/** 
	 *  @private
	 *  The zero-based index number of this thumb. 
	 */
	mx_internal var thumbIndex:int;

	/**
	 *  @private
	 *  x-position offset.
	 */
	private var xOffset:Number;
	
	//--------------------------------------------------------------------------
	//
	//  Overridden properties
	//
	//--------------------------------------------------------------------------

	//----------------------------------
	//  x
	//----------------------------------

	/**
	 *  @private
	 *  Handle changes to the x-position value of the thumb.
	 */
	override public function set x(value:Number):void
	{
		var result:Number = moveXPos(value);
		
		updateValue();
		
		super.x = result;
	}
	
	//--------------------------------------------------------------------------
	//
	//  Properties
	//
	//--------------------------------------------------------------------------

	//----------------------------------
	//  xPosition
	//----------------------------------

	/**
	 *  Specifies the position of the center of the thumb on the x-axis.
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function get xPosition():Number
	{
		return $x + width / 2;
	}
	
	/**
	 *  @private
	 */
	public function set xPosition(value:Number):void
	{
		$x = value - width / 2;
		
		Slider(owner).drawTrackHighlight();
	}
	
	//--------------------------------------------------------------------------
	//
	//  Overridden methods: UIComponent
	//
	//--------------------------------------------------------------------------
	
	/**
	 *  @private
	 */
	override protected function measure():void
	{
		super.measure();

		if (FlexVersion.compatibilityVersion < FlexVersion.VERSION_4_0)
		{
			measuredWidth = 12;
			measuredHeight = 12;
		}
	}
	
	/**
	 *  @private
	 */
	override public function drawFocus(isFocused:Boolean):void
	{
		phase =  isFocused ? ButtonPhase.DOWN : ButtonPhase.UP;
	}
	
	//--------------------------------------------------------------------------
	//
	//  Overridden methods: Button
	//
	//--------------------------------------------------------------------------

	/**
	 *  @private
	 */
	override mx_internal function buttonReleased():void
	{
		super.buttonReleased();
		
		if (enabled)
		{
			systemManager.getSandboxRoot().removeEventListener(
				MouseEvent.MOUSE_MOVE, mouseMoveHandler, true);
            systemManager.deployMouseShields(false);
            
			Slider(owner).onThumbRelease(this);
		}
	}

	//--------------------------------------------------------------------------
	//
	//  Methods
	//
	//--------------------------------------------------------------------------

	/**
	 *  @private
	 *  Move the thumb into the correct position.
	 */
	private function moveXPos(value:Number, 
                              overrideSnap:Boolean = false, 
                              noUpdate:Boolean = false):Number
	{
		var result:Number = calculateXPos(value, overrideSnap);
		
		xPosition = result;
		
		if (!noUpdate) 
			updateValue();
		
		return result;
	}
	
	/**
	 *  @private
	 *  Ask the Slider if we should be moving into a snap position 
	 *  and make sure we haven't exceeded the min or max position
	 */
	private function calculateXPos(value:Number,
								   overrideSnap:Boolean = false):Number
	{
		var bounds:Object = Slider(owner).getXBounds(thumbIndex);
		
		var result:Number = Math.min(Math.max(value, bounds.min), bounds.max);

		if (!overrideSnap)
			result = Slider(owner).getSnapValue(result, this);	
		
		return result;
	}
	
	/**
	 *	@private
	 *	Used by the Slider for animating the sliding of the thumb.
	 */
	mx_internal function onTweenUpdate(value:Number):void
	{
		moveXPos(value, true, true);
	}
	
	/**
	 *	@private
	 *	Used by the Slider for animating the sliding of the thumb.
	 */
	mx_internal function onTweenEnd(value:Number):void
	{
		moveXPos(value);
	}
	
	/**
	 *  @private
	 *  Tells the Slider to update its value for the thumb based on the thumb's
	 *  current position
	 */
	private function updateValue():void
	{
		Slider(owner).updateThumbValue(thumbIndex);
	}

	//--------------------------------------------------------------------------
	//
	//  Overridden event handlers: UIComponent
	//
	//--------------------------------------------------------------------------

	/**
	 *  @private
	 *  Handle key presses when focus is on the thumb.
	 */
	override protected function keyDownHandler(event:KeyboardEvent):void
	{
		var multiThumbs:Boolean = Slider(owner).thumbCount > 1;
		var currentVal:Number = xPosition;
		var moveInterval:Number = Slider(owner).snapInterval > 0 ?
								  Slider(owner).getSnapIntervalWidth() :
								  1;
		var isHorizontal:Boolean =
			Slider(owner).direction == SliderDirection.HORIZONTAL;
		
		var newVal:Number;
        
        // If rtl layout, need to swap LEFT and RIGHT so correct action
        // is done.
        var keyCode:uint = mapKeycodeForLayoutDirection(event);
        
		if ((keyCode == Keyboard.DOWN && !isHorizontal) ||
			(keyCode == Keyboard.LEFT && isHorizontal))
		{
			newVal = currentVal - moveInterval;
		}
		else if ((keyCode == Keyboard.UP && !isHorizontal) ||
				 (keyCode == Keyboard.RIGHT && isHorizontal))
		{
			newVal = currentVal + moveInterval;
		}
		else if ((keyCode == Keyboard.PAGE_DOWN && !isHorizontal) ||
				 (keyCode == Keyboard.HOME && isHorizontal))
		{
			newVal = Slider(owner).getXFromValue(Slider(owner).minimum);
		}
		else if ((keyCode == Keyboard.PAGE_UP && !isHorizontal) ||
				 (keyCode == Keyboard.END && isHorizontal))
		{
			newVal = Slider(owner).getXFromValue(Slider(owner).maximum);
		}
		
		if (!isNaN(newVal))
		{
			event.stopPropagation();
			//mark last interaction as key 
			Slider(owner).keyInteraction = true;
			moveXPos(newVal);
		}
	}

	//--------------------------------------------------------------------------
	//
	//  Overridden event handlers: Button
	//
	//--------------------------------------------------------------------------
	
	/**
	 *  @private
	 */
	override protected function mouseDownHandler(event:MouseEvent):void
	{
		super.mouseDownHandler(event);

		if (enabled)
		{
			// Store where the mouse is positioned
			// relative to the thumb when first pressed.
			xOffset = event.localX; 
			
			systemManager.getSandboxRoot().addEventListener(
				MouseEvent.MOUSE_MOVE, mouseMoveHandler, true);
			systemManager.deployMouseShields(true);
			
			Slider(owner).onThumbPress(this);
		}
	}
	//--------------------------------------------------------------------------
	//
	//  Event handlers
	//
	//--------------------------------------------------------------------------

	/**
	 *  @private
	 *  Internal function to handle mouse movements
	 *  when the thumb is in a pressed state
	 *  We want the thumb to follow the x-position of the mouse. 
	 */
	private function mouseMoveHandler(event:MouseEvent):void
	{
		if (enabled)
		{
			var pt:Point = new Point(event.stageX, event.stageY);
			pt = Slider(owner).innerSlider.globalToLocal(pt);
			
			// Place the thumb in the correct position.
			moveXPos(pt.x - xOffset + width / 2, false, true);
			
			// Callback to the Slider to handle tooltips and update its value.
			Slider(owner).onThumbMove(this);
		}
	}
}

}