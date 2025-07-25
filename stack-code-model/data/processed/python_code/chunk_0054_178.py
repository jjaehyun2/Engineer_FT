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
package spark.components.beads
{	
	import org.apache.royale.core.IIndexedItemRenderer;
	import org.apache.royale.core.SimpleCSSStyles;
	import org.apache.royale.core.UIBase;
	import org.apache.royale.html.beads.HorizontalListItemRendererInitializer;

	/**
	 *  The TabBarItemRendererInitializer class initializes item renderers
	 *  in TabBar tab labels.
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 10.2
	 *  @playerversion AIR 2.6
	 *  @productversion Royale 0.9.8
	 */
	public class TabBarItemRendererInitializer extends org.apache.royale.html.beads.HorizontalListItemRendererInitializer
	{
		/**
		 *  constructor.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10.2
		 *  @playerversion AIR 2.6
		 *  @productversion Royale 0.9.8
		 */
		public function TabBarItemRendererInitializer() 
		{
		}
		
		/**
		 * @royaleignorecoercion org.apache.royale.core.UIBase
		 */
		override protected function setupVisualsForItemRenderer(ir:IIndexedItemRenderer):void
		{
			var style:SimpleCSSStyles = new SimpleCSSStyles();
			style.marginBottom = presentationModel.separatorThickness;
			(ir as UIBase).style = style;
			//(ir as UIBase).height = presentationModel.rowHeight;
		}
	}
}