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

package mx.managers
{

import flash.display.DisplayObject;
import flash.events.IEventDispatcher;
import flash.display.InteractiveObject;
import flash.display.Sprite;
import mx.core.IButton;
import mx.core.IUIComponent;

/**
 *  The IFocusManager interface defines the interface that components must implement 
 *  to manage the focus on components in response to mouse activity or 
 *  keyboard activity (Tab key), and to support a default button.
 *
 *  @see mx.managers.FocusManager
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public interface IFocusManager extends IEventDispatcher
{
    //--------------------------------------------------------------------------
    //
    //  Properties
    //
    //--------------------------------------------------------------------------

    //----------------------------------
    //  defaultButton
    //----------------------------------

    /**
     *  A reference to the original default Button control.
     *  Pressing the Enter key while the focus is on any control 
     *  activates the Button control by dispatching a <code>click</code> event 
     *  on the Button control, just as if it was clicked with the mouse.
     *  The actual default Button control changes if focus is given to another
     *  Button control, but switches back to the original if focus is not
     *  on a button.
     *
     *  <p>This property is managed by Flex containers; do not set it directly
     *  to specify the default button.</p>
     * 
     *  <p>The <code>defaultButton</code> must be of class
     *  <code>mx.controls.Button</code> even though this property
     *  is of type <code>IUIComponent</code>.</p>
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    function get defaultButton():IButton;
    
    /**
     *  @private
     */
    function set defaultButton(value:IButton):void;

    //----------------------------------
    //  defaultButtonEnabled
    //----------------------------------

    /**
     *  A flag that indicates whether the FocusManager should
     *  check for the Enter key being pressed to activate the default button.
     *  TextArea and other components that want to recognize 
     *  the <code>Enter</code> key
     *  set this property to <code>false</code> to disable the Enter
     *  key from dispatching a <code>click</code> event on the
     *  default button, if it exists.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    function get defaultButtonEnabled():Boolean;
    
    /**
     *  @private
     */
    function set defaultButtonEnabled(value:Boolean):void;

    //----------------------------------
    //  focusPane
    //----------------------------------

    /**
     *  A single Sprite that is moved from container to container
     *  as the focus moves to those containers.
     *  The Sprite is used as the parent of the visual indicator
     *  that a component has focus.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    function get focusPane():Sprite;
    
    /**
     *  @private
     */
    function set focusPane(value:Sprite):void;

    //----------------------------------
    //  nextTabIndex
    //----------------------------------

    /**
     *  The next unique tab index to use in this tab loop.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    function get nextTabIndex():int;

    //----------------------------------
    //  showFocusIndicator
    //----------------------------------

    /**
     *  A flag that indicates whether to display an indicator that
     *  a component has focus.
     *  If <code>true</code> a component receiving focus
     *  draws a visible indicator that it has focus.
     *
     *  <p>By default, this is <code>false</code> until the user uses
     *  the Tab key, then it is set to <code>true</code>.</p>
     *
     *  <p>In general it is better to use 
     *  the <code>showFocus()</code> and <code>hideFocus()</code> methods
     *  to change this property as those methods also update the
     *  visual indicator that a component has focus.</p>
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    function get showFocusIndicator():Boolean;
    
    /**
     *  @private
     */
    function set showFocusIndicator(value:Boolean):void;

    //--------------------------------------------------------------------------
    //
    //  Methods
    //
    //--------------------------------------------------------------------------

    /**
     *  Gets the IFocusManagerComponent component that currently has the focus.
     *  Calling this method is recommended instead of using the Stage object 
     *  because it indicates which component has focus.
     *  The Stage might return a subcomponent in that component.
     *
     *  @return IFocusManagerComponent object that has focus.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    function getFocus():IFocusManagerComponent;

    /**
     *  Sets focus to an IFocusManagerComponent component.  Does not check for
     *  the components visibility, enabled state, or any other conditions.
     *
     *  @param o A component that can receive focus.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    function setFocus(o:IFocusManagerComponent):void;

    /**
     *  Sets <code>showFocusIndicator</code> to <code>true</code>
     *  and draws the visual focus indicator on the focused object, if any.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    function showFocus():void;

    /**
     *  Sets <code>showFocusIndicator</code> to <code>false</code>
     *  and removes the visual focus indicator from the focused object, if any.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    function hideFocus():void;

    /**
     *  The SystemManager activates and deactivates a FocusManager
     *  if more than one IFocusManagerContainer is visible at the same time.
     *  If the mouse is clicked in an IFocusManagerContainer with a deactivated
     *  FocusManager, the SystemManager will call 
     *  the <code>activate()</code> method on that FocusManager.
     *  The FocusManager that was activated will have its <code>deactivate()</code> method
     *  called prior to the activation of another FocusManager.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    function activate():void;

    /**
     *  The SystemManager activates and deactivates a FocusManager
     *  if more than one IFocusManagerContainer is visible at the same time.
     *  If the mouse is clicked in an IFocusManagerContainer with a deactivated
     *  FocusManager, the SystemManager will call 
     *  the <code>activate()</code> method on that FocusManager.
     *  The FocusManager that was activated will have its <code>deactivate()</code> method
     *  called prior to the activation of another FocusManager.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    function deactivate():void;

    /**
     *  Returns the IFocusManagerComponent that contains the given object, if any.
     *  Because the player can set focus to a subcomponent of a Flex component
     *  this method determines which IFocusManagerComponent has focus from
     *  the component perspective.
     *
     *  @param o An object that can have player-level focus.
     *
     *  @return The IFOcusManagerComponent containing <code>o</code> or 
     *  <code>null</code>
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    function findFocusManagerComponent(o:InteractiveObject):IFocusManagerComponent;

    /**
     *  Returns the IFocusManagerComponent that would receive focus
     *  if the user pressed the Tab key to navigate to another component.
     *  It will return the same component as the current focused component
     *  if there are no other valid components in the application.
     *
     *  @param backward If <code>true</code>, return the object 
     *  as if the Shift-Tab keys were pressed.
     *
     *  @return The component that would receive focus.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    function getNextFocusManagerComponent(
                            backward:Boolean = false):IFocusManagerComponent;


}

}