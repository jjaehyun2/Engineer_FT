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
	COMPILE::JS {
    	import org.apache.royale.core.UIBase;
    }
	import org.apache.royale.core.ILayoutChild;
	import org.apache.royale.core.ILayoutView;
	import org.apache.royale.core.IUIBase;
	import org.apache.royale.events.Event;

    /**
     *  The TableLayout class is a simple layout
     *  bead.  It takes the set of children and lays them out
     *  as a Table.
     *
     *  @langversion 3.0
     *  @playerversion Flash 10.2
     *  @playerversion AIR 2.6
     *  @productversion Royale 0.9.4
     */
	public class TableLayout extends StyledLayoutBase
	{
        /**
         *  Constructor.
         *
         *  @langversion 3.0
         *  @playerversion Flash 10.2
         *  @playerversion AIR 2.6
         *  @productversion Royale 0.9.4
         */
		public function TableLayout()
		{
			super();
		}

		/**
		 * @royalesuppresspublicvarwarning
		 */
		public static const LAYOUT_TYPE_NAMES:String = "layout table";

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

			COMPILE::JS
			{
				if (hostClassList.contains("layout"))
					hostClassList.remove("layout");
				hostClassList.add("layout");
				if(hostClassList.contains("table"))
					hostClassList.remove("table");
				hostClassList.add("table");
			}
		}

        /**
         * @copy org.apache.royale.core.IBeadLayout#layout
		 * @royaleignorecoercion org.apache.royale.core.UIBase
         */
		override public function layout():Boolean
		{
            COMPILE::SWF
            {
				var contentView:ILayoutView = layoutView;

				var hostWidthSizedToContent:Boolean = host.isWidthSizedToContent();
				var hostHeightSizedToContent:Boolean = host.isHeightSizedToContent();

				var w:Number = hostWidthSizedToContent ? 0 : contentView.width;
				var h:Number = hostHeightSizedToContent ? 0 : contentView.height;

				var n:int = contentView.numElements;

                for (var i:int = 0; i < n; i++)
                {
                    var child:IUIBase = contentView.getElementAt(i) as IUIBase;
					if (child == null || !child.visible) continue;

					var positions:Object = childPositions(child);
					var margins:Object = childMargins(child, contentView.width, contentView.height);
                    var ww:Number = w;
                    var hh:Number = h;

                    var ilc:ILayoutChild = child as ILayoutChild;

					// set the top edge of the child
                    if (!isNaN(positions.left))
                    {
                        if (ilc)
                            ilc.setX(positions.left+margins.left);
                        else
                            child.x = positions.left+margins.left;
                        ww -= positions.left + margins.left;
                    }

					// set the left edge of the child
                    if (!isNaN(positions.top))
                    {
                        if (ilc)
                            ilc.setY(positions.top+margins.top);
                        else
                            child.y = positions.top+margins.top;
                        hh -= positions.top + margins.top;
                    }

					// set the right edge of the child
					if (!isNaN(positions.right))
					{
						if (!hostWidthSizedToContent)
						{
							if (!isNaN(positions.left))
							{
								if (ilc)
									ilc.setWidth(ww - positions.right - margins.right, false);
								else
									child.width = ww - positions.right - margins.right;
							}
							else
							{
								if (ilc)
								{
									ilc.setX( w - positions.right - margins.left - child.width - margins.right);
								}
								else
								{
									child.x = w - positions.right - margins.left - child.width - margins.right;
								}
							}
						}
					}
					else if (ilc != null && !isNaN(ilc.percentWidth) && !hostWidthSizedToContent)
					{
						ilc.setWidth((ww - margins.right - margins.left) * ilc.percentWidth/100, false);
					}

					// set the bottm edge of the child
					if (!isNaN(positions.bottom))
					{
						if (!hostHeightSizedToContent)
						{
							if (!isNaN(positions.top))
							{
								if (ilc)
									ilc.setHeight(hh - positions.bottom - margins.bottom, false);
								else
									child.height = hh - positions.bottom - margins.bottom;
							}
							else
							{
								if (ilc)
									ilc.setY( h - positions.bottom - child.height - margins.bottom);
								else
									child.y = h - positions.bottom - child.height - margins.bottom;
							}
						}
					}
					else if (ilc != null && !isNaN(ilc.percentHeight) && !hostHeightSizedToContent)
					{
						ilc.setHeight((hh - margins.top - margins.bottom) * ilc.percentHeight/100, false);
					}
					
					if (margins.auto)
					{
						if (ilc)
							ilc.setX( (w - child.width) / 2);
						else
							child.x = (w - child.width) / 2;
					}
                }

                return true;

            }

            COMPILE::JS
            {
				
                return true;
            }
		}
	}
}