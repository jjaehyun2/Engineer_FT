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
	import org.apache.royale.mdl.supportClasses.IFooterSection;
	import org.apache.royale.core.UIBase;

    COMPILE::JS
    {
        import org.apache.royale.core.WrappedHTMLElement;
        import org.apache.royale.html.util.addElementToWrapper;
    }

	/**
	 *  FooterLinkList class defines an footer unordered list as a drop-down (vertical) list
     *  and relies on an itemRenderer factory to produce its children components
	 *  and on a layout to arrange them. This is the only UI element aside from the 
     *  itemRenderers.
     *
     *  @langversion 3.0
     *  @playerversion Flash 10.2
     *  @playerversion AIR 2.6
     *  @productversion Royale 0.8
     */  
	public class FooterLinkList extends List
	{
        /**
         *  Constructor.
         *  
         *  @langversion 3.0
         *  @playerversion Flash 10.2
         *  @playerversion AIR 2.6
         *  @productversion Royale 0.8
         */
		public function FooterLinkList()
		{
			super();

            typeNames = "mdl-mega-footer__link-list";
		}

        /**
         * @royaleignorecoercion org.apache.royale.core.WrappedHTMLElement
         */
        COMPILE::JS
        override protected function createElement():WrappedHTMLElement
        {
			return addElementToWrapper(this,'ul');
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

			if(parent is IFooterSection)
			{
				var parentSection:IFooterSection = parent as IFooterSection;
				if(UIBase(parentSection).parent is Footer)
				{
					if (Footer(UIBase(parentSection).parent).mini)
					{
                        element.classList.remove(typeNames);
                        typeNames = "mdl-mini-footer__link-list";
                        setClassName(computeFinalClassNames());
					}
				}
			}
			else
			{
				throw new Error("FooterLinkList can not be used if parent is not a MDL Footer Section component.");
			}			
        } 
	}
}