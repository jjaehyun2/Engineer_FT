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

package mx.controls
{

import flash.ui.Keyboard;
import mx.controls.scrollClasses.ScrollBar;
import mx.controls.scrollClasses.ScrollBarDirection;
import mx.core.mx_internal;
import mx.events.ScrollEvent;

use namespace mx_internal;

//--------------------------------------
//  Events
//--------------------------------------

/**
 *  Dispatched when the ScrollBar control scrolls through
 *  user initiated action or programmatically. 
 *
 *  @eventType mx.events.ScrollEvent.SCROLL
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Event(name="scroll", type="mx.events.ScrollEvent")]

//--------------------------------------
//  Styles
//--------------------------------------

/**
 *  Number of milliseconds to wait after the first <code>buttonDown</code>
 *  event before repeating <code>buttonDown</code> events at the
 *  <code>repeatInterval</code>.
 *  The default value is 500.
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Style(name="repeatDelay", type="Number", format="Time", inherit="no")]

/**
 *  Number of milliseconds between <code>buttonDown</code> events
 *  if the user presses and holds the mouse on a button.
 *  The default value is 35.
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Style(name="repeatInterval", type="Number", format="Time", inherit="no")]

//--------------------------------------
//  Excluded APIs
//--------------------------------------

[Exclude(name="direction", kind="property")]

//--------------------------------------
//  Other metadata
//--------------------------------------

[DefaultBindingProperty(source="scrollPosition", destination="scrollPosition")]

[DefaultTriggerEvent("scroll")]

[IconFile("VScrollBar.png")]

[Alternative(replacement="spark.components.VScrollBar", since="4.0")]

/**
 *  The VScrollBar (vertical ScrollBar) control  lets you control
 *  the portion of data that is displayed when there is too much data
 *  to fit in a display area.
 * 
 *  This control extends the base ScrollBar control. 
 *  
 *  <p>Although you can use the VScrollBar control as a stand-alone control,
 *  you usually combine it as part of another group of components to
 *  provide scrolling functionality.</p>
 *  
 *  <p>A ScrollBar control consist of four parts: two arrow buttons,
 *  a track, and a thumb. 
 *  The position of the thumb and the display of the arrow buttons
 *  depend on the current state of the ScrollBar control.
 *  The ScrollBar control uses four parameters to calculate its 
 *  display state:</p>
 *
 *  <ul>
 *    <li>Minimum range value</li>
 *    <li>Maximum range value</li>
 *    <li>Current position - must be within the
 *    minimum and maximum range values</li>
 *    <li>Viewport size - represents the number of items
 *    in the range that you can display at one time. The
 *    number of items must be less than or equal to the 
 *    range, where the range is the set of values between
 *    the minimum range value and the maximum range value.</li>
 *  </ul>
 *  
 *  @mxml
 *  
 *  <p>The <code>&lt;mx:VScrollBar&gt;</code> tag inherits all the
 *  tag attributes of its superclass, and adds the following tag attributes:</p>
 *  
 *  <pre>
 *  &lt;mx:VScrollBar
 *    <strong>Styles</strong>
 *    repeatDelay="500"
 *    repeatInterval="35"
 * 
 *    <strong>Events</strong>
 *    scroll="<i>No default</i>"
 *  /&gt;
 *  </pre>
 *  
 *  @includeExample examples/VScrollBarExample.mxml
 *
 *  @see mx.controls.scrollClasses.ScrollBar
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public class VScrollBar extends ScrollBar
{
    include "../core/Version.as";

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
    public function VScrollBar()
    {
        super();

        // ScrollBar variables.
        super.direction = ScrollBarDirection.VERTICAL;
    }

    //--------------------------------------------------------------------------
    //
    //  Overridden properties
    //
    //--------------------------------------------------------------------------

    //----------------------------------
    //  direction
    //----------------------------------
    
    [Inspectable(environment="none")]   

    /**
     *  @private
     *  Don't allow user to change the direction.
     */
    override public function set direction(value:String):void
    {
    }

    //----------------------------------
    //  minWidth
    //----------------------------------

    /**
     *  @private
     */
    override public function get minWidth():Number
    {
        return _minWidth;
    }

    //----------------------------------
    //  minHeight
    //----------------------------------

    /**
     *  @private
     */
    override public function get minHeight():Number
    {
        return _minHeight;
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

        measuredWidth = _minWidth;
        measuredHeight = _minHeight;
    }

    //--------------------------------------------------------------------------
    //
    //  Overridden methods: ScrollBar
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     *  Map keys to scroll events.
     */
    override mx_internal function isScrollBarKey(key:uint):Boolean
    {
        if (key == Keyboard.UP)
        {
            lineScroll(-1);
            return true;
        }

        else if (key == Keyboard.DOWN)
        {
            lineScroll(1);
            return true;
        }

        else if (key == Keyboard.PAGE_UP)
        {
            pageScroll(-1);
            return true;
        }

        else if (key == Keyboard.PAGE_DOWN)
        {
            pageScroll(1);
            return true;
        }

        return super.isScrollBarKey(key);
    }
}

}