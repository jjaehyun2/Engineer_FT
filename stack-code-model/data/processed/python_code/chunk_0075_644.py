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
package org.apache.royale.mdl.beads
{
	import org.apache.royale.core.IStrand;
    import org.apache.royale.core.IBead;
	import org.apache.royale.core.UIBase;

	/**
	 *  The ListItemSecondaryAction class decorates a tag element in a list item renderer
     *  Defines the Action sub-division
	 *  Requires the host ListItemrenderer to have "twoLine" or "threeLine" set to true
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 10.2
	 *  @playerversion AIR 2.6
	 *  @productversion Royale 0.8
	 */
	public class ListItemSecondaryAction implements IBead
	{
		/**
		 *  constructor.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10.2
		 *  @playerversion AIR 2.6
		 *  @productversion Royale 0.8
		 */
		public function ListItemSecondaryAction()
		{
			super();   
		}
		
		private var _strand:IStrand;		
		/**
		 *  @copy org.apache.royale.core.IBead#strand
		 *  
		 *  @langversion 3.0
		 *  @playerversion Flash 10.2
		 *  @playerversion AIR 2.6
		 *  @productversion Royale 0.8
		 *  @royaleignorecoercion HTMLElement;
		 */
		public function set strand(value:IStrand):void
		{
			_strand = value;
			
			COMPILE::JS
			{
				var host:UIBase = value as UIBase;
				
				if (host.element is HTMLElement)
				{
					host.element.classList.add("mdl-list__item-secondary-action");
				}
				else
				{
					throw new Error("Host component must be an MDL element.");
				}
			}
		}
    }
}