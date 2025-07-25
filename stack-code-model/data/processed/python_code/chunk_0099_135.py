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

import flash.display.DisplayObject;
import flash.display.DisplayObjectContainer;
import flash.events.Event;
import flash.events.FocusEvent;
import flash.events.KeyboardEvent;
import flash.events.MouseEvent;
import flash.geom.Point;
import flash.geom.Rectangle;
import flash.ui.Keyboard;
import flash.utils.getTimer;

import mx.controls.listClasses.IListItemRenderer;
import mx.core.EdgeMetrics;
import mx.core.IFlexDisplayObject;
import mx.core.ILayoutDirectionElement;
import mx.core.IRectangularBorder;
import mx.core.IUIComponent;
import mx.core.UIComponent;
import mx.core.UIComponentGlobals;
import mx.core.mx_internal;
import mx.effects.Tween;
import mx.events.DropdownEvent;
import mx.events.FlexMouseEvent;
import mx.events.InterManagerRequest;
import mx.events.ListEvent;
import mx.events.MenuEvent;
import mx.events.SandboxMouseEvent;
import mx.managers.IFocusManagerComponent;
import mx.managers.ISystemManager;
import mx.managers.PopUpManager;
import mx.styles.ISimpleStyleClient;

use namespace mx_internal;

//--------------------------------------
//  Events
//-------------------------------------- 

/**
 *  Dispatched when the specified UIComponent closes. 
 *
 *  @eventType mx.events.DropdownEvent.CLOSE
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Event(name="close", type="mx.events.DropdownEvent")]

/**
 *  Dispatched when the specified UIComponent opens.
 *
 *  @eventType mx.events.DropdownEvent.OPEN
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Event(name="open", type="mx.events.DropdownEvent")]

//--------------------------------------
//  Styles
//--------------------------------------

include "../styles/metadata/IconColorStyles.as"

/**
 *  Number of pixels between the divider line and the right 
 *  edge of the component.
 *  
 *  @default 18
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Style(name="arrowButtonWidth", type="Number", format="Length", inherit="no")]

/**
 *  Length of a close transition, in milliseconds.
 *
 *  The default value for the Halo theme is 250.
 *  The default value for the Spark theme is 50.
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Style(name="closeDuration", type="Number", format="Time", inherit="no")]

/**
 *  Easing function to control component closing tween.
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Style(name="closeEasingFunction", type="Function", inherit="no")]

/**
 *  The default icon class for the main button.
 *
 *  @default null
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Style(name="icon", type="Class", inherit="no", states="up, over, down, disabled")]

/**
 *  Length of an open transition, in milliseconds.
 *
 *  The default value for the Halo theme is 250.
 *  The default value for the Spark theme is 0.
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Style(name="openDuration", type="Number", format="Time", inherit="no")]

/**
 *  Easing function to control component opening tween.
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Style(name="openEasingFunction", type="Function", inherit="no")]

/**
 *  The name of a CSS style declaration used by the control.  
 *  This style allows you to control the appearance of the 
 *  UIComponent object popped up by this control. 
 *
 *  @default undefined
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Style(name="popUpStyleName", type="String", inherit="no")]

/**
 *  Skin class for the popUpDown state (when arrowButton is in down 
 *  state) of the background and border.
 * 
 *  <p>The default skin class is based on the theme. For example, with the Halo theme,
 *  the default skin class is <code>mx.skins.halo.PopUpButtonSkin</code>. For the Spark theme, the default skin
 *  class is <code>mx.skins.spark.PopUpButtonSkin</code>.</p>
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Style(name="popUpDownSkin", type="Class", inherit="no")]

/**
 *  Number of vertical pixels between the PopUpButton and the
 *  specified popup UIComponent.
 * 
 *  @default 0
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Style(name="popUpGap", type="Number", format="Length", inherit="no")]

/**
 *  The icon used for the right button of PopUpButton.
 *  Supported classes are mx.skins.halo.PopUpIcon
 *  and mx.skins.halo.PopUpMenuIcon.
 * 
 *  @default mx.skins.halo.PopUpIcon (for Halo and Spark themes)
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Style(name="popUpIcon", type="Class", inherit="no")]

/**
 *  Skin class for the popUpOver state (over arrowButton) of 
 *  the background and border.
 *  
 *  <p>The default skin class is based on the theme. For example, with the Halo theme,
 *  the default skin class is <code>mx.skins.halo.PopUpButtonSkin</code>. For the Spark theme, the default skin
 *  class is <code>mx.skins.spark.PopUpButtonSkin</code>.</p>
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Style(name="popUpOverSkin", type="Class", inherit="no")]

/**
 *  Default stateful skin class for the control.
 *
 *  The default value for the Halo theme is <code>mx.skins.halo.PopUpButtonSkin</code>.
 *  The default value for the Spark theme is <code>mx.skins.spark.PopUpButtonSkin</code>.
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Style(name="skin", type="Class", inherit="no", states="up, over, down, disabled, popUpOver, popUpDown")]

/**
 *  Color of any symbol of a component. Examples include the check mark of a CheckBox or
 *  the arrow of a ScrollBar button.
 *   
 *  @default 0x000000
 * 
 *  @langversion 3.0
 *  @playerversion Flash 10
 *  @playerversion AIR 1.5
 *  @productversion Flex 4
 */ 
