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

import mx.effects.effectClasses.FadeInstance;

[Alternative(replacement="spark.effects.Fade", since="4.0")]

/**
 *  The Fade effect animates the <code>alpha</code> property of a component,
 *  either from transparent to opaque, or from opaque to transparent. 
 *  
 *  <p>If you specify the Fade effect for the <code>showEffect</code> 
 *  or <code>hideEffect</code> trigger, and if you omit values for the
 *  <code>alphaFrom</code> and <code>alphaTo</code> properties, 
 *  the effect automatically transitions <code>alpha</code> from 0
 *  to the target's current <code>alpha</code> value on a
 *  <code>showEffect</code> trigger, and from the target's current
 *  <code>alpha</code> value to 0 on a <code>hideEffect</code> trigger.</p> 
 *
 *  <p><b>Note:</b> To use the Fade effect with text,
 *  you must use an embedded font, not a device font. </p> 
 *
 *  @mxml
 *
 *  <p>The <code>&lt;mx:Fade&gt;</code> tag
 *  inherits the tag attributes of its superclass,
 *  and adds the following tag attributes:</p>
 *  
 *  <pre>
 *  &lt;mx:Fade 
 *    id="ID"
 *    alphaFrom="val"
 *    alphaTo="val"
 *  /&gt;
 *  </pre>
 *  
 *  @see mx.effects.effectClasses.FadeInstance
 *
 *  @includeExample examples/FadeEffectExample.mxml
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public class Fade extends TweenEffect
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
    private static var AFFECTED_PROPERTIES:Array = [ "alpha", "visible" ];

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
    public function Fade(target:Object = null)
    {
        super(target);

        instanceClass = FadeInstance;
    }
    
    //--------------------------------------------------------------------------
    //
    //  Properties
    //
    //--------------------------------------------------------------------------

    //----------------------------------
    //  alphaFrom
    //----------------------------------

    [Inspectable(category="General", defaultValue="undefined")]
    
    /** 
     *  Initial transparency level between 0.0 and 1.0, 
     *  where 0.0 means transparent and 1.0 means fully opaque. 
     * 
     *  <p>If the effect causes the target component to disappear,
     *  the default value is the current value of the target's
     *  <code>alpha</code> property.
     *  If the effect causes the target component to appear,
     *  the default value is 0.0.</p>
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

    [Inspectable(category="General", defaultValue="NaN")]
    
    /** 
     *  Final transparency level,
     *  where 0.0 means transparent and 1.0 means fully opaque.
     *
     *  <p>If the effect causes the target component to disappear,
     *  the default value is 0.0.
     *  If the effect causes the target component to appear,
     *  the default value is the current value of the target's
     *  <code>alpha</code> property.</p>
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var alphaTo:Number;
    
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
    override protected function initInstance(instance:IEffectInstance):void
    {
        super.initInstance(instance);
        
        var fadeInstance:FadeInstance = FadeInstance(instance);

        fadeInstance.alphaFrom = alphaFrom;
        fadeInstance.alphaTo = alphaTo;
    }
}

}