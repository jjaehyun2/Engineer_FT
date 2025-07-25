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
package org.apache.royale.jewel.itemRenderers
{
    COMPILE::JS
    {
	import org.apache.royale.core.WrappedHTMLElement;
	import org.apache.royale.html.util.addElementToWrapper;
    }
	import org.apache.royale.core.StyledMXMLItemRenderer;
	import org.apache.royale.events.Event;
	import org.apache.royale.jewel.supportClasses.INavigationRenderer;
	import org.apache.royale.jewel.supportClasses.util.getLabelFromData;
    
	/**
	 *  The TabBarButtonInidicatorRestrictedToContentItemRenderer
     *  is a TabBarButtonItemRenderer that restrict indicator to content
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 10.2
	 *  @playerversion AIR 2.6
	 *  @productversion Royale 0.9.6
	 */
	public class TabBarButtonInidicatorRestrictedToContentItemRenderer extends TabBarButtonItemRenderer
	{
		/**
		 *  constructor.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10.2
		 *  @playerversion AIR 2.6
		 *  @productversion Royale 0.9.4
		 */
		public function TabBarButtonInidicatorRestrictedToContentItemRenderer()
		{
			super();
		}

		/**
		 * adding indicator to positioner makes the indicator fill all available space
		 * adding to "span" HTMLElement restrict indicator to content.
		 * Override this function in TabBarButtonItemRenderer subclasses
		 */
		COMPILE::JS
		override protected function addIndicator():void
		{
			span.appendChild(indicator);
		}
	}
}