[Style(name="symbolColor", type="uint", format="Color", inherit="yes", theme="spark")]

//--------------------------------------
//  Excluded APIs
//--------------------------------------

[Exclude(name="toggle", kind="property")]
[Exclude(name="selectedDisabledIcon", kind="style")]
[Exclude(name="selectedDisabledSkin", kind="style")]
[Exclude(name="selectedDownIcon", kind="style")]
[Exclude(name="selectedDownSkin", kind="style")]
[Exclude(name="selectedOverIcon", kind="style")]
[Exclude(name="selectedOverSkin", kind="style")]
[Exclude(name="selectedUpIcon", kind="style")]
[Exclude(name="selectedUpSkin", kind="style")]

//--------------------------------------
//  Other metadata
//--------------------------------------

//[IconFile("PopUpButton.png")]

[RequiresDataBinding(true)]

/** 
 *  The PopUpButton control adds a flexible pop-up control
 *  interface  to a Button control.
 *  It contains a main button and a secondary button,
 *  called the pop-up button, which pops up any UIComponent
 *  object when a user clicks the pop-up button. 
 *
 *  <p>A PopUpButton control can have a text label, an icon,
 *  or both on its face.
 *  When a user clicks the main part of the PopUpButton 
 *  control, it dispatches a <code>click</code> event.</p>
 *
 *  <p>One common use for the PopUpButton control is to have
 *  the pop-up button open a List control or a Menu control
 *  that changes  the function and label of the main button.</p>
 *
 *  <p>The PopUpButton control has the following default characteristics:</p>
 *     <table class="innertable">
 *        <tr>
 *           <th>Characteristic</th>
 *           <th>Description</th>
 *        </tr>
 *        <tr>
 *           <td>Default size</td>
 *           <td>Sufficient width to accommodate the label and icon on the main button and the icon on the pop-up button</td>
 *        </tr>
 *        <tr>
 *           <td>Minimum size</td>
 *           <td>0 pixels</td>
 *        </tr>
 *        <tr>
 *           <td>Maximum size</td>
 *           <td>Undefined</td>
 *        </tr>
 *     </table>
 *
 *  @mxml
 *  
 *  <p>The <code>&lt;mx:PopUpButton&gt;</code> tag inherits all of the tag
 *  attributes of its superclass and adds the following tag attributes:</p>
 *  
 *  <pre>
 *  &lt;mx:PopUpButton
 *    <strong>Properties</strong> 
 *    openAlways="false|true
 *    popUp="No default"
 *  
 *    <strong>Styles</strong>
 *    arrowButtonWidth="16"
 *    closeDuration="250"
 *    closeEasingFunction="No default"
 *    disabledIconColor="0x999999"
 *    iconColor="0x111111"
 *    openDuration="250"
 *    openEasingFunction="No default"
 *    popUpDownSkin="popUpDownSkin"
 *    popUpGap="0"
 *    popUpIcon="PopUpIcon"
 *    popUpOverSkin="popUpOverSkin"
 *  
 *    <strong>Events</strong>
 *    close="No default"
 *    open="No default"
 *  /&gt;
 *  </pre>
 *
 *  @includeExample examples/PopUpButtonExample.mxml
 * 
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public class PopUpButton extends Button 
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
    public function PopUpButton()
    {
        super();
                        
        addEventListener(MouseEvent.MOUSE_MOVE, mouseMoveHandler);
        addEventListener(Event.REMOVED_FROM_STAGE, removedFromStageHandler);
    }
    
    //--------------------------------------------------------------------------
    //
    //  Variables
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     */
    private var inTween:Boolean = false;

    /**
     *  @private
     *  Is the popUp list currently shown?
     */
    private var showingPopUp:Boolean = false;

    /**
     *  @private
     *  The tween used for showing/hiding the popUp.
     */
    private var tween:Tween = null;
    
    /**
     *  @private
     *  Greater of the arrowButtonWidth style and the icon's width.
     */
    private var arrowButtonsWidth:Number = 0;

    /**
     *  @private
     *  Greater of the arrowButtonsHeight style and the icon's height.
     */
    private var arrowButtonsHeight:Number = 0;

    /**
     *  @private
     */
    private var popUpIconChanged:Boolean = false;

    /**
     *  @private
     */
    private var popUpChanged:Boolean = false;
    
    //--------------------------------------------------------------------------
    //
    //  Overridden properties
    //
    //--------------------------------------------------------------------------
    
    //----------------------------------
    //  showInAutomationHierarchy
    //----------------------------------

    /**
     *  @private
     */
    override public function set showInAutomationHierarchy(value:Boolean):void
    {
        //do not allow value changes
    }
    
    //----------------------------------
    //  toggle
    //----------------------------------

    [Inspectable(environment="none")]

    /**
     *  @private
     *  A PopUpButton is not toggleable by definition, so _toggle is set
     *  to false in the constructor and can't be changed via this setter.
     */
    override public function set toggle(value:Boolean):void
    {
    }
     
    //--------------------------------------------------------------------------
    //
    //  Properties
    //
    //--------------------------------------------------------------------------


    //----------------------------------
    //  closeOnActivity
    //----------------------------------
    
    /**
     *  @private
     *  Storage for the closeOnActivity property.
     */
    private var _closeOnActivity:Boolean = true;
    
    /**
     *  If <code>true</code>, specifies that the pop-up control closes
     *  on a click or other user activity.
     *  The pop-up control is the control opened by a click on the 
     *  pop-up button.
     * 
     *  <p>For pop-up controls like Menu, List, or TileList,  
     *  you can leave this property with its default value of <code>true</code>
     *  because those controls should close on activity.
     *  However, for multiple selection and other types of pop-up controls,
     *  you can set this property to <code>false</code> to prevent the 
     *  pop-up control from closing on activity.</p>
     *  
     *  @default true 
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */     
    public function get closeOnActivity():Boolean
    {
        return _closeOnActivity;
    }
    
    /**
     *  @private
     */  
    public function set closeOnActivity(value:Boolean):void
    {
        _closeOnActivity = value;
    }
    

    //----------------------------------
    //  openAlways
    //----------------------------------
    
    /**
     *  @private
     *  Storage for the openAlways property.
     */
    private var _openAlways:Boolean = false;
    
    [Inspectable(category="General", defaultValue="false")]
    
    /**
     *  If <code>true</code>, specifies to pop up the 
     *  <code>popUp</code> when you click the main button. 
     *  The <code>popUp</code> always appears when you press the Spacebar, 
     *  or when you click the pop-up button, regardless of the setting of 
     *  the <code>openAlways</code> property.
     *
     *  @default false
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */     
    public function get openAlways():Boolean
    {
        // We are not exposing this property for now, until the need arises.
        return _openAlways;
    }
    
    /**
     *  @private
     */  
    public function set openAlways(value:Boolean):void
    {
        _openAlways = value;
    }
    
    //----------------------------------
    //  popUp
    //----------------------------------
    
    /**
     *  @private
     *  Storage for popUp property.
     */    
    private var _popUp:IUIComponent = null;
    
    [Bindable(event='popUpChanged')]
    [Inspectable(category="General", defaultValue="null")]
    
    /**
     *  Specifies the UIComponent object, or object defined by a subclass 
     *  of UIComponent, to pop up. 
     *  For example, you can specify a Menu, TileList, or Tree control. 
     *
     *  @default null 
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */    
    public function get popUp():IUIComponent
    {
        return _popUp;
    }
    
    /**
     *  @private
     */  
    public function set popUp(value:IUIComponent):void
    {
        _popUp = value;
        popUpChanged = true;

        invalidateProperties();
    }

    //--------------------------------------------------------------------------
    //
    //  Overridden methods: UIComponent
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     */    
    override protected function commitProperties():void
    {
        super.commitProperties();

        if (popUpChanged)
        {
            if (_popUp is IFocusManagerComponent)
                IFocusManagerComponent(_popUp).focusEnabled = false;
                
            _popUp.cacheAsBitmap = true;
            _popUp.scrollRect = new Rectangle(0, 0, 0, 0);        
            
            if (_popUp is Menu)
                _popUp.addEventListener(MenuEvent.MENU_HIDE, menuHideHandler);
                
            if (_popUp is IListItemRenderer)
            {
                _popUp.addEventListener(
                    ListEvent.ITEM_CLICK, popUpItemClickHandler);
            }
            
            _popUp.addEventListener(FlexMouseEvent.MOUSE_DOWN_OUTSIDE,
                                    popMouseDownOutsideHandler);
            
            _popUp.addEventListener(FlexMouseEvent.MOUSE_WHEEL_OUTSIDE,
                                    popMouseDownOutsideHandler);
            _popUp.addEventListener(SandboxMouseEvent.MOUSE_DOWN_SOMEWHERE,
                                    popMouseDownOutsideHandler);
            _popUp.addEventListener(SandboxMouseEvent.MOUSE_WHEEL_SOMEWHERE,
                                    popMouseDownOutsideHandler);
            //weak reference to stage
             var sm:ISystemManager = systemManager.topLevelSystemManager;
            sm.getSandboxRoot().addEventListener(Event.RESIZE, stage_resizeHandler, false, 0, true);
                
            _popUp.owner = this;
            
            if (_popUp is ISimpleStyleClient)
                ISimpleStyleClient(_popUp).styleName = getStyle("popUpStyleName");
            
            popUpChanged = false;
        }
        
        // Close if we're disabled and we happen to still be showing our popup.
        if (showingPopUp && !enabled)
            close();
    }

    /**
     *  @private
     */
    override protected function measure():void
    {
        super.measure();

        calcArrowButtonSize();
        
        // Add in pop-up button width
        measuredWidth += arrowButtonsWidth;
        measuredHeight = arrowButtonsHeight;
    }
    
    /**
     *  @private
     */
    override public function styleChanged(styleProp:String):void
    {
        // PopUpIcon style prop has changed, dump skins
        if (styleProp == null ||
            styleProp == "styleName" ||
            styleProp.toLowerCase().indexOf("popupicon") != -1)
        {
            popUpIconChanged = true;
            changeSkins();
        }
        if (styleProp == "arrowButtonWidth")
            invalidateSize();
        else if (styleProp == "popUpStyleName" && _popUp 
                && _popUp is ISimpleStyleClient)
            ISimpleStyleClient(_popUp).styleName = getStyle("popUpStyleName");
            
        super.styleChanged(styleProp);
    }
    
    //--------------------------------------------------------------------------
    //
    //  Overridden methods: Button
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     */
    override mx_internal function layoutContents(unscaledWidth:Number,
                                                 unscaledHeight:Number,
                                                 offset:Boolean):void
    {
        if ((!isNaN(explicitWidth) && !isNaN(explicitHeight)) ||
            popUpIconChanged)
        {
            calcArrowButtonSize();
            popUpIconChanged = false;
        }

        unscaledWidth -= arrowButtonsWidth;
        
        super.layoutContents(unscaledWidth, unscaledHeight, offset);
        
        unscaledWidth += arrowButtonsWidth;
    }
    
    /**
     *  @private
     *  Displays one of the six possible skins,
     *  creating it if it doesn't already exist.
     */
    override mx_internal function viewSkin():void
    {
        // Determine which skin to display, based on whether this
        // PopUpButton is enabled or disabled, whether it is
        // selected or unselected, and how it is currently interacting
        // with the mouse (i.e., the up/over/down state).
        
        var tempSkinName:String;
        var stateName:String;
        
        if (!enabled)
            tempSkinName = "disabledSkin";
        else if (phase == "arrowOver")
            tempSkinName = "popUpOverSkin";
        else if (phase == "arrowDown")
            tempSkinName = "popUpDownSkin";   
        else 
            tempSkinName = phase + "Skin";
        
        viewSkinForPhase(tempSkinName, getCurrentButtonState());
    }

    /**
     *  @private
     */
    override mx_internal function getCurrentIconName():String
    {
        var iconName:String = super.getCurrentIconName();

        if (iconName)
            return iconName; 

        if (phase == "arrowOver")
            iconName = selected ? selectedOverIconName : overIconName;
        else if (phase == "arrowDown")
            iconName = selected ? selectedDownIconName : downIconName;
        else
            iconName = phase + "Icon";

        return iconName;
    }
    
    /**
     *  @private
     *  Displays one of the four possible icons,
     *  creating it if it doesn't already exist.
     */
    override mx_internal function viewIcon():void
    {
        // Determine which skin to display, based on whether this
        // PopUpButton is enabled or disabled, whether it is
        // selected or unselected, and how it is currently interacting
        // with the mouse (i.e., the up/over/down state).
        
        var iconName:String;
        
        if (!enabled)
            iconName = "disabledIcon";
        else if (phase == "arrowOver")
            iconName = selected ? selectedOverIconName : overIconName;
        else if (phase == "arrowDown")
            iconName = selected ? selectedDownIconName : downIconName;
        else
            iconName = phase + "Icon";
        
        viewIconForPhase(iconName);
    }

    /**
     *  @private
     *  Computes the current button state based on whether this button is 
     *  enabled or disabled, whether it is selected or unselected, and how it 
     *  is currently interacting with the mouse (i.e. the up/over/down state).
     */
    override mx_internal function getCurrentButtonState():String
    {
        _currentButtonState = "";
        
        if (!enabled)
            _currentButtonState = "disabled";
        else if (phase == "arrowOver")
            _currentButtonState = "popUpOver";
        else if (phase == "arrowDown")
            _currentButtonState = "popUpDown";             
        else 
            _currentButtonState = phase;
        
        return _currentButtonState;
    }
    
    //--------------------------------------------------------------------------
    //
    //  Methods
    //
    //--------------------------------------------------------------------------
    
    /**
     *  @private
     *  Used by PopUpMenuButton
     */     
    mx_internal function getPopUp():IUIComponent
    {
        return _popUp ? _popUp : null;
    }
    
    /**
     *  Opens the UIComponent object specified by the <code>popUp</code> property.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */  
    public function open():void
    {
        openWithEvent(null);
    }
    
    /**
     *  @private
     */
    private function openWithEvent(trigger:Event = null):void
    {
        if (!showingPopUp && enabled)
        {
            displayPopUp(true);

            var cbde:DropdownEvent = new DropdownEvent(DropdownEvent.OPEN);
            cbde.triggerEvent = trigger;
            dispatchEvent(cbde);
        }
    }
    
    /**
     *  Closes the UIComponent object opened by the PopUpButton control.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */  
    public function close():void
    {
        closeWithEvent(null);
    }

    /**
     *  @private
     */
    private function closeWithEvent(trigger:Event = null):void
    {
        if (showingPopUp)
        {
            displayPopUp(false);

            var cbde:DropdownEvent = new DropdownEvent(DropdownEvent.CLOSE);
            cbde.triggerEvent = trigger;
            dispatchEvent(cbde);
        }
    }

    /**
     *  @private
     */
    private function displayPopUp(show:Boolean):void
    {
        if (!initialized || (show == showingPopUp))
            return;
        // Subclasses may extend to do pre-processing
        // before the popUp is displayed
        // or override to implement special display behavior
        
        if (getPopUp() == null)
            return;
        
        if (_popUp is ILayoutDirectionElement)
        {
            ILayoutDirectionElement(_popUp).layoutDirection = layoutDirection;
        }
        
        //Show or hide the popup
        var initY:Number;
        var endY:Number;
        var easingFunction:Function;
        var duration:Number;
        var sm:ISystemManager = systemManager.topLevelSystemManager;
        var screen:Rectangle = sm.getVisibleApplicationRect(null, true);

        if (show)
        {
            if (_popUp.parent == null)
            {
                PopUpManager.addPopUp(_popUp, this, false);
                _popUp.owner = this;
            }
            else
                PopUpManager.bringToFront(_popUp);
        }
            
        var popUpGap:Number = getStyle("popUpGap");
        var point:Point = new Point(layoutDirection == "rtl" ? _popUp.getExplicitOrMeasuredWidth() : 0, unscaledHeight + popUpGap);
        point = localToGlobal(point);
        
        if (show)
        {          
           if (point.y + _popUp.height > screen.bottom && 
                point.y > (screen.top + height + _popUp.height))
            { 
                // PopUp will go below the bottom of the stage
                // and be clipped. Instead, have it grow up.
                point.y -= (unscaledHeight + _popUp.height + 2*popUpGap);
                initY = -_popUp.height;
            }
            else
            {
                initY = _popUp.height;
            }

            point.x = Math.min( point.x, screen.right - _popUp.getExplicitOrMeasuredWidth());
            point.x = Math.max( point.x, 0);
            point = _popUp.parent.globalToLocal(point);
            if (_popUp.x != point.x || _popUp.y != point.y)
                _popUp.move(point.x, point.y);

            _popUp.scrollRect = new Rectangle(0, initY,
                    _popUp.width, _popUp.height);
            
            if (!_popUp.visible)
                _popUp.visible = true;
            
            endY = 0;
            showingPopUp = show;
            duration = getStyle("openDuration");
            easingFunction = getStyle("openEasingFunction") as Function;
        }
        else
        {
            showingPopUp = show;

            if (_popUp.parent == null)
                return;

            point = _popUp.parent.globalToLocal(point);

            endY = (point.y + _popUp.height > screen.bottom && 
                               point.y > (screen.top + height + _popUp.height)
                               ? -_popUp.height - 2
                               : _popUp.height + 2);
            initY = 0;
            duration = getStyle("closeDuration")
            easingFunction = getStyle("closeEasingFunction") as Function;
        }
        
        inTween = true;
        UIComponentGlobals.layoutManager.validateNow();
        
        // Block all layout, responses from web service, and other background
        // processing until the tween finishes executing.
        UIComponent.suspendBackgroundProcessing();
        
        tween = new Tween(this, initY, endY, duration);
        if (easingFunction != null)
            tween.easingFunction = easingFunction;
    }
    
    /**
     *  @private
     *  Calculates the ArrowButton's sizes.
     */ 
    private function calcArrowButtonSize():void
    {
        // If the current skin defines a borderMetrics property,
        // then use it. Otherwise, use a default value.
        var bm:EdgeMetrics;
        
        if (currentSkin is IRectangularBorder)
            bm = IRectangularBorder(currentSkin).borderMetrics;
        else
            bm = new EdgeMetrics(3, 3, 3, 3);
        
        var popUpIcon:IFlexDisplayObject =
            IFlexDisplayObject(getChildByName("popUpIcon"));
        
        // If not, create it.
        if (!popUpIcon)
        {
            var popUpIconClass:Class = Class(getStyle("popUpIcon"));
            popUpIcon = new popUpIconClass();         
        }
        
        arrowButtonsWidth = Math.max(getStyle("arrowButtonWidth"),
                                    popUpIcon.width + bm.right + 1);
        arrowButtonsHeight = Math.max(measuredHeight,
                                     popUpIcon.height + bm.top + bm.bottom);
    }

    /**
     *  @private
     *  Returns true if the mouse is over the pop-up button
     */      
    mx_internal function overArrowButton(event:MouseEvent):Boolean
    {
        return event.localX >= unscaledWidth - arrowButtonsWidth;
    }

    /**
     *  @private
     */
    mx_internal function onTweenUpdate(value:Number):void
    {
        _popUp.scrollRect =
            new Rectangle(0, value, _popUp.width, _popUp.height);
    }

    /**
     *  @private
     */
    mx_internal function onTweenEnd(value:Number):void
    {
        _popUp.scrollRect =
            new Rectangle(0, value, _popUp.width, _popUp.height);

        inTween = false;
        UIComponent.resumeBackgroundProcessing();

        if (!showingPopUp)
        {
            _popUp.visible = false;
            _popUp.scrollRect = null;
        }
    }
        
    //--------------------------------------------------------------------------
    //
    //  Overridden event handlers: UIComponent
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     */
    override protected function keyDownHandler(event:KeyboardEvent):void
    {
        super.keyDownHandler(event);
        
        if (event.ctrlKey && event.keyCode == Keyboard.DOWN)
        {
            openWithEvent(event);
            event.stopPropagation();
        }
        else if ((event.ctrlKey && event.keyCode == Keyboard.UP) ||
                 (event.keyCode == Keyboard.ESCAPE))
        {
            closeWithEvent(event);
            event.stopPropagation();
        }
        else if (event.keyCode == Keyboard.ENTER && showingPopUp)
        {
            // Redispatch the event to the popup
            // and let its keyDownHandler() handle it.
            _popUp.dispatchEvent(event);
            closeWithEvent(event);                      
            event.stopPropagation();
        }       
        else if (showingPopUp &&
                 (event.keyCode == Keyboard.UP ||
                  event.keyCode == Keyboard.DOWN ||
                  event.keyCode == Keyboard.LEFT ||
                  event.keyCode == Keyboard.RIGHT ||
                  event.keyCode == Keyboard.PAGE_UP ||
                  event.keyCode == Keyboard.PAGE_DOWN))
        {
            // Redispatch the event to the popup
            // and let its keyDownHandler() handle it.
            _popUp.dispatchEvent(event);
            event.stopPropagation();
        }
    }

    /**
     *  @private
     */
    override protected function focusOutHandler(event:FocusEvent):void
    {
        // Note: event.relatedObject is the object getting focus.
        // It can be null in some cases, such as when you open
        // the popUp and then click outside the application.

        // If the dropdown is open...
        if (showingPopUp && _popUp && event.target == this)
        {
            // If focus is moving outside the popUp...
            if (!event.relatedObject)
            {
                close();
            }
            else if (event.relatedObject is Menu)
            {
                // For nested Menu's find parent.
                var target:Menu = Menu(event.relatedObject);
                while (target.parentMenu) 
                {
                    target = target.parentMenu;
                }
                if (_popUp is DisplayObjectContainer && !DisplayObjectContainer(_popUp).contains(target))
                    close();
            }
            else if (_popUp is DisplayObjectContainer && !DisplayObjectContainer(_popUp).contains(event.relatedObject))
            {
                close();
            }
        }

        super.focusOutHandler(event);
    }

    //--------------------------------------------------------------------------
    //
    //  Overridden event handlers: Button
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     */
    override protected function rollOverHandler(event:MouseEvent):void
    {
        // Check if the pop-up button was pressed.
        if (overArrowButton(event))
        {
            phase = "arrowOver";
            viewSkin();
            return;
        }

        super.rollOverHandler(event);
    }

    /**
     *  @private
     */
    override protected function rollOutHandler(event:MouseEvent):void
    {
        // Check if the pop-up button was pressed.
        if (overArrowButton(event))
        {
            phase = "up";
            viewSkin();
            return;
        }

        super.rollOutHandler(event);
    }
    
    /**
     *  @private
     */
    override protected function mouseDownHandler(event:MouseEvent):void
    {
        // Check if the pop-up button was pressed.
        if (overArrowButton(event))
        {
            phase = "arrowDown";            
            viewSkin();
            return;
        }

        super.mouseDownHandler(event);
    }

    /**
     *  @private
     */
    override protected function mouseUpHandler(event:MouseEvent):void
    {
        // Check if the pop-up button was pressed.
        if (overArrowButton(event))
        {
            phase = "arrowOver";            
            viewSkin();            
            return;
        }

        super.mouseUpHandler(event);
    }

    /**
     *  @private
     */
    override protected function clickHandler(event:MouseEvent):void
    {
        if (overArrowButton(event))
        {
            if (showingPopUp)
                closeWithEvent(event);
            else
                openWithEvent(event);

            event.stopImmediatePropagation();
        }
        else
        {
            super.clickHandler(event);
            if (openAlways) 
            {
                if (showingPopUp)
                    closeWithEvent(event);
                else
                    openWithEvent(event);       
            }   
        }
    }

    //--------------------------------------------------------------------------
    //
    //  Event handlers
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     */
    private function mouseMoveHandler(event:MouseEvent):void
    {
        // Check if the pop-up button was pressed.
        if (phase == "over" || phase == "arrowOver")
        {
            phase = overArrowButton(event) ? "arrowOver" : "over";    
            viewSkin();
        }
    }
    
    /**
     *  @private
     *  Close popUp for IListItemRenderer's like List/Menu.
     */   
    private function popUpItemClickHandler(event:Event):void
    {
        if (_closeOnActivity)
            close();
    }
    
    /**
     *  @private
     *  Hide is called intermittently before close gets called.
     *  Call close() in such cases to  reset variables.
     */    
    private function menuHideHandler(event:MenuEvent):void
    {
        //we don't want to close the popUp if we're just hiding 
        //a submenu
        if (event.menu != Menu(_popUp).getRootMenu())
        {
            return;
        }
        
        // Menu is hidden through a call to hide()
        // Make it visible again so that the menu can
        // be tweened and closed.
        showingPopUp = true;
        _popUp.visible = true;
        displayPopUp(false);
    }
    
    /**
     *  @private
     */    
    private function popMouseDownOutsideHandler(event:Event):void
    {
        if (event is MouseEvent)
        {
            // for automated testing, since we're generating this event and
            // can only set localX and localY, transpose those coordinates
            // and use them for the test point.
            var mouseEvent:MouseEvent = MouseEvent(event);
            var p:Point = event.target.localToGlobal(new Point(mouseEvent.localX, 
                                                               mouseEvent.localY));
            if (hitTestPoint(p.x, p.y, true))
            {
                // do nothing
            }
            else
            {
                close();
            }
        }
        else if (event is SandboxMouseEvent)
            close();
    }    
    
    /**
     *  @private
     */
    private function removedFromStageHandler(event:Event):void
    {
        // Ensure we've unregistered ourselves from PopupManager, else
        // we'll be leaked.
        if (_popUp) {
            PopUpManager.removePopUp(_popUp);
            showingPopUp = false;
        }
    }

    /**
     *  @private
     */
    private function stage_resizeHandler(event:Event):void 
    {
        // Hide the popUp and don't show tweening when popUp is closed
        // due to resizing.
        _popUp.visible = false;

        close();
    } 
    
    /**
     *  @private
     */
    mx_internal function get isShowingPopUp():Boolean
    {
        return showingPopUp;
    }

    /**
     *  @private
     */
    mx_internal function getArrowButtonsWidth():Number
    {
        return arrowButtonsWidth;
    }

}

}