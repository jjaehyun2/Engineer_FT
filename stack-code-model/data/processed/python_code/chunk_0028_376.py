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
package org.apache.royale.mdl
{
	import org.apache.royale.html.elements.Div;
    
    COMPILE::JS
    {
        import org.apache.royale.core.WrappedHTMLElement;
		import org.apache.royale.html.util.addElementToWrapper;
    }
    
	/**
	 *  The FooterLogo class defines a container as a styled section heading
	 *  This is used in footer bottom or left sections 
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 10.2
	 *  @playerversion AIR 2.6
	 *  @productversion Royale 0.8
	 */
	public class FooterLogo extends Div
	{
		/**
		 *  constructor.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10.2
		 *  @playerversion AIR 2.6
		 *  @productversion Royale 0.8
		 */
		public function FooterLogo()
		{
			super();

            typeNames = "mdl-logo";
		}

		/**
         *  Configuration depends on parent Footer.
		 *  Check to see if is mega or mini.
         *  
         *  @langversion 3.0
         *  @playerversion Flash 10.2
         *  @playerversion AIR 2.6
         *  @productversion Royale 0.8
        */ 
		COMPILE::JS
		override public function addedToParent():void
        {
			super.addedToParent();

			if(parent is FooterLeftSection || parent is FooterBottomSection)
			{
				//ok
			}
			else
			{
				throw new Error("FooterLeftSection can not be used if parent is not a MDL Footer component.");
			}			
        }
	}
}