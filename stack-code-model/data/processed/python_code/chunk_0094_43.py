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
package mx.containers.beads
{
    import org.apache.royale.html.beads.VirtualDataContainerView;
    import org.apache.royale.core.IChild;
    import org.apache.royale.core.IParent;

	/**
	 *  The DataContainerView provides the visual elements for the DataContainer.
	 *  
	 *  @viewbead
	 *  @langversion 3.0
	 *  @playerversion Flash 10.2
	 *  @playerversion AIR 2.6
	 *  @productversion Royale 0.9.8
	 */
	public class VirtualDataContainerView extends org.apache.royale.html.beads.VirtualDataContainerView
	{
		public function VirtualDataContainerView()
		{
			super();
		}
		
        
        /**
         * @copy org.apache.royale.core.IItemRendererOwnerView#removeAllItemRenderers()
         * @private
         *
         *  @langversion 3.0
         *  @playerversion Flash 10.2
         *  @playerversion AIR 2.6
         *  @productversion Royale 0.9.8
         *  @royaleignorecoercion org.apache.royale.core.IParent
         */
        override public function removeAllItemRenderers():void
        {
            while ((contentView as IParent).numElements > 0) {
                var child:IChild = (contentView as IParent).getElementAt(1);
                (contentView as IParent).removeElement(child);
            }
        }
	}
}