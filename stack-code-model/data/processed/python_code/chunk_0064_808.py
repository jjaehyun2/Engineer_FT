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
package org.apache.royale.textLayout.elements
{
	/**
	 *  The OverflowPolicy class defines a set of constants for the <code>overflowPolicy</code> property
	 *  of the IConfiguration class. This defines how the composer will treat lines at the end of the composition area.
	 *
	 * @playerversion Flash 10
	 * @playerversion AIR 1.5
	 * @langversion 3.0
	 */
	 
 	public final class OverflowPolicy {
 	
	/** 
	 * Fit the line in the composition area if any part of the line fits.
	 *
	 * @playerversion Flash 10
	 * @playerversion AIR 1.5
	 * @langversion 3.0
	 */
	 
     public static const FIT_ANY:String = "fitAny";
    
	/*
	 * Fit the line in the composition area if the area from the top to the baseline fits.
	 *
	 * @playerversion Flash 10
	 * @playerversion AIR 1.5
	 * @langversion 3.0
	 */
	 
 //    public static const FIT_BASELINE:String = "fitAny";
    
	/** 
	 * Fit the line in the composition area if the area from the top to the baseline fits.
	 *
	 * @playerversion Flash 10
	 * @playerversion AIR 1.5
	 * @langversion 3.0
	 */
	 
     public static const FIT_DESCENDERS:String = "fitDescenders";
    
	}
}