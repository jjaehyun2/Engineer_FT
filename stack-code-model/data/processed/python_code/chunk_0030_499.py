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
	COMPILE::SWF
	{
	import org.apache.royale.core.IBorderPaddingMarginValuesImpl;
	import org.apache.royale.core.ILayoutChild;
	import org.apache.royale.core.ILayoutView;
	import org.apache.royale.core.IUIBase;
	import org.apache.royale.core.ValuesManager;
	import org.apache.royale.core.layout.EdgeData;
	}
	import org.apache.royale.events.Event;
	import org.apache.royale.jewel.beads.layouts.StyledLayoutBase;
	
    /**
     *  The SimpleHorizontalLayout class is a simple layout
     *  bead that takes the set of children and lays them out
     *  horizontally in one row. In JS we make use of the CSS flex layout rules.
	 * 
	 *  Note:SWF comes from basic layouts and are not tested
     *
     *  @langversion 3.0
     *  @playerversion Flash 10.2
     *  @playerversion AIR 2.6
     *  @productversion Royale 0.9.4
     */
	public class SimpleHorizontalLayout extends StyledLayoutBase
	{
        /**
         *  Constructor.
         *
         *  @langversion 3.0
         *  @playerversion Flash 10.2
         *  @playerversion AIR 2.6
         *  @productversion Royale 0.9.4
         */
		public function SimpleHorizontalLayout()
		{
			super();
		}

		/**
		 * @royalesuppresspublicvarwarning
		 */
		public static const LAYOUT_TYPE_NAMES:String = "layout horizontal";

		/**
		 *  Add class selectors when the component is addedToParent
		 *  Otherwise component will not get the class selectors when 
		 *  perform "removeElement" and then "addElement"
		 * 
 		 *  @langversion 3.0
 		 *  @playerversion Flash 10.2
 		 *  @playerversion AIR 2.6
 		 *  @productversion Royale 0.9.4
 		 */
		override public function beadsAddedHandler(event:Event = null):void
		{
			super.beadsAddedHandler();
			
			hostComponent.replaceClass("layout");
			hostComponent.replaceClass("horizontal");
		}

        /**
		 *  Layout children horizontally
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10.2
		 *  @playerversion AIR 2.6
		 *  @productversion Royale 0.9.4
		 *  @royaleignorecoercion org.apache.royale.core.ILayoutHost
		 *  @royaleignorecoercion org.apache.royale.core.WrappedHTMLElement
		 */
		override public function layout():Boolean
		{
            COMPILE::SWF
            {
				var contentView:ILayoutView = layoutView;

				var n:Number = contentView.numElements;
				if (n == 0) return false;

				var maxWidth:Number = 0;
				var maxHeight:Number = 0;
				var hostWidthSizedToContent:Boolean = host.isWidthSizedToContent();
				var hostHeightSizedToContent:Boolean = host.isHeightSizedToContent();
				var hostWidth:Number = host.width;
				var hostHeight:Number = host.height;

				var ilc:ILayoutChild;
				var data:Object;
				var canAdjust:Boolean = false;

				var paddingMetrics:EdgeData = (ValuesManager.valuesImpl as IBorderPaddingMarginValuesImpl).getPaddingMetrics(host);
				var borderMetrics:EdgeData = (ValuesManager.valuesImpl as IBorderPaddingMarginValuesImpl).getBorderMetrics(host);
				
				// adjust the host's usable size by the metrics. If hostSizedToContent, then the
				// resulting adjusted value may be less than zero.
				hostWidth -= paddingMetrics.left + paddingMetrics.right + borderMetrics.left + borderMetrics.right;
				hostHeight -= paddingMetrics.top + paddingMetrics.bottom + borderMetrics.top + borderMetrics.bottom;

				var xpos:Number = borderMetrics.left + paddingMetrics.left;
				var ypos:Number = borderMetrics.top + paddingMetrics.top;

				// First pass determines the data about the child.
				for(var i:int=0; i < n; i++)
				{
					var child:IUIBase = contentView.getElementAt(i) as IUIBase;
					if (child == null || !child.visible) continue;
					var positions:Object = childPositions(child);
					var margins:Object = childMargins(child, hostWidth, hostHeight);

					ilc = child as ILayoutChild;

					xpos += margins.left;

					var childYpos:Number = ypos + margins.top; // default y position

					var childHeight:Number = child.height;
					if (ilc != null && !isNaN(ilc.percentHeight)) {
						childHeight = hostHeight * ilc.percentHeight/100.0;
						ilc.setHeight(childHeight);
					}
					var valign:Object = ValuesManager.valuesImpl.getValue(child, "vertical-align");
					if (valign == "middle")
					{
						childYpos = hostHeight/2 - (childHeight + margins.top + margins.bottom)/2;
					}
	
					if (ilc) {
						ilc.setX(xpos);
						ilc.setY(childYpos);

						if (!isNaN(ilc.percentWidth)) {
							var newWidth:Number = hostWidth * ilc.percentWidth / 100;
							ilc.setWidth(newWidth);
						}

					} else {
						child.x = xpos;
						child.y = childYpos;
					}

					xpos += child.width + margins.right;
				}

				return true;

            }
            COMPILE::JS
            {
				/** 
				 *  This Layout uses the following CSS rules
				 *  no code needed in JS for layout
				 * 
				 *  .layout {
				 *		display: flex;
				 *	}
				 *
				 *	.layout.horizontal {
				 *		flex-flow: row nowrap;
				 *      align-items: flex-start
				 *	}
				 *  
				 *  .layout.horizontal > * {
				 *    flex: 0 0 auto
				 *  }
				 */				
                return true;
            }
		}
	}
}