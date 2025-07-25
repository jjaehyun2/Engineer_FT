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

package
{

import mx.utils.ColorUtil;

/**
 *  Defines the colors used by components that support the Halo theme.
 */
public class HaloColors 
{
    //include "../../core/Version.as";

    //--------------------------------------------------------------------------
    //
    //  Class variables
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     */
    private static var cache:Object = {};
    
    //--------------------------------------------------------------------------
    //
    //  Class methods
    //
    //--------------------------------------------------------------------------

    /**
     *  Returns a unique hash key based on the colors that are passed in. This
     *  key is used to store the calculated colors so they only need to be 
     *  calculated once.
     */
    public static function getCacheKey(... colors):String
    {
        return colors.join(",");
    }

    /**
     *  Calculates colors that are used by components that support the Halo theme, such as the colors of beveled edges.
     *  This method uses the <code>themeColor</code> and <code>fillColors</code> properties to calculate its colors. 
     * 
     *  @param colors 
     *  @param themeColor The value of the <code>themeColor</code> style property.
     *  @param fillColor0 The start color of a fill.
     *  @param fillColor1 The end color of a fill.
     */
    public static function addHaloColors(colors:Object,
                                         themeColor:uint,
                                         fillColor0:uint,
                                         fillColor1:uint):void
    {
        var key:String = getCacheKey(themeColor, fillColor0, fillColor1); 
        var o:Object = cache[key];
        
        if (!o)
        {
            o = cache[key] = {};
            
            // Cross-component styles
            o.themeColLgt = ColorUtil.adjustBrightness(themeColor, 100);
            o.themeColDrk1 = ColorUtil.adjustBrightness(themeColor, -75);
            o.themeColDrk2 = ColorUtil.adjustBrightness(themeColor, -25);
            o.fillColorBright1 = ColorUtil.adjustBrightness2(fillColor0, 15);
            o.fillColorBright2 = ColorUtil.adjustBrightness2(fillColor1, 15);
            o.fillColorPress1 = ColorUtil.adjustBrightness2(themeColor, 85);
            o.fillColorPress2 = ColorUtil.adjustBrightness2(themeColor, 60);
            o.bevelHighlight1 = ColorUtil.adjustBrightness2(fillColor0, 40);
            o.bevelHighlight2 = ColorUtil.adjustBrightness2(fillColor1, 40);
        }
        
        colors.themeColLgt = o.themeColLgt;
        colors.themeColDrk1 = o.themeColDrk1;
        colors.themeColDrk2 = o.themeColDrk2;
        colors.fillColorBright1 = o.fillColorBright1;
        colors.fillColorBright2 = o.fillColorBright2;
        colors.fillColorPress1 = o.fillColorPress1;
        colors.fillColorPress2 = o.fillColorPress2;
        colors.bevelHighlight1 = o.bevelHighlight1;
        colors.bevelHighlight2 = o.bevelHighlight2;
    }
}

}