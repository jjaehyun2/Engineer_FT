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

package mx.effects.effectClasses
{

import flash.events.Event;
import mx.core.UIComponent;
import mx.core.mx_internal;
import mx.events.ChildExistenceChangedEvent;
import mx.events.FlexEvent;
import mx.geom.RoundedRectangle;
import mx.styles.StyleManager;

use namespace mx_internal;

/**
 *  The DissolveInstance class implements the instance class
 *  for the Dissolve effect.
 *  Flex creates an instance of this class when it plays a Dissolve effect;
 *  you do not create one yourself.
 *  
 *  <p>Every effect class that is a subclass of the TweenEffect class 
 *  supports the following events:</p>
 *  
 *  <ul>
 *    <li><code>tweenEnd</code>: Dispatched when the tween effect ends. </li>
 *  
 *    <li><code>tweenUpdate</code>: Dispatched every time a TweenEffect 
 *      class calculates a new value.</li> 
 *  </ul>
 *  
 *  <p>The event object passed to the event listener for these events is of type TweenEvent. 
 *  The TweenEvent class  defines the property <code>value</code>, which contains 
 *  the tween value calculated by the effect. 
 *  For the Dissolve effect, 
 *  the <code>TweenEvent.value</code> property contains a Number between the values of the 
 *  <code>Dissolve.alphaFrom</code> and <code>Dissolve.alphaTo</code> properties.</p>
 *
 *  @see mx.effects.Dissolve
 *  @see mx.events.TweenEvent
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */  
public class DissolveInstance extends TweenEffectInstance
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
	 *  @param target The Object to animate with this effect.
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function DissolveInstance(target:Object)
	{
		super(target);
	}

	//--------------------------------------------------------------------------
	//
	//  Variables
	//
	//--------------------------------------------------------------------------

	/**
	 *  @private
	 */
	private var overlay:UIComponent;
	
	//--------------------------------------------------------------------------
	//
	//  Properties
	//
	//--------------------------------------------------------------------------

	//----------------------------------
	//  alphaFrom
	//----------------------------------

	/** 
	 *  Initial transparency level between 0.0 and 1.0,
	 *  where 0.0 means transparent and 1.0 means fully opaque. 
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public var alphaFrom:Number;
	
	//----------------------------------
	//  alphaTo
	//----------------------------------

	/** 
	 *  Final transparency level between 0.0 and 1.0,
	 *  where 0.0 means transparent and 1.0 means fully opaque.
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public var alphaTo:Number;

	//----------------------------------
	//  color
	//----------------------------------

	/** 
	 *  Hex value that represents the color of the floating rectangle 
	 *  that the effect displays over the target object. 
	 *
	 *  The default value is the color specified by the target component's
	 *  <code>backgroundColor</code> style property, or 0xFFFFFF, if 
	 *  <code>backgroundColor</code> is not set.
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public var color:uint = StyleManager.NOT_A_COLOR;
	
	//----------------------------------
	//  persistAfterEnd
	//----------------------------------

	/** 
	 *  @private
	 */
	mx_internal var persistAfterEnd:Boolean = false;

	//----------------------------------
	//  targetArea
	//----------------------------------

	/**
	 *  The area of the target to play the effect upon.
	 *  The dissolve overlay is drawn using this property's dimensions. 
	 *  UIComponents create an overlay over the entire component.
	 *  Containers create an overlay over their content area,
	 *  but not their chrome. 
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public var targetArea:RoundedRectangle;
	
	//--------------------------------------------------------------------------
	//
	//  Overridden methods
	//
	//--------------------------------------------------------------------------

	/**
	 *  @private
	 */
	override public function initEffect(event:Event):void
	{
		super.initEffect(event);

		switch (event.type)
		{	
			case "childrenCreationComplete":
			case FlexEvent.CREATION_COMPLETE:
			case "resizeEnd":
			case FlexEvent.SHOW:
			case Event.ADDED:
			{
				if (isNaN(alphaFrom))
					alphaFrom = 0;
				if (isNaN(alphaTo))
					alphaTo = target.alpha;
				break;
			}
		
			case FlexEvent.HIDE:
			case "resizeStart":
			case Event.REMOVED:
			{
				if (isNaN(alphaFrom))
					alphaFrom = target.alpha;
				if (isNaN(alphaTo))
					alphaTo = 0;
				break;
			}
		}
	}
	
	/**
	 *  @private
	 */
	override public function play():void
	{
		super.play();
		
		var values:PropertyChanges = propertyChanges;

		// If nobody assigned a value, make this a "show" effect.
		if (isNaN(alphaFrom) && isNaN(alphaTo))
		{	
			// If we are in transition mode
			if (values && values.end["alpha"] !== undefined)
			{
				alphaFrom = target.alpha;
				alphaTo = values.end["alpha"];
			}
			else if (values && values.end["visible"] !== undefined)
			{
				alphaFrom = values.start["visible"] ? target.alpha : 0;
				alphaTo = values.end["visible"] ? target.alpha : 0;
			}
			else
			{
				alphaFrom = 0;
				alphaTo = target.alpha;
			}
		}
		else if (isNaN(alphaFrom))
		{
			alphaFrom = (alphaTo == 0) ? target.alpha : 0;
		}
		else if (isNaN(alphaTo))
		{
			if (values && values.end["alpha"] !== undefined)
				alphaTo = values.end["alpha"];
			else
				alphaTo = (alphaFrom == 0) ? target.alpha : 0;	
		}
			
		// If nobody assigned a color, then use the target's background color.
		if (color == StyleManager.NOT_A_COLOR) 
		{
			color = 0xFFFFFF;
			var bgColor:Number = target.getStyle("backgroundColor");
			if (isNaN(bgColor) && target.parent)
			{
				bgColor = target.parent.getStyle("backgroundColor");	
			}
			if (!isNaN(bgColor))
			{
				color = uint(bgColor);
			}
		}
		
		// Capture the target's width and height before creating the overlay.
		// Label is a subclass of UIComponent, so creating an overlay
		// for the label will change the label's width and height.
		var targetWidth:Number = target.width;
		var targetHeight:Number = target.height;

		target.addEventListener(ChildExistenceChangedEvent.OVERLAY_CREATED,
								overlayCreatedHandler);
        
		target.addOverlay(color, targetArea);
		//overlay.cacheAsBitmap = true;
	}
	
	/**
	 *  @private
	 */
	override public function onTweenUpdate(value:Object):void 
	{
		overlay.alpha = Number(value);
	}

	/**
	 *  @private
	 */
	override public function onTweenEnd(value:Object):void
	{				
		super.onTweenEnd(value);
		
		if (!persistAfterEnd)
			target.removeOverlay();
	}

	//--------------------------------------------------------------------------
	//
	//  Event handlers
	//
	//--------------------------------------------------------------------------
	
	/**
	 *	@private
	 */
	private function overlayCreatedHandler(event:ChildExistenceChangedEvent):void
	{
		target.removeEventListener(ChildExistenceChangedEvent.OVERLAY_CREATED,
								   overlayCreatedHandler);
		
		event.stopImmediatePropagation();
								   
		overlay = UIComponent(event.relatedObject);
		
		// Create a tween.
		tween = createTween(this, 1.0 - alphaFrom,
										 1.0 - alphaTo, duration);

		// Set the animation to the initial value before the screen refreshes.
		applyTweenStartValues();
	}

}
}