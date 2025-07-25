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

package spark.accessibility
{

import flash.accessibility.Accessibility;
import flash.events.Event;

import mx.accessibility.AccConst;
import mx.core.UIComponent;
import mx.core.mx_internal;

import spark.components.TabBar;

use namespace mx_internal;

/**
 *  TabBarAccImpl is the accessibility implementation class
 *  for spark.components.TabBar.
 *
 *  <p>When a Spark TabBar is created,
 *  its <code>accessibilityImplementation</code> property
 *  is set to an instance of this class.
 *  The Flash Player then uses this class to allow MSAA clients
 *  such as screen readers to see and manipulate the TabBar.
 *  See the mx.accessibility.AccImpl and
 *  flash.accessibility.AccessibilityImplementation classes
 *  for background information about accessibility implementation
 *  classes and MSAA.</p>
 *
 *  <p><b>Children</b></p>
 *
 *  <p>The MSAA children of a TabBar are its tabs.
 *  As described above, the accessibility of these tabs is managed
 *  by the TabBar; their own <code>accessibilityImplementation</code> and
 *  <code>accessibilityProperties</code> are ignored by the Flash Player.</p>
 *
 *  <p><b>Role</b></p>
 *
 *  <p>The MSAA Role of a TabBar is ROLE_SYSTEM_PAGETABLIST.</p>
 *
 *  <p>The Role of each tab is ROLE_SYSTEM_PAGETAB.</p>
 *
 *  <p><b>Name</b></p>
 *
 *  <p>The MSAA Name of a TabBar is, by default, an empty string.
 *  When wrapped in a FormItem element, the Name is the FormItem's label.
 *  To override this behavior, set the TabBar's
 *  <code>accessibilityName</code> property.</p>
 *
 *  <p>The Name of each tab is determined by the TabBar's
 *  <code>itemToLabel()</code> method.</p>
 *
 *  <p>When the Name of the TabBar or one of its tabs changes,
 *  a TabBar dispatches the MSAA event EVENT_OBJECT_NAMECHANGE
 *  with the proper childID for the tab or 0 for itself.</p>
 *
 *  <p><b>Description</b></p>
 *
 *  <p>The MSAA Description of a TabBar is, by default, an empty string,
 *  but you can set the TabBar's <code>accessibilityDescription</code>
 *  property.</p>
 *
 *  <p>The Description of each tab is the empty string.</p>
 *
 *  <p><b>State</b></p>
 *
 *  <p>The MSAA State of a TabBar is a combination of:
 *  <ul>
 *    <li>STATE_SYSTEM_UNAVAILABLE (when enabled is false)</li>
 *    <li>STATE_SYSTEM_FOCUSABLE (when enabled is true)</li>
 *    <li>STATE_SYSTEM_FOCUSED
 *    (when enabled is true and the TabBar has focus)</li>
 *  </ul></p>
 *
 *  <p>The State of a tab in a TabBar is a combination of:
 *  <ul>
 *    <li>STATE_SYSTEM_FOCUSED</li>
 *    <li>STATE_SYSTEM_PRESSED</li>
 *  </ul></p>
 *
 *  <p>When the State of the TabBar or one of its tabs changes,
 *  a TabBar dispatches the MSAA event EVENT_OBJECT_STATECHANGE
 *  with the proper childID for the tab or 0 for itself.</p>
 *
 *  <p><b>Value</b></p>
 *
 *  <p>A TabBar, or a tab in a TabBar, does not have an MSAA Value.</p>
 *
 *  <p><b>Location</b></p>
 *
 *  <p>The MSAA Location of a TabBar, or a tab in a TabBar,
 *  is its bounding rectangle.</p>
 *
 *  <p><b>Default Action</b></p>
 *
 *  <p>A TabBar does not have an MSAA DefaultAction.</p>
 *
 *  <p>The DefaultAction of a tab in a TabBar is "Switch".
 *  When it is performed, the given tab is pressed.</p>
 *
 *  <p><b>Focus</b></p>
 *
 *  <p>Both the TabBar and its individual tabs accept focus.
 *  When they do so it dispatches the MSAA event EVENT_OBJECT_FOCUS.
 *  A tab is not automatically pressed
 *  when focused through arrow key navigation.
 *  To press a focused tab, the user must press the spacebar.</p>
 *
 *  <p><b>Selection</b></p>
 *
 *  <p>MSAA Selection will press the tab
 *  corresponding to the specified childID.
 *  Only one tab can be pressed at a time.</p>
 *
 *  @langversion 3.0
 *  @playerversion Flash 10
 *  @playerversion AIR 1.5
 *  @productversion Flex 4
 */
public class TabBarAccImpl extends ButtonBarBaseAccImpl
{
    include "../core/Version.as";
    
    //--------------------------------------------------------------------------
    //
    //  Class methods
    //
    //--------------------------------------------------------------------------
    
    /**
     *  Enables accessibility in the TabBar class.
     *
     *  <p>This method is called by application startup code
     *  that is autogenerated by the MXML compiler.
     *  Afterwards, when instances of TabBar are initialized,
     *  their <code>accessibilityImplementation</code> property
     *  will be set to an instance of this class.</p>
     *
     *  @langversion 3.0
     *  @playerversion Flash 10
     *  @playerversion AIR 1.5
     *  @productversion Flex 4
     */
    public static function enableAccessibility():void
    {
        TabBar.createAccessibilityImplementation =
            createAccessibilityImplementation;
    }
    
    /**
     *  @private
     *  Creates a TabBar's AccessibilityImplementation object.
     *  This method is called from UIComponent's
     *  initializeAccessibility() method.
     */
    mx_internal static function createAccessibilityImplementation(
        component:UIComponent):void
    {
        component.accessibilityImplementation =
            new TabBarAccImpl(component);
    }
    
    //--------------------------------------------------------------------------
    //
    //  Constructor
    //
    //--------------------------------------------------------------------------
    
    /**
     *  Constructor.
     *
     *  @param master The UIComponent instance that this AccImpl instance
     *  is making accessible.
     *
     *  @langversion 3.0
     *  @playerversion Flash 10
     *  @playerversion AIR 1.5
     *  @productversion Flex 4
     */
    public function TabBarAccImpl(master:UIComponent)
    {
        super(master);
        role = AccConst.ROLE_SYSTEM_PAGETABLIST;
    }
    
    //--------------------------------------------------------------------------
    //
    //  Overridden methods: AccessibilityImplementation
    //
    //--------------------------------------------------------------------------
    
    /**
     *  @private
     *  Gets the role for the component.
     *
     *  @param childID children of the component
     */
    override public function get_accRole(childID:uint):uint
    {
        return childID == 0 ? role : AccConst.ROLE_SYSTEM_PAGETAB;
    }
    
    /**
     *  @private
     *  IAccessible method for returning the Default Action.
     *
     *  @param childID uint
     *
     *  @return DefaultAction String
     */
    override public function get_accDefaultAction(childID:uint):String
    {
        if (childID == 0)
            return null;
        
        return "Switch";
    }
}

}