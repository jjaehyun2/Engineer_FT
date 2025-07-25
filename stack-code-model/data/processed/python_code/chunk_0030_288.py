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

package mx.effects
{

import mx.effects.effectClasses.MoveInstance;

[Alternative(replacement="spark.effects.Move", since="4.0")]

/**
 *  The Move effect changes the position of a component
 *  over a specified time interval.
 *  You can specify the initial position with the <code>xFrom</code> and
 *  <code>yFrom</code> values, the destination position with <code>xTo</code>
 *  and <code>yTo</code>, or the number of pixels to move the component
 *  with <code>xBy</code> and <code>yBy</code>. 
 *
 *  <p>If you specify any two of the values (initial position, destination,
 *  or amount to move), Flex calculates the third.
 *  If you specify all three, Flex ignores the <code>xBy</code> and
 *  <code>yBy</code> values.  
 *  If you specify only the <code>xTo</code> and <code>yTo</code> values
 *  or the <code>xBy</code> and <code>yBy</code> values,
 *  Flex sets <code>xFrom</code> and <code>yFrom</code> to be the object's
 *  current position.</p>
 *  
 *  <p>If you specify a Move effect for a <code>moveEffect</code> trigger,
 *  and if you do not set the six From, To, and By properties, 
 *  Flex sets them to create a smooth transition between the object's 
 *  old position and its new position.</p>
 *
 *  <p>You typically apply this effect to a target in a container 
 *  that uses absolute positioning, such as Canvas, 
 *  or one with <code>"layout=absolute"</code>,  such as Application or Panel. 
 *  If you apply it to a target in a container that performs automatic layout, 
 *  such as a VBox or Grid container, 
 *  the move occurs, but the next time the container updates its layout, 
 *  it moves the target back to its original position.
 *  You can set the container's <code>autoLayout</code> property to <code>false</code>
 *  to disable the move back, but that disables layout for all controls in the container.</p>
 *  
 *  @mxml
 *
 *  <p>The <code>&lt;mx:Move&gt;</code> tag
 *  inherits all of the tag attributes of its of its superclass,
 *  and adds the following tag attributes:</p>
 *  
 *  <pre>
 *  &lt;mx:Move
 *    id="ID"
 *    xFrom="val" 
 *    yFrom="val"
 *    xTo="val"
 *    yTo="val"
 *    xBy="val"
 *    yBy="val"
 *   /&gt;
 *  </pre>
 *
 *  @see mx.effects.effectClasses.MoveInstance
 *  
 *  @includeExample examples/MoveEffectExample.mxml
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public class Move extends TweenEffect
{
    include "../core/Version.as";

    //--------------------------------------------------------------------------
    //
    //  Class constants
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     */
    private static var AFFECTED_PROPERTIES:Array = [ "x", "y" ];
    private static var RELEVANT_STYLES:Array = 
        ["left", "right", "top", "bottom", "horizontalCenter", "verticalCenter"];

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
    public function Move(target:Object = null)
    {
        super(target);
        
        instanceClass = MoveInstance;
    }

    //--------------------------------------------------------------------------
    //
    //  Properties
    //
    //--------------------------------------------------------------------------

    //----------------------------------
    //  xBy
    //----------------------------------

    [Inspectable(category="General", defaultValue="NaN")]

    /** 
     *  Number of pixels to move the components along the x axis.
     *  Values can be negative. 
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var xBy:Number;

    //----------------------------------
    //  xFrom
    //----------------------------------

    [Inspectable(category="General", defaultValue="NaN")]

    /** 
     *  Initial position's x coordinate.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var xFrom:Number;
    
    //----------------------------------
    //  xTo
    //----------------------------------

    [Inspectable(category="General", defaultValue="NaN")]

    /** 
     *  Destination position's x coordinate.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var xTo:Number;
    
    //----------------------------------
    //  yBy
    //----------------------------------

    [Inspectable(category="General", defaultValue="NaN")]

    /** 
     *  Number of pixels to move the components along the y axis.
     *  Values can be negative.     
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var yBy:Number;

    //----------------------------------
    //  yFrom
    //----------------------------------

    [Inspectable(category="General", defaultValue="NaN")]

    /**
     *  Initial position's y coordinate.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var yFrom:Number;

    //----------------------------------
    //  yTo
    //----------------------------------

    [Inspectable(category="General", defaultValue="NaN")]

    /** 
     *  Destination position's y coordinate.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var yTo:Number;

    //--------------------------------------------------------------------------
    //
    //  Overridden methods
    //
    //--------------------------------------------------------------------------
    
    /**
     *  @private
     */
    override public function getAffectedProperties():Array /* of String */
    {
        return AFFECTED_PROPERTIES;
    }   

    /**
     *  @private
     */
    override public function get relevantStyles():Array /* of String */
    {
        return RELEVANT_STYLES;
    }   

    /**
     *  @private
     */
    override protected function initInstance(instance:IEffectInstance):void
    {
        super.initInstance(instance);
        
        var moveInstance:MoveInstance = MoveInstance(instance);

        moveInstance.xFrom = xFrom;
        moveInstance.xTo = xTo;
        moveInstance.xBy = xBy;
        moveInstance.yFrom = yFrom;
        moveInstance.yTo = yTo;
        moveInstance.yBy = yBy;
    }
}

}