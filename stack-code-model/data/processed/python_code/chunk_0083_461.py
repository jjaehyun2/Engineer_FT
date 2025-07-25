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

package mx.events
{

/**
 *  The FocusDirection class defines the constant values for the direction
 *  focus may be moved in. The value is used with the SWFBridgeRequest.MOVE_FOCUS_REQUEST
 *  request and with the FocusManager <code>moveFocus()</code> method.
 *  
 *  @see SWFBridgeRequest
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public final class FocusRequestDirection
{
    include "../core/Version.as";

    //--------------------------------------------------------------------------
    //
    //  Class constants
    //
    //--------------------------------------------------------------------------

    /**
     *  Move the focus forward to the next control in the tab loop as if the
	 *  TAB key were pressed.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public static const FORWARD:String = "forward";
    
    /**
     *  Move the focus backward to the previous control in the tab loop as if
	 *  the SHIFT+TAB keys were pressed.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public static const BACKWARD:String = "backward";
    
    /**
     *  Move the focus to the top/first control in the tab loop as if the
	 *  TAB key were pressed when no object had focus in the tab loop
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */ 
    public static const TOP:String = "top";
    
    /**
     *  Move the focus to the bottom/last control in the tab loop as if the
	 *  SHIFT+TAB key were pressed when no object had focus in the tab loop
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */ 
    public static const BOTTOM:String = "bottom";


}

}