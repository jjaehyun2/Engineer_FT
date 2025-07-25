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
package org.apache.royale.jewel.beads.layouts
{
	import org.apache.royale.core.ILayoutChild;
	import org.apache.royale.core.ILayoutView;
	import org.apache.royale.core.IStrand;
	import org.apache.royale.core.IStyleableObject;
	import org.apache.royale.events.Event;
	import org.apache.royale.jewel.beads.models.ButtonBarModel;

	/**
	 *  The Jewel ButtonBarLayout class bead sizes and positions the button
	 *  elements that make up a org.apache.royale.jewel.ButtonBar.
	 *  
	 *  This bead arranges the Buttons horizontally and makes them all the same width 
	 *  (widthType = NaN) unless the buttonWidths property has been set in which case
	 *  the values stored in that array are used.
	 *
	 *  @langversion 3.0
	 *  @playerversion Flash 10.2
	 *  @playerversion AIR 2.6
	 *  @productversion Royale 0.9.7
	 */
	public class ButtonBarLayout extends HorizontalLayout
	{
		/**
		 *  constructor.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10.2
		 *  @playerversion AIR 2.6
		 *  @productversion Royale 0.9.7
		 */
		public function ButtonBarLayout()
		{
			super();
		}

		/**
		 * @royalesuppresspublicvarwarning
		 */
		public static const LAYOUT_TYPE_NAMES:String = "layout horizontal";

		private var model:ButtonBarModel;
		/**
		 *  Add class selectors when the component is addedToParent
		 *  Otherwise component will not get the class selectors when 
		 *  perform "removeElement" and then "addElement"
		 * 
 		 *  @langversion 3.0
 		 *  @playerversion Flash 10.2
 		 *  @playerversion AIR 2.6
 		 *  @productversion Royale 0.9.7
 		 */
		override public function beadsAddedHandler(event:Event = null):void
		{
			super.beadsAddedHandler();

			model = (host as IStrand).getBeadByType(ButtonBarModel) as ButtonBarModel;
			if (model) {
				widthType = model.buttonWidths != null ? model.widthType : NaN;
			}
		}

		/**
		 *  Switch between four different types of width
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10.2
		 *  @playerversion AIR 2.6
		 *  @productversion Royale 0.9.7
		 */
		public function get widthType():Number
        {
            return model.widthType;
        }
		public function set widthType(value:Number):void
        {
			if (model.widthType != value)
            {
				model.widthType = value;
                COMPILE::JS
                {
				if(hostComponent)
				{
					if (hostComponent.containsClass("pixelWidths"))
						hostComponent.removeClass("pixelWidths");
					if (hostComponent.containsClass("proportionalWidths"))
						hostComponent.removeClass("proportionalWidths");
					if (hostComponent.containsClass("percentWidths"))
						hostComponent.removeClass("percentWidths");
					if (hostComponent.containsClass("naturalWidths"))
						hostComponent.removeClass("naturalWidths");
					if (hostComponent.containsClass("sameWidths"))
						hostComponent.removeClass("sameWidths");
					if(isNaN(model.widthType))
					{
						hostComponent.addClass("sameWidths");
					}
					else
					{
						switch(model.widthType)
						{
							case ButtonBarModel.PIXEL_WIDTHS:
								hostComponent.addClass("pixelWidths");
								break;
							case ButtonBarModel.PROPORTIONAL_WIDTHS:
								hostComponent.addClass("proportionalWidths");
								break;
							case ButtonBarModel.PERCENT_WIDTHS:
								hostComponent.addClass("percentWidths");
								break;
							case ButtonBarModel.NATURAL_WIDTHS:
								hostComponent.addClass("naturalWidths");
								break;
						}
					}
				}
				}
			}
		}

		/**
		 * @copy org.apache.royale.core.IBeadLayout#layout
		 * @royaleignorecoercion org.apache.royale.core.ILayoutChild
		 * @royaleignorecoercion org.apache.royale.core.IStrand
		 * @royaleignorecoercion org.apache.royale.jewel.beads.models.ButtonBarModel
		 */
		override public function layout():Boolean
		{
			var contentView:ILayoutView = layoutView;
			var n:int = contentView.numElements;
			if (n <= 0) return false;

			for (var i:int=0; i < n; i++)
			{	
				var ilc:ILayoutChild = contentView.getElementAt(i) as ILayoutChild;
				if (ilc == null || !ilc.visible) continue;
				if (!(ilc is IStyleableObject)) continue;
				
				COMPILE::JS
				{
				// otherwise let the flexbox layout handle matters on its own.
				if (model.buttonWidths) {
					var widthValue:* = model.buttonWidths[i];
					
					if (model.widthType == ButtonBarModel.PIXEL_WIDTHS) {
						if (widthValue != null) ilc.width = Number(widthValue);
					} else {
						ilc.width = NaN;
					}
					// else if (_widthType == ButtonBarModel.PROPORTIONAL_WIDTHS) {
					// 	if (widthValue != null) ilc.element.style["flex-grow"] = String(widthValue);
					// }
					// else if (_widthType == ButtonBarModel.PERCENT_WIDTHS) {
					// 	if (widthValue != null) ilc.percentWidth = Number(widthValue);
					// }
				} 
				// else if (!_widthType == ButtonBarModel.NATURAL_WIDTHS) {
				// 	ilc.element.style["flex-grow"] = "1";
				// }
				}
			}

			// now let the horizontal layout take care of things.
			return super.layout();
		}
	}
